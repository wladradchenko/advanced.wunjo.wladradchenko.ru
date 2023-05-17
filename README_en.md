[![Price](https://img.shields.io/badge/price-FREE-0098f7.svg)](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/librosa.svg)](https://badge.fury.io/py/librosa)
[![GitHub package version](https://img.shields.io/github/v/release/wladradchenko/wunjo.wladradchenko.ru?display_name=tag&sort=semver)](https://github.com/wladradchenko/wunjo.wladradchenko.ru)
[![License: MIT v1.0](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/wladradchenko/wunjo.wladradchenko.ru/blob/main/LICENSE)

<p align="right">(<a href="README_en.md">RU</a>)</p>
<div id="top"></div>

<br />
<div align="center">
  <a href="https://github.com/wladradchenko/voiceai.wladradchenko.ru">
    <img src="example/robot.gif" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">Voice AI</h3>

  <p align="center">
    Project documentation
    <br/>
    <br/>
    <br/>
    <a href="https://github.com/wladradchenko/voiceai.wladradchenko.ru/issues">Issue</a>
    ·
    <a href="https://github.com/wladradchenko/voiceai.wladradchenko.ru/issues">Features</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## About

Application for speech synthesis from text and speech recognition to text. One of the unique features of this application is the ability to create multi-dialogues with multiple voices, and the number of characters used is not limited, unlike similar web applications. You can also speak text in real time and the app will recognize it from the audio. This feature is great for dictating text instead of manually typing it.

All in all, this neural network desktop application is a handy and powerful tool for anyone who needs speech synthesis and voice-to-text recognition. Best of all, the app is free, installs locally, and is easy to use! And you can use it in the voice acting of commercials, books, games, etc.

<!-- FEATURES -->
## Setup

Requirements 3.8 <= [Python](https://www.python.org/downloads/) <=3.10 and [ffmpeg](https://ffmpeg.org/download.html).

Create venv and activate ones:

```
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

Attention! The first time you run video synthesis, models will be downloaded in .wunja/talker/checkpoints and .wunja/talker/gfpgan in size 5GB. This may take a long time.

Run:
```
briefcase dev
```

Additionally, you can create a build:
```
briefcase build
```

Run build
```
briefcase run
```

Create install packet for your OS:
```
briefcase package
```

Read more in the documentation [BeeWare](https://beeware.org/project/projects/tools/briefcase)

<!-- DOWNLOAD -->
## Install packets

[Ubuntu / Debian](https://wladradchenko.ru/static/wunjo.wladradchenko.ru/build/linux/wunjo_1.2.0.deb)

```
// Requirement to create animation is ffmpeg
sudo apt install ffmpeg

// Install app
sudo dpkg -i wunjo_{vesrion}.deb

// Attention! The first time you run video synthesis, models will be downloaded in .wunja/talker/checkpoints and .wunja/talker/gfpgan in size 5GB. This may take a long time.

// Remove app
sudo dpkg -r wunjo

// Remove cache
rm -rf ~/.wunjo
```

[MacOS](https://wladradchenko.ru/static/wunjo.wladradchenko.ru/build/macos/wunjo_macos_1.2.0.zip)

```
// Requirement to create animation is ffmpeg
brew install ffmpeg 

// Unzip app
unzip wunjo_macos_{vesrion}.zip

// Attention! The first time you run video synthesis, models will be downloaded in .wunja/talker/checkpoints and .wunja/talker/gfpgan in size 5GB. This may take a long time.

// Remove cache
rm -rf ~/.wunjo
```

[Windows](https://wladradchenko.ru/static/wunjo.wladradchenko.ru/build/windows/wunjo_1.2.0.msi)

```
// Requirement to create animation is ffmpeg, Install ffmpeg and add to Path env
setx PATH "%PATH%;C:\path\to\ffmpeg\bin"

// Install app
wunjo_{vesrion}.msi

// Attention! The first time you run video synthesis, models will be downloaded in .wunja/talker/checkpoints and .wunja/talker/gfpgan in size 5GB. This may take a long time.

//Remove cache
%USERPROFILE%/.wunjo
```

<!-- EXAMPLE -->
## Пример

<div align="center">
  <table>
  <tr>
    <th>Original</th>
    <th>Move face + Enhancer</th>
    <th>Fix face + Enhancer</th>
  </tr>
  <tr align="center">
    <td><img src="example/original.gif" alt="original" width="228" height="360"></td>
    <td><img src="example/move_enhancer.gif" alt="move_enhancer" width="228" height="360"></td>
    <td><img  src="example/static_enhancer.gif" alt="static_enhancer" width="228" height="360"></td>
  </tr>
</table>
</div>

<!-- EXAMPLE -->

<!-- VIDEO -->
## Video

[![Watch the video](https://img.youtube.com/vi/oHQR1Zx6YOk/hqdefault.jpg)](https://youtu.be/oHQR1Zx6YOk)

<!-- CONTACT -->
## Контакт

Owner: [Wladislav Radchenko](https://github.com/wladradchenko/)

Email: [i@wladradchenko.ru](i@wladradchenko.ru)

Project: [https://github.com/wladradchenko/voiceai.wladradchenko.ru](https://github.com/wladradchenko/voiceai.wladradchenko.ru)

Web site: [wladradchenko.ru/voice](https://wladradchenko.ru/voice)

<!-- PREMISE -->
## Premise

Wunjo comes from the ancient runic alphabet and represents joy and contentment, which could tie into the idea of using the application to create engaging and expressive speech. Vunyo (ᚹ) is the eighth rune of the Elder and Anglo-Saxon Futhark. Prior to the introduction of the letter W into the Latin alphabet, the letter Ƿynn (Ƿƿ) was used instead in English, derived from this rune.

<!-- CREDITS -->
## Credits

* Tacatron 2 - https://github.com/NVIDIA/tacotron2
* Waveglow - https://github.com/NVIDIA/waveglow
* Flask UI - https://github.com/ClimenteA/flaskwebgui
* BeeWare - https://beeware.org/project/projects/tools/briefcase/
* Sad Talker - https://github.com/OpenTalker/SadTalker
* Face Utils: https://github.com/xinntao/facexlib
* Face Enhancement: https://github.com/TencentARC/GFPGAN
* Image/Video Enhancement:https://github.com/xinntao/Real-ESRGAN

<p align="right">(<a href="#top">to top</a>)</p>
