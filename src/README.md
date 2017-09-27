Haru(Humanic Awareness and Response Unit) 
===============================================================================

<p align="center">
  <img src="http://i.imgur.com/0TUUXZO.png">
</p>

## Interface Version
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

## Getting started

먼저 음성인식(STT)과 텍스트를 음성으로 변환시키는(TTS) 모듈을 사용하기 위해 [Google Cloud Speech](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/speech_recognition) 와 [Naver TTS](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech) 의 API Key를 설정해줍니다.</br>
First, Set [Google Cloud Speech](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/speech_recognition) and [Naver TTS](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech) API Key for using STT and TTS modules.

그리고 다음과 같이 [main.py](https://github.com/CNUPiedPiper/HARU-Interface/blob/master/src/main.py) 를 실행합니다.</br>
Then run [main.py](https://github.com/CNUPiedPiper/HARU-Interface/blob/master/src/main.py) as follows.
``` bash
$ sudo python main.py
```

## Hardware Design

### Raspberry PI case 3D Modeling file
라즈베리 파이 케이스 3d stl 파일을 [이곳](https://www.dropbox.com/sh/tzxt7pajaykzqf3/AADd1HNbXNhV6j7XNzx4KZQsa?dl=0)에서 다운로드 받을 수 있습니다.</br>
You can download our Raspberry Pi case 3d stl file at [here](https://www.dropbox.com/sh/tzxt7pajaykzqf3/AADd1HNbXNhV6j7XNzx4KZQsa?dl=0).

<p align="center">
  <img src="https://i.imgur.com/7bo0Qqt.png">
</p>

### LED
저희는 [Adafruit 24 RGB LED Neopixel Ring](https://www.amazon.com/Adafruit-RGB-LED-Neopixel-Ring/dp/B00K9M3WXG/ref=sr_1_8?ie=UTF8&qid=1506436738&sr=8-8&keywords=adafruit+led) 을 사용하였으며, [이곳](https://learn.adafruit.com/neopixels-on-raspberry-pi/software) 에서 관련된 Reference를 확인 할 수 있습니다. </br>
We used [Adafruit 24 RGB LED Neopixel Ring](https://www.amazon.com/Adafruit-RGB-LED-Neopixel-Ring/dp/B00K9M3WXG/ref=sr_1_8?ie=UTF8&qid=1506436738&sr=8-8&keywords=adafruit+led) and you can check reference at [here](https://www.amazon.com/Adafruit-RGB-LED-Neopixel-Ring/dp/B00K9M3WXG/ref=sr_1_8?ie=UTF8&qid=1506436738&sr=8-8&keywords=adafruit+led).

<p align="center">
  <img src="https://i.imgur.com/8CyR2jz.jpg">
</p>

## Structure

- [/apibucket](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/apibucket) - api 모듈을 위한 디렉토리입니다. </br>
- [/detector](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/detector) - HARU를 깨우는 사용자의 행동을 탐지하는 모듈들의 디렉토리입니다. </br>
- [/recorder](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/recorder) - 사용자의 음성 명령을 바이너리 데이터로 녹음하는 모듈의 디렉토리 입니다. </br>
- [/speech_recognition](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/speech_recognition) - 바이너리 데이터로 변환시킨 음성 명령을 텍스트로 변환시키는 모듈의 디렉토리 입니다. </br>
- [/text2speech](https://github.com/CNUPiedPiper/HARU-Interface/tree/master/src/text2speech) - HARU-Server로 부터 받은 텍스트 형태의 답을 음성형태로 변환시키는 모듈의 디렉토리 입니다. </br>
- [led_controller.py](https://github.com/CNUPiedPiper/HARU-Interface/blob/master/src/led_controller.py) - led를 사용하여 HARU의 진행상황을 알 수 있도록 해주는 모듈 파일입니다. </br>
- [config.ini](https://github.com/CNUPiedPiper/HARU-Interface/blob/master/src/config.ini) - api key를 저장하여 사용하는 파일입니다. </br>
- [main.py](https://github.com/CNUPiedPiper/HARU-Interface/blob/master/src/main.py) - HARU를 실행하는 파일입니다. </br>
