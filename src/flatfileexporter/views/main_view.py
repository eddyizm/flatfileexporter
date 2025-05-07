import toga
import os
import asyncio
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .components.console_output import ConsoleOutput
from .components.script_dialog import ScriptDialog

class MainView(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, margin=10, flex=1))
        self.app = app

        # Navigation toolbar
        toolbar = toga.Box(style=Pack(direction=ROW, margin=5))
        config_btn = toga.Button(
            "Configuration",
            on_press=lambda widget: self.app._show_config_view(),
            style=Pack(margin=5),
        )
        add_script_btn = toga.Button(
            "Select SQL Script",
            on_press=self._add_script,
            # icon='resources/file-upload-line.svg',
            style=Pack(margin=5),
        )
        toolbar.add(config_btn)

        # toolbar.add(add_script_btn)
        file_toolbar = toga.Box(style=Pack(direction=ROW, margin=5))
        file_toolbar.add(add_script_btn)

        # Main content
        content_box = toga.Box(style=Pack(direction=COLUMN, flex=1))

        # Add console output
        self.console = ConsoleOutput()

        script_btn = toga.Button(
            "Generate file", on_press=self.execute_script, style=Pack(margin=10)
        )

        content_box.add(script_btn)
        content_box.add(self.console)

        self.add(toolbar)
        self.add(file_toolbar)
        self.add(content_box)

    def execute_script(self, widget):
        """Button handler - just delegates to app"""
        self.app.execute_sql()

    def refresh_data(self):
        self.console.log("Application ready")

    def _add_script(self, widget):
        self.console.log("adding sql script")
        ScriptDialog.browse_script(self, widget)
        # self.console.log(os.getcwd())
