"""
Using a sql script to export flat files.
"""

import toga
from .views.main_window import create_main_window


class FlatFileExporter(toga.App):
    def startup(self):
        """Create and show the main window."""
        # self.cmd_quit = toga.Command(
        #     lambda widget: self.exit(),
        #     text='Quit',
        #     shortcut=toga.Key.MOD_1 + 'q',  # Cmd-Q on macOS, Ctrl-Q on others
        #     group=toga.Group.FILE
        # )

        # Add to startup() method
        # self.cmd_about = toga.Command(
        #     self.show_about,
        #     label="About",
        #     group=toga.Group.HELP,
        #     order=1
        # )

        # self.commands.add(self.cmd_about)
        # self.commands.add(self.cmd_quit)

        self.main_window = create_main_window(app=self)
        self.main_window.show()


def main():
    return FlatFileExporter('FlatFileExporter', 'org.eddyizm.flatfileexporter')
