from textual.app import App, ComposeResult
from textual.widgets import Button
from textual.widgets import Footer
from textual.widgets import Header
from textual.widgets import Label
from textual.widgets import Static
from textual.widgets import Input
from textual.containers import Container, Grid

class FlatFileExporterApp(App):
    """A Textual app export flat files."""

    CSS_PATH = "styling.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label('top level text header')
        yield Input()
        yield Button(label='Generate File')

        yield Label()
        yield Footer()
        yield Container()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = FlatFileExporterApp()
    app.run()
