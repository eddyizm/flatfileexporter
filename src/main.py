from textual.app import App, ComposeResult
from textual.widgets import (
    Button,
    Footer,
    Header,
    Input,
    Label,
    Static
)
from textual.containers import (
    Container,
    Grid
)

# #313245
# tuna

class FlatFileExporterApp(App):
    """A Textual app export flat files."""

    CSS_PATH = "styling.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label('top level text header', classes='box')
        yield Input()
        yield Footer()
        with Container(classes='box'):
            yield Button(label='Generate File')
            yield Button(label='Exit')

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = FlatFileExporterApp()
    app.run()
