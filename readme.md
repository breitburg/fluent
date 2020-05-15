![](https://imgur.com/download/6hKZqiN/)

# Fluent

Pretty multi-platform apps development framework.

> **⚠️**  
> Fluent isn't ready for production yet!

## Usage

Here is the basic *Hello, world* example:

```python
from fluent.core.launch import launch
from fluent.core.property import Color
from fluent.widget.shape import Text

launch(
    target=Text(
        text='Hello, Fluent',
        color=Color(255, 255, 255)
    )
)
```

Execution result:

![](https://i.imgur.com/7kcBUeL.png)

## Features

Here is the most featured features:

- Hot reload
- Platform independent
- Easy-to-use
- All is a widget concept

## Installation

The simplest installation way is using `pip`. You can install the latest stable release by executing following command:

```console
$ pip install libfluent
```

Also, you need to have `sdl2-gfx` and `sdl2-ttf` libraries installed. You can download it from [here](http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.zip) and [here](https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.zip). Unpack that, and execute following commands to compile and install the libraries:

```console
$ ./configure
$ make
$ make install
```

> **⚡️**  
>️ This project is using [Poetry](https://python-poetry.org/) as package manager.  
> If you want to build package by your own please use `poetry build.`

## Requirements

You need to compile and install `sdl2-gfx` and `sdl2-ttf` libraries for rendering advanced primitive shapes.
