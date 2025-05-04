"""
Using a sql script to export flat files.
"""

import toga
from .views.main_window import create_main_window


class FlatFileExporter(toga.App):
    def startup(self):
        """Create and show the main window."""
        self.main_window = create_main_window(app=self)
        self.main_window.show()


def main():
    return FlatFileExporter('FlatFileExporter', 'org.eddyizm.flatfileexporter')
