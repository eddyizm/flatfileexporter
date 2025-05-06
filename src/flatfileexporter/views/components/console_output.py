import toga
from toga.style import Pack
from toga.style.pack import COLUMN

class ConsoleOutput(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, flex=1))
        self.output = toga.MultilineTextInput(readonly=True)
        # Replace ProgressBar with simple activity indicator
        self.status_label = toga.Label("Ready", style=Pack(padding_top=5))
        self.add(self.output)
        self.add(self.status_label)

    def log(self, message):
        self.output.value += f"{message}\n"
        self.output.scroll_to_bottom()

    def show_working(self):
        self.status_label.text = "Working..."

    def show_ready(self):
        self.status_label.text = "Ready"
