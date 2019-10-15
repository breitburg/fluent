# ![](https://imgur.com/download/MjCngrh/)

Powerful mobile development framework. (Inspired by [Flutter](https://flutter.dev/))

```python
import rocket

rocket.run_app(
    rocket.widget.Text('Hello, world')
)
```

![](https://imgur.com/download/n2kudlu/)


## Advanced Example

1. Writing your own widgets:

```python
import rocket


class MyApp (rocket.widget.Widget):
    def build(self, context=None):
        return rocket.layout.Column(children=(
            rocket.widget.Text('This'),
            rocket.widget.Text('is'),
            rocket.widget.Text('example'),
            rocket.layout.Row(children=(
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
    rocket.run_app(MyApp())
```

Result of running application:

![Result](https://imgur.com/download/yn8PeQt/)

## Widgets

Currently available widgets:

- Layouts
    - Column (`rocket.layout.Column`)
    - Row (`rocket.layout.Row`)
    - Padding (`rocket.layout.Padding`)
    
- Primitives
    - Rectangle (`rocket.widget.Rectangle`)
    - Text (`rocket.widget.Text`)
    
## Rendering

It renders screen via `pygame`, then `pygame` based on `sdl2`.