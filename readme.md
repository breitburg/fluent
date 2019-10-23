<p align="center">
  <img src="https://imgur.com/download/cRa9Nhb/"/>
</p>

Powerful mobile development framework. (Inspired by [Flutter](https://flutter.dev/))

![](https://imgur.com/download/nEzr53g/)


## Installation

1. Download library from releases on GitHub
2. Install downloaded package through `pip` or `setuptools`

## Build

How to build your apps and get fully working binary.

### Android

To build your app for Android you need to use [`python-for-android`](https://github.com/kivy/python-for-android) project. Build your app following the instructions like if you`re building a SDL app.

### iOS

Currently is no way to build your app for iOS, but we plan to implement that in the future.

### Linux/macOS/Windows

To build your app for Windows/Linux/macOS you need to use [`pyinstaller`](http://www.pyinstaller.org) project.

## How render works?

It renders widgets via `pygame.draw` module, then `pygame` based on `sdl2`. So, we can say that renders widgets through SDL2. In the future all pygame drawing methods will be replaced with sdl or different rendering library if it will be needed.
