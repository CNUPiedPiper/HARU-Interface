#-*- coding: utf-8 -*- 
import configparser
import requests, json
import sys
from detector import hotword
from recorder import recorder
from speech_recognition import transcribe_streaming
from led_controller import Led_controller
from text2speech import text2speech
from apibucket.music_recognizer import music_recog

# Haru main class.
class Main:
    def __init__(self, server_ip, port_number):
        self.config = configparser.RawConfigParser()
        self.config.read('config.ini')
        self.server_url = 'http://' + server_ip + ':' + port_number + '/request'

        naver_id = self.config.get('NAVER', 'id')
        naver_secret = self.config.get('NAVER', 'secret')

        self.detector = hotword.hotword()
        self.rec = recorder.Recorder()
        self.speaker = text2speech.Text2Speech(naver_id, naver_secret)
        
        self.led = Led_controller()
        self.led.start()
        self.speaker.speak(u'안녕하세요')
        self.speaker.speak(u'하루를 시작합니다..')

    def request_api(self, sentence):
        data = {'sentence': sentence}
        response_body = requests.post(self.server_url, data=data)
        return response_body

    def preprocessing(self, response_body):
        data = json.loads(response_body.content)
        try:
            function_number = int(data['function_number'])
        except:
            return u'서버 오류 입니다. 다시 시도해주세요.'

        if function_number == 4: # Recording for music recognize
            self.speaker.speak(u'잠시 들어볼게요.')
            host = self.config.get('MUSIC_RECOGNIZER', 'host')
	    key = self.config.get('MUSIC_RECOGNIZER', 'key')
	    secret = self.config.get('MUSIC_RECOGNIZER', 'secret')
            answer_text = music_recog.get_music_title(host, key, secret)
            return answer_text
        else:
            answer_text = data['answer']
            
        return answer_text

    def main_flow(self):
        print('[HARU] In Main flow..')
        print('[HARU] Recording now.. Ask a question now') 
        self.led.turn_on()
        
        # Record user's order sentence.
        audio_buffer = self.rec.record_audio()

        print('[HARU] Now transcribe the audio buffer to text')
        self.led.turn_off()

        # Transcribing audio buffer streaming to korean using Google Speech Recognition api.
        sentence = transcribe_streaming.transcribe_streaming(audio_buffer)
        #sentence = u'오늘 날씨는 어때'
        #sentence = u'오늘 이슈는 뭐야'
        #sentence = u'지금 몇시야'
        #sentence = u'이 노래가 뭐지'

        self.led.turn_on()

        # Request for classifying user's order sentence.
        response_body = self.request_api(sentence)
        answer_text = self.preprocessing(response_body)

        # Speak the answer text using Naver TTS api.
        self.speaker.speak(answer_text)
        self.led.turn_off()
        
        # Call run funciton again.
        self.run()

    def run(self):
        # Detecting wake-up word.
        self.detector.start_detection(self.main_flow)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print '$sudo python main.py server_ip port_number'
        print '$sudo python main.py 192.168.1.3 5000'
        exit()

    print('[HARU] Starting the HARU-Interface')
    haru = Main(sys.argv[1], sys.argv[2])
    # haru = Main('127.0.0.1', 5000)
    haru.run()
