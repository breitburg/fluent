from rocket import launch, material, widget


launch(
    material.Alert(
        title=widget.Text('Test Alert', color=(0, 0, 0), font='bold'),
        subtitle=widget.Text('ma', color=(0, 0, 0))
    )
)