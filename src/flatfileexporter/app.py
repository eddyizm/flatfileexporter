import toga
import asyncio
from .storage import AppConfig
from .views.main_view import MainView
from .views.config_view import ConfigView


class FlatFileExporter(toga.App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Initialize persistent configuration
        self.config_store = AppConfig("FlatFileExporter")

        # Load saved configuration
        self.saved_config = {
            "db_type": self.config_store.get("db_type", "SQL Server"),
            "server": self.config_store.get("server", ""),
            "database": self.config_store.get("database", ""),
            "username": self.config_store.get("username", ""),
        }

    def startup(self):
        """Create and show the main window."""
        # Initialize views
        self.main_view = MainView(app=self)
        self.config_view = ConfigView(app=self, initial_config=self.saved_config)

        # Create main window
        self.main_window = toga.MainWindow(title=self.name)

        # Show main view initially
        self._show_main_view()

        self.main_window.show()

    def save_configuration(self, config):
        """Save configuration to persistent storage"""
        for key, value in config.items():
            self.config_store.set(key, value)
        self.saved_config = config

    def _show_main_view(self):
        """Switch to main view (private method)"""
        self.main_window.content = self.main_view
        self.main_view.refresh_data()

    def _show_config_view(self):
        """Switch to config view (private method)"""
        self.main_window.content = self.config_view

    def execute_sql(self):
        """Simple synchronous execution with progress feedback"""
        self.main_view.console.show_working()
        self.main_view.console.log("Starting execution...")

        import time

        for i in range(5):
            time.sleep(1)  # Blocking sleep
            self.main_view.console.log(f"Completed step {i+1}")

        self.main_view.console.log("Execution finished")
        self.main_view.console.show_ready()


def main():
    return FlatFileExporter("FlatFileExporter", "org.eddyizm.flatfileexporter")
