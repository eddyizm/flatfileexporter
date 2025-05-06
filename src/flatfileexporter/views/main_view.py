import toga
import asyncio
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .components.console_output import ConsoleOutput


class MainView(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=10, flex=1))
        self.app = app

        # Navigation toolbar
        toolbar = toga.Box(style=Pack(direction=ROW, padding=5))
        config_btn = toga.Button(
            "Configuration",
            on_press=lambda widget: self.app._show_config_view(),
            style=Pack(padding=5),
        )
        toolbar.add(config_btn)

        # Main content
        content_box = toga.Box(style=Pack(direction=COLUMN, flex=1))

        # Add console output
        self.console = ConsoleOutput()

        # Add SQL script button
        script_btn = toga.Button(
            "Execute SQL", on_press=self.execute_script, style=Pack(padding=10)
        )

        content_box.add(script_btn)
        content_box.add(self.console)

        self.add(toolbar)
        self.add(content_box)

    def execute_script(self, widget):
        """Button handler - just delegates to app"""
        self.app.execute_sql()

    def refresh_data(self):
        self.console.log("Application ready")
