import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from .connection import ConnectionSection
from .export import ExportSection


def create_main_window(app):
    """Factory function to create the main window."""
    window = toga.MainWindow(title=app.formal_name)
    print(window.toolbar.__dict__)

    # Main container
    main_box = toga.Box(
        style=Pack(direction=COLUMN, padding=10, flex=1)
    )
    # TODO Move these to their own pages --Create sections
    connection_section = ConnectionSection(app)
    export_section = ExportSection(app)

    # Add sections to main container
    main_box.add(connection_section)
    main_box.add(export_section)

    window.content = main_box
    return window
