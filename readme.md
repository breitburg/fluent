# ![](https://imgur.com/download/Hb8KcFA/)

Powerful and simple mobile applications framework. (Inspired by [Flutter](https://flutter.dev/))

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
        return rocket.widget.VerticalStack((
            rocket.widget.Text('This'),
            rocket.widget.Text('is'),
            rocket.widget.Text('Rocket'),
            rocket.widget.HorizontalStack((
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

rocket.run_app(MyApp())
```

Result of running application:

![Result](https://imgur.com/download/yn8PeQt/)

## Widgets

Currently available widgets:

- Stack
    - Vertical Stack (`rocket.widget.VerticalStack`)
    - Horizontal Stack (`rocket.widget.HorizontalStack`)
    
- Primitives
    - Rectangle (`rocket.widget.Rectangle`)
    - Text (`rocket.widget.Text`)
    
## Rendering

It renders screen via `pygame`, then `pygame` based on `sdl2`.