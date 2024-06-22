import logging
from logging.handlers import RotatingFileHandler
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

from DAL import check_odbc
# #313245
# tuna
TEXT = 'flat file exporter... hello world\n'

class FileExtensionCheckbox(Static):
    '''Add this optional extension in phase 2.'''
    def compose(self) -> ComposeResult:
        with Horizontal(classes='box'):
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
        if button_id == "generate":
            check_odbc()
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header(id="header")
        # yield Label('top level text header', classes='box')
        yield Static("Sidebar1", id="sidebar")
        yield Static(TEXT * 10, id="body")
        # with Container(classes='main_container'):
        #     # yield FileExtensionCheckbox()
        #     yield Input(placeholder='Select a sql script...', disabled=True, id='script-input')
        #     with Horizontal(classes='button_layout'):
        #         yield Button(id='generate', classes='center_buttons', label='Generate File')
        #         yield Button(id='exit', classes='center_buttons', label='Exit')
        yield Footer(id='footer')

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark

    def action_quit(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = FlatFileExporterApp()
    app.run()
