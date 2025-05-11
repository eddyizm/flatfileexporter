import toga
import os
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .components.console_output import ConsoleOutput

# from .components.script_dialog import ScriptDialog


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
            on_press=self.open_file_dialog,
            # on_press=self._add_script,
            # icon='resources/file-upload-line',
            style=Pack(margin=5),
        )
        toolbar.add(config_btn)
        self.file_label = toga.Label(
            "_", id="filelabel", style=Pack(direction=ROW, margin_top=15)
        )
        # toolbar.add(add_script_btn)
        self.file_toolbar = toga.Box(style=Pack(direction=ROW, margin=5))

        self.file_toolbar.add(self.file_label)
        self.file_toolbar.add(add_script_btn)

        # # Create UI elements
        # self.open_button = toga.Button(
        #     "Open SQL File",
        #     on_press=self.open_file_dialog,
        #     style=Pack(padding=10)
        # )

        # # Add a label to show selected file info
        # self.file_label = toga.Label(
        #     "No file selected",
        #     style=Pack(padding=(0, 5, 10, 5))
        # )

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
        self.add(self.file_toolbar)
        self.add(content_box)

    def execute_script(self, widget):
        """Button handler - just delegates to app"""
        self.app.execute_sql()

    def refresh_data(self):
        self.console.log("Application ready")

    def _add_script(self, widget):
        self.console.log("adding sql script")
        # ScriptDialog.browse_script(self, widget)
        script_path = toga.OpenFileDialog(
            title="Select SQL Script", file_types=["sql", "txt"]
        )
        self.console.log(type(script_path))
        self.console.log(script_path)
        self.console.log(script_path.__dict__)

    #         breakpoint()

    async def open_file_dialog(self, widget):
        try:
            file_path = await self.app.main_window.open_file_dialog(
                title="Select SQL File",
                file_types=["sql", "txt"],
                multiple_select=False,
            )

            if file_path:
                await self.handle_file_selection(file_path)

        except ValueError as e:
            self.file_label.text = "File selection canceled"
            print(f"No file selected: {e}")

    async def handle_file_selection(self, file_path):
        # Update the UI
        self.file_label.text = f"Selected: {file_path.name}"

        # Show confirmation dialog
        await self.app.main_window.info_dialog(
            "File Selected", f"Successfully selected:\n{file_path}"
        )
        with open(str(file_path), "r") as f:
            content = f.readlines()

            for line in content:
                self.console.log(line.replace("\n", ""))
        # Here you would typically:
        # 1. Read the SQL file (file_path.read())
        # 2. Process the content
        # 3. Update other parts of your UI
