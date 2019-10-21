from rocket import launch, material


launch(
    material.Page(
        widget=material.PushButton(
            text='Hello'
        )
    )
)