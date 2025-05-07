import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from pathlib import Path


class ScriptDialog(toga.Window):
    def __init__(self, app):
        super().__init__(title="Select SQL Script", size=(400, 300))
        self.app = app

        # Main container
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # File selection controls
        self.file_path = toga.TextInput(placeholder="Script path", readonly=True)
        browse_btn = toga.Button(
            "Browse...", on_press=self.browse_script, style=Pack(padding=5)
        )

        # Preview area
        self.preview = toga.MultilineTextInput(readonly=True, style=Pack(flex=1))

        # Action buttons
        btn_box = toga.Box(style=Pack(direction=ROW, margin_top=10))
        load_btn = toga.Button(
            "Load Script", on_press=self.load_script, style=Pack(flex=1, padding=5)
        )
        cancel_btn = toga.Button(
            "Cancel",
            on_press=lambda widget: self.close(),
            style=Pack(flex=1, padding=5),
        )
        btn_box.add(load_btn)
        btn_box.add(cancel_btn)

        # Add components to dialog
        main_box.add(toga.Label("Select SQL script file:"))
        main_box.add(self.file_path)
        main_box.add(browse_btn)
        main_box.add(toga.Label("Preview:"))
        main_box.add(self.preview)
        main_box.add(btn_box)

        self.content = main_box

    def browse_script(self, widget):
        """Open file selection dialog"""
        try:
            # Show file selection dialog
            script_path = self.app.main_window.open_file_dialog(
                title="Select SQL Script", file_types=["sql", "txt"]
            )

            if script_path:
                self.file_path.value = script_path
                self.preview_script(script_path)
        except Exception as e:
            self.app.main_window.error_dialog("Error", str(e))

    def preview_script(self, path):
        """Show a preview of the script"""
        try:
            with open(path, "r") as f:
                content = f.read()
                # Show first 500 chars for preview
                self.preview.value = content[:500] + (
                    "..." if len(content) > 500 else ""
                )
        except Exception as e:
            self.app.main_window.error_dialog("Error", f"Could not read file: {e}")

    def load_script(self, widget):
        """Handle script loading"""
        if not self.file_path.value:
            self.app.main_window.error_dialog("Error", "No script selected")
            return

        try:
            # Here you would implement what happens when a script is loaded
            print(f"Loading script: {self.file_path.value}")

            # For example, you might want to:
            # 1. Store the script path in your app
            # 2. Parse the script
            # 3. Show it in the main view

            self.app.main_window.info_dialog(
                "Success",
                f"Script loaded successfully: {Path(self.file_path.value).name}",
            )
            self.close()
        except Exception as e:
            self.app.main_window.error_dialog("Error", str(e))
