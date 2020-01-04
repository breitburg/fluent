from unittest import TestCase
from fluent.essential import *


class SizeTest(TestCase):
    def test_widget(self):
        widget = FilledBox(
                    size=(100, 100)
                )

        self.assertEqual(first=widget.size, second=[100, 100])

    def test_row(self):
        widget = Row(
            children=(
                FilledBox(
                    size=(100, 300)
                ),
                FilledBox(
                    size=(200, 200)
                ),
                FilledBox(
                    size=(1, 1)
                )
            )
        )

        self.assertEqual(first=widget.size, second=[200, 531])
