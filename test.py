from rocket.material import *


def on_button_pressed(button):
    print(f'{button} was pressed')

launch(
    Button(
        child=Text(
            text='Hello'
        ),
        pressed=on_button_pressed
    )
)
