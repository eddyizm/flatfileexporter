from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Header, Footer, Button, Static

# pyinstaller -F -n testtextual main.py --paths=env/Lib/site-packages --add-data="stopwatch03.tcss;."
class TimeDisplay(Static):
    """A widget to display elapsed time."""


class Stopwatch(Static):
    """A stopwatch widget."""

    def compose(self) -> ComposeResult:
        """Create child widgets of a stopwatch."""
        yield Button("Start", id="start", variant="success")
        yield Button("Stop", id="stop", variant="error")
        yield Button("Reset", id="reset")
        yield TimeDisplay("00:00:00.00")


class FlatFileExporterApp(App):
    """A Textual app export flat files."""

    CSS_PATH = "stopwatch03.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield ScrollableContainer(Stopwatch(), Stopwatch(), Stopwatch())

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = FlatFileExporterApp()
    app.run()