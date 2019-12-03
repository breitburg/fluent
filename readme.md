# Fluent

Powerful mobile & desktop app development kit (Inspired by Flutter)

## Features

List of the most featured features 🧐

- All is a widget paradigm 
- Hot reload
- Support multiple platforms
- Pure Python
- Super-simple

## Installation

The simplest installation way is using `pip`. You can install the latest stable release by executing following command:
```console
$ pip install libfluent
```

Also, you need to have `sdl2-gfx` library. You can download it [here](http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.zip). Unpack that, and execute following commands to compile and install the library:

```console
$ ./configure
$ make
$ make install
```

After installation you can try to check running version by executing following command:

```console
$ fluent version
🚀 Fluent, version 0.0.2
```

This command will create an empty project with codebase.

## Requirements

1. You need to compile and install `sdl2-gfx` library for rendering advanced primitive shapes
2. Must be installed `pysdl2` library
3. Library `reloadr` must be installed for hot reloading

## Issues

- No ability to set fonts
- Text widget size is zero