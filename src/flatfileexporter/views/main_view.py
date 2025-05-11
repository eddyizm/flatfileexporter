import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from .components.console_output import ConsoleOutput
from ..models.files import FileExport


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
        toolbar.add(config_btn)

        # script selection
        add_script_btn = toga.Button(
            "Select SQL Script",
            on_press=self.open_file_dialog,
            style=Pack(margin=5),
        )

        self.file_label = toga.Label(
            "_", id="filelabel", style=Pack(direction=ROW, margin_top=15)
        )
        self.file_toolbar = toga.Box(style=Pack(direction=ROW, margin=5))

        # Create file extension selector component
        self.selection = toga.Selection(
            items=["csv", "txt", "xlsx"],
            on_change=self._file_selection,
            style=Pack(margin=5),
        )

        # Change the selection to "Charlie"
        self.selection.value = "csv"

        self.file_toolbar.add(self.selection)
        self.file_toolbar.add(self.file_label)
        self.file_toolbar.add(add_script_btn)

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

        # create file export object to hold values
        self._file_export = FileExport(filename="", filetype="", sql_query="")

    def execute_script(self, widget):
        """Button handler - just delegates to app"""

        if self._file_export.sql_query == "":
            self.console.log("Error, please select a valid sql script.")
            return
        self._file_export.filetype = self.selection.value
        self._file_export.filename = "test"
        self.app.execute_sql(self._file_export)

    def refresh_data(self):
        self.console.log("Ready")

    def _file_selection(self, widget):
        self.console.log(f"file selected: {self.selection.value}")

    def _add_script(self, widget):
        self.console.log("adding sql script")
        # ScriptDialog.browse_script(self, widget)
        script_path = toga.OpenFileDialog(
            title="Select SQL Script", file_types=["sql", "txt"]
        )
        self.console.log(type(script_path))
        self.console.log(script_path)
        self.console.log(script_path.__dict__)

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
        self.file_label.text = f"Selected: {file_path.name}"
        await self.app.main_window.info_dialog(
            "File Selected", f"Successfully selected:\n{file_path}"
        )
        with open(str(file_path), "r") as f:
            content = f.readlines()
            self._file_export.sql_query = content

            for line in content:
                self.console.log(line.replace("\n", ""))
