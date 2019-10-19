# ![](https://imgur.com/download/cRa9Nhb/)

Powerful mobile development framework. (Inspired by [Flutter](https://flutter.dev/))

```python
import rocket

rocket.launch(
    rocket.widget.Text('Hello, world')
)
```

![](https://imgur.com/download/n2kudlu/)


## Advanced Example

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

Result of running application:

![Result](https://imgur.com/download/yn8PeQt/)

## Widgets

Currently available widgets:

- Layouts
    - Column (`rocket.widget.Column`)
    - Row (`rocket.widget.Row`)
    - Padding (`rocket.widget.Padding`)
    - Overlay (`rocket.widget.Overlay`)
    
- Shapes
    - Rectangle (`rocket.widget.Rectangle`)
    - Text (`rocket.widget.Text`)
    
## Rendering

It renders screen via `pygame`, then `pygame` based on `sdl2`.
