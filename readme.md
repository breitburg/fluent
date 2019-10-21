# ![](https://imgur.com/download/cRa9Nhb/)

Powerful mobile development framework. (Inspired by [Flutter](https://flutter.dev/))

![](https://imgur.com/download/nEzr53g/)


## Installation

1. Download library from releases on GitHub
2. Install downloaded package

```console
pip install rocket-x.x.x.tar.gz
```

3. Enjoy!

## Example

```python
import rocket

rocket.launch(
    rocket.widget.Text('Hello, world')
)
```

![](https://imgur.com/download/n2kudlu/)

## Widgets

Currently available widgets:

- Layouts
    - Column (`rocket.widget.Column`)
    - Row (`rocket.widget.Row`)
    - Padding (`rocket.widget.Padding`)
    - Overlay (`rocket.widget.Overlay`)
    
- Shapes
    - Rectangle (`rocket.widget.Rectangle`)
    - Ellipse (`rocket.widget.Ellipse`)
    - Text (`rocket.widget.Text`)
    
- Material
    - Push Button (`rocket.material.PushButton`)
    - Floating Action Button (`rocket.material.FloatingActionButton`)
    - Page (`rocket.material.Page`)
    - Scaffold (`rocket.material.Scaffold`)
    - App Bar (`rocket.material.AppBar`)

## Rendering

It renders screen via `pygame`, then `pygame` based on `sdl2`.
