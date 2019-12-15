![](https://imgur.com/download/6hKZqiN/)

**Fluent** – Simple and powerful multi-platform development framework.

## Example

Here is the basic *Hello, world* code example:

```python
from fluent.material import *  # Importing library


# Calling launch method
launch(
    # Setting target to Text widget
    target=Text(
        text='Hello, Fluent',  # Setting text to the widget
        color=color.white  # Setting color to the widget
    )  # Text
)  # launch
```

Execution result:

![](https://imgur.com/download/AahLtit/)

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

Also, you need to have `sdl2-gfx` and `sdl2-ttf` library. You can download it [here](http://www.ferzkopp.net/Software/SDL2_gfx/SDL2_gfx-1.0.4.zip) and [here](https://www.libsdl.org/projects/SDL_ttf/release/SDL2_ttf-2.0.15.zip). Unpack that, and execute following commands to compile and install the library:

```console
$ ./configure
$ make
$ make install
```

Or, in the latest release we added automated installation script that installs the latest version from our repository and installs all SDL additional packages. Execute that using:

```console
$ sh bin/install.sh
```

After installation you can try to check running version by executing following command:

```console
$ fluent version
🚀 Fluent, version 1.0.0-beta1
```

## Requirements

You need to compile and install `sdl2-gfx` and `sdl2-ttf` libraries for rendering advanced primitive shapes.
