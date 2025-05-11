import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class ConsoleOutput(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, flex=1))
        self.output = toga.MultilineTextInput(
            readonly=True, style=Pack(flex=1, font_family="monospace", margin_bottom=5)
        )
        self.status_label = toga.Label(
            "Application Log", style=Pack(margin_top=5, margin_bottom=5)
        )
        self.add(self.status_label)
        self.add(self.output)

        self.clear_output_btn = toga.Button(
            "Clear output",
            on_press=self._clear_console,
            style=Pack(margin=5),
        )
        self.add(self.clear_output_btn)

    def log(self, message):
        self.output.value += f"{message}\n"
        self.output.scroll_to_bottom()

    def _clear_console(self, widget):
        self.output.value = ""
        self.log("Ready")
