# ![](https://imgur.com/download/cRa9Nhb/)

Powerful mobile development framework. (Inspired by [Flutter](https://flutter.dev/))

![](https://imgur.com/download/nEzr53g/)


## Example

```python
import rocket

rocket.launch(
    rocket.widget.Text('Hello, world')
)
```

![](https://imgur.com/download/n2kudlu/)


### Advanced Example

1. Writing your own widgets:

```python
import rocket


class MyApp (rocket.widget.Widget):
    def build(self):
        return rocket.widget.Column(children=(
            rocket.widget.Text('This'),
            rocket.widget.Text('is'),
            rocket.widget.Text('example'),
            rocket.widget.Row(children=(
                rocket.widget.Rectangle(
                    (100, 100), color=(255, 0, 0)
                ),
                rocket.widget.Rectangle(
                    (100, 100), color=(0, 255, 0)
                ),
                rocket.widget.Rectangle(
                    (100, 100), color=(0, 0, 255)
                )
            ), spacing=0)
        ), spacing=20)


if __name__ == '__main__':
    rocket.launch(MyApp())
```

![Result](https://imgur.com/download/yn8PeQt/)


### Material App Example

```python
from rocket import launch, material, widget


class MyApp (widget.Widget):
    hello = 0

    def build(self):
        return material.Scaffold(
            app_bar=material.AppBar(
                title=widget.Text('Material App Demo')
            ),
            body=material.Page(
                widget.Padding(
                    widget=widget.Column(
                        children=(
                            widget.Text(f'Number: {self.hello}', color=(20, 20, 20)),
                            material.PushButton('Press here', pressed=self.on_button_press)
                        ),
                        spacing=20
                    ),
                    padding=20
                )
            )
        )

    def on_button_press(self):
        self.hello += 1


launch(MyApp())
```

![](http://g.recordit.co/KNeT9XIBas.gif)

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
