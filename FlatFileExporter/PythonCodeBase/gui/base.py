from time import monotonic

from textual.app import App, ComposeResult
from textual.containers import Container
# from textual.reactive import reactive
from textual.widgets import Button, Header, Footer, Static


class Stopwatch(Static):
    """A stopwatch widget."""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        print(button_id)
        

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Generate File", id="start", variant="success")
    

class FlatFileExporter(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = FlatFileExporter()
    app.run()