[![Price](https://img.shields.io/badge/price-FREE-0098f7.svg)](https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru/blob/main/LICENSE)
[![GitHub package version](https://img.shields.io/github/v/release/wladradchenko/advanced.wunjo.wladradchenko.ru?display_name=tag&sort=semver)](https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru)
[![License: MIT v1.0](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru/blob/main/LICENSE)

<p align="right">(<a href="README.md">EN</a>)</p>
<div id="top"></div>

<br />
<div align="center">
  <a href="https://github.com/wladradchenko/wunjo.wladradchenko.ru">
    <img src="example/man.gif" alt="Logo" width="180" height="180">
  </a>

  <h3 align="center">Продвинутый Wunjo AI</h3>
  <h4 align="center">Расширение</h4>

  <p align="center">
    Документация о проекте
    <br/>
    <br/>
    <br/>
    <a href="https://github.com/wladradchenko/advanced.wunjo.wladradchenko.ru/issues">Сообщить об ошибке</a>
    ·
    <a href="https://github.com/wladradchenko/voiceai.wladradchenko.ru/issues">Запросить функцию</a>
  </p>
</div>

> Устарело: начиная с версии 1.4 использование расширений в Wunjo AI устарело.

<!-- ABOUT THE EXTENSIONS -->
## О расширении

Расширение добовляет в основное приложение:
- Панель тренировки собственной модели нейронной сети для синтеза голоса
- Возможность использовать GPU
- Переключение работы с CPU на GPU и обратно
- Улучшения качества фона, при создании анимации
- Консоль для отслеживания процесса обучения и генерации контента

Примечание: Расширения для работы с GPU, доступно, если у вас стоит CUDA.

<!-- ABOUT THE PROJECT -->
## О проекте

Расширения Wunjo AI - это дополнительные модули для расширения возможностей Wunjo AI. Основной GitHub проект по <a href="https://github.com/wladradchenko/wunjo.wladradchenko.ru">ссылке</a>.

Wunjo AI - это приложение для синтеза речи из текста и распознования речи в текст. Одной из уникальных особенностей этого приложения является возможность создавать мультидиалоги с несколькими голосами, а количество используемых символов не ограничено, в отличие от аналогичных веб-приложений. Вы также можете проговаривать текст в режиме реального времени, и приложение распознает его по аудио. Эта функция отлично подходит для диктовки текста вместо того, чтобы набирать его вручную.

В целом, это настольное приложение с нейронными сетями представляет собой удобный и мощный инструмент для всех, кто нуждается в синтезе речи и распознавании голоса в текст. Лучше всего то, что приложение бесплатно, устанавливается локально и проста в использовании! А применить вы его можете, в озвучке роликов, книг, игр, итд.

<!-- UPDATE -->
## Обновление 1.0.0

- [x] Добавлено использование GPU для ускорения обработки.
- [x] Переключение работы с CPU на GPU и обратно
- [x] Улучшения качества фона, при создании анимации
- [x] Добавлен панель для тренировки модели нейронной сети Tacotron2 (результат тренировки в .wunjo/user_trained_voice)
- [x] Добавлен панель для тренировки модели нейронной сети Waveglow (результат тренировки в .wunjo/user_trained_voice)

## Обновление 1.0.1

- [x] Добавлена консоль для отслеживания процесса обучения и синтеза.

## Обновление 1.0.2

- [x] Добавить проверить правильный формат файла метки.
- [ ] Сменить ru и en на иконке.
      
<!-- INSTALL -->
## Установка

Скачать в директорию `.wunjo/extensions/{folder}`

<!-- FORMAT -->
## Формат расширения

Для создания своего собственного расширения вам понадобится создать файл run.py с методом run. Метод run должен принимать на вход параметры media_folder, extension_folder, app, где media_folder - директория медиа файлов для сохранения результатов работы кода, extension_folder - директория самого расширения, app - приложение Flask, в который вы можете добавлять новые страницы или параметры.

Для добавления новых элементов в интерфейс приложения, вам необходимо создать в своем расширении директорию templates/index.html, в который вы можете добавлять новые элементы, js, css.

Пример создания структуры расширения в этом проекте.

<!-- VIDEO -->
## Видео

[![Watch the video](https://cdn1.tenchat.ru/static/vbc-gostinder/2023-05-25/2c682bac-28cb-4fe9-8967-18a9d2aa8250.jpeg)](https://kinescope.io/204247464/original)

<!-- CONTACT -->
## Контакт

Автор: [Wladislav Radchenko](https://github.com/wladradchenko/)

Почта: [i@wladradchenko.ru](i@wladradchenko.ru)

Проект: [https://github.com/wladradchenko/wunjo.wladradchenko.ru](https://github.com/wladradchenko/wunjo.wladradchenko.ru)

Сайт приложения: [wladradchenko.ru/voice](https://wladradchenko.ru/wunjo)


<!-- CREDITS -->
## Зависимости

* Tacatron 2 - https://github.com/NVIDIA/tacotron2
* Waveglow - https://github.com/NVIDIA/waveglow
* Apex - https://github.com/NVIDIA/apex


<p align="right">(<a href="#top">вернуться наверх</a>)</p>
