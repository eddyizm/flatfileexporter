from textual.app import App, ComposeResult
from textual.widgets import (
    Button,
    Checkbox,
    Footer,
    Header,
    Input,
    Label,
    Static
)
from textual.containers import (
    Container,
    Grid,
    Horizontal
)

# #313245
# tuna
class FileExtensionCheckbox(Static):

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Checkbox("csv", True)
            yield Checkbox("[magenta]txt[/]")
            yield Checkbox("[b]XLSX[/b]")

class ConnectionSettings(Static):
    # TODO enter connection settings, save to file?
    # encrypt or obfuscate creds?
    pass


class FlatFileExporterApp(App):
    """A Textual app export flat files."""

    CSS_PATH = "styling.tcss"
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
        ("ctrl+q", "quit", "Quit")
    ]

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        button_id = event.button.id
        if button_id == "exit":
            self.exit()
 
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label('top level text header', classes='box')
        yield FileExtensionCheckbox(classes='box')
        yield Footer()
        with Container(classes='box'):
            yield Input(placeholder='Select a sql script...')
            yield Button(label='Generate File')
            yield Button(id='exit', label='Exit')

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = FlatFileExporterApp()
    app.run()
