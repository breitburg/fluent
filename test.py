from rocket import material, launch, widget


launch(
    material.Scaffold(
        app_bar=material.AppBar(
            title=widget.Text('Demo Material App')
        ),
        home=material.Page(
            widget=widget.Padding(
                widget=material.PushButton('Press here'),
                padding=20
            )
        ),
        floating_action_button=material.FloatingActionButton()
    )
)