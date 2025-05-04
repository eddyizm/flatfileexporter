import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class ExportSection(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=5))
        self.app = app

        self.format = toga.Selection(
            items=['CSV', 'JSON', 'Excel'],
            style=Pack(padding=(0, 0, 5, 0))
        )

        self.export_btn = toga.Button(
            'Export Data',
            on_press=self.export_data,
            style=Pack(padding=(5, 0))
        )

        self.add(toga.Label('Export Format:'))
        self.add(self.format)
        self.add(self.export_btn)

    def export_data(self, widget):
        # TODO implement export functionality later
        self.app.main_window.info_dialog(
            'Info',
            f'Exporting as {self.format.value}'
        )
