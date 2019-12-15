from fluent.material import *  # Importing library
from fluent.widget.animation.slide import Slide


# Calling launch method
launch(
    # Setting target to Text widget
    target=Slide(
        child=Text(
            text='Hello, Fluent',  # Setting text to the widget
            color=color.white  # Setting color to the widget
        ),
        offset=10000
    )  # Text
)  # launch