[![Price](https://img.shields.io/badge/price-FREE-0098f7.svg)](https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru/blob/main/LICENSE)
[![GitHub package version](https://img.shields.io/github/v/release/wladradchenko/advanced.wunjo.wladradchenko.ru?display_name=tag&sort=semver)](https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru)
[![License: MIT v1.0](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru/blob/main/LICENSE)

<p align="right">(<a href="README_ru.md">RU</a>)</p>
<div id="top"></div>

<br />
<div align="center">
  <a href="https://github.com/wladradchenko/wunjo.wladradchenko.ru">
    <img src="example/robot.gif" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">Advanced Wunjo AI</h3>
  <h4 align="center">Extension</h4>

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

<!-- ABOUT THE EXTENSIONS -->
## About extension

The extension adds to the main application:
- Training panel of your own neural network model for voice synthesis
- Ability to use GPU
- Switching work from CPU to GPU and vice versa
- Improved background quality when creating animations
- Console to track learning progress and content generation

Note: GPU extensions available if you have CUDA installed.

<!-- ABOUT THE PROJECT -->
## About

Wunjo AI Extensions are add-on modules for extending the capabilities of Wunjo AI. Main GitHub project at <a href="https://github.com/wladradchenko/wunjo.wladradchenko.ru">link</a>.

Wunjo AI is a speech-to-text and speech-to-text recognition application. One of the unique features of this application is the ability to create multi-dialogues with multiple voices, and the number of characters used is not limited, unlike similar web applications. You can also speak text in real time and the app will recognize it from the audio. This feature is great for dictating text instead of manually typing it.

All in all, this neural network desktop application is a handy and powerful tool for anyone who needs speech synthesis and voice-to-text recognition. Best of all, the app is free, installs locally, and is easy to use! And you can use it in the voice acting of commercials, books, games, etc.

<!-- UPDATE -->
## Update 1.0.0

- [x] Added GPU usage for faster processing.
- [x] Switching work from CPU to GPU and vice versa
- [x] Background quality improvements when creating animations
- [x] Added panel for training Tacotron2 neural network model (training result in .wunjo/user_trained_voice)
- [x] Added panel for training Waveglow neural network model (training result in .wunjo/user_trained_voice)

## Update 1.0.1

- [x] Added console to track learning and synthesis progress.

## Update 1.0.2

- [x] Add inspect right format of mark file.
- [ ] Change ru and en on icon.

<!-- INSTALL -->
## Installation

Download to directory `.wunjo/extensions/{folder}`

<!-- FORMAT -->
## Extension format

To create your own extension, you will need to create a run.py file with a run method that takes the media_folder, extension_folder, app directory as input, where media_folder is the media file directory for saving the code, extension_folder is the directory of the extension itself, app is the Flask application, where you can add new pages or options.

To add new elements to the front of the project, you need to create a templates/index.html directory in your extension, where you can add new elements, js, css.

An example of creating an extension structure in this project.

## Train data format
Audio has to be in .wav format Mono channels, sample rate 22050 Hz and bit rate 352Kbts. Example for marks:

```
006522.wav|Н+е к Пл+юхиной ж+е обращ+аться, сказ+ал ред+актор. В+от он+о, д+умаю, тво+ё подсозн+ание. Сд+елайте, гол+убчик.
006523.wav|В см+ысле заш+ить? Н+а ск+орую р+уку. Вообщ+е‑т+о я н+е ум+ею… Д+а к+ак сум+еете. Кор+оче, заш+ил я ем+у бр+юки.
006524.wav|Чег+о +уж т+ам… Заглян+ул в лаборат+орию к Жбанк+ову. Собир+айся, говор+ю, пошл+и.
```

Where + is the stress in the word. 

P.S. Even if your custom dataset is smaller in terms of total number of files, individual sequences could be longer. Tacotron2's memory consumption largely depends on the sequence lengths due to the recurrent nature of the model. Ensure that sequences in your custom dataset aren't too long or consider truncating or splitting them. If you still have an error CUDA out of memory, then you can reduce batch size to 16 in hparams.yaml

<!-- VIDEO -->
## Video

[![Watch the video](https://cdn1.tenchat.ru/static/vbc-gostinder/2023-05-25/2c682bac-28cb-4fe9-8967-18a9d2aa8250.jpeg)](https://kinescope.io/204247464/original)

<!-- CONTACT -->
## Контакт

Author: [Wladislav Radchenko](https://github.com/wladradchenko/)

Email: [i@wladradchenko.ru](i@wladradchenko.ru)

Project: [https://github.com/wladradchenko/wunjo.wladradchenko.ru](https://github.com/wladradchenko/wunjo.wladradchenko.ru)

Web site: [wladradchenko.ru/voice](https://wladradchenko.ru/wunjo)

<!-- CREDITS -->
## Credits

* Tacatron 2 - https://github.com/NVIDIA/tacotron2
* Waveglow - https://github.com/NVIDIA/waveglow
* Apex - https://github.com/NVIDIA/apex

<p align="right">(<a href="#top">to top</a>)</p>
