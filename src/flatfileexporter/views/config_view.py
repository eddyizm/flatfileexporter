import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
from flatfileexporter.data.DAL import check_odbc


class ConfigView(toga.Box):
    def __init__(self, app, initial_config):
        super().__init__(style=Pack(direction=COLUMN, margin=10, flex=1))
        self.app = app

        # Navigation toolbar
        toolbar = toga.Box(style=Pack(direction=ROW, margin=5))
        back_btn = toga.Button(
            "Back to Main", on_press=self._save_and_exit, style=Pack(margin=5)
        )
        toolbar.add(back_btn)

        # Configuration content
        content_box = toga.Box(style=Pack(direction=COLUMN, margin=10, flex=1))

        # Database connection fields
        self.db_type = toga.Selection(
            items=["SQL Server", "PostgreSQL", "MySQL"],
            value=initial_config.get("db_type", "SQL Server"),
            style=Pack(margin=5),
        )

        self.server_input = toga.TextInput(
            value=initial_config.get("server", ""),
            placeholder="Server",
            style=Pack(margin=5),
        )

        self.db_input = toga.TextInput(
            value=initial_config.get("database", ""),
            placeholder="Database",
            style=Pack(margin=5),
        )

        self.username_input = toga.TextInput(
            value=initial_config.get("username", ""),
            placeholder="Username",
            style=Pack(margin=5),
        )

        self.password_input = toga.PasswordInput(
            placeholder="Password", style=Pack(margin=5)
        )

        # Add fields to content box
        content_box.add(toga.Label("Database Type:"))
        content_box.add(self.db_type)
        content_box.add(toga.Label("Server:"))
        content_box.add(self.server_input)
        content_box.add(toga.Label("Database:"))
        content_box.add(self.db_input)
        content_box.add(toga.Label("Username:"))
        content_box.add(self.username_input)
        content_box.add(toga.Label("Password:"))
        content_box.add(self.password_input)

        # Add test connection button
        test_btn = toga.Button(
            "Test Connection", on_press=self._test_connection, style=Pack(margin=10)
        )
        content_box.add(test_btn)

        # Add all to main view
        self.add(toolbar)
        self.add(content_box)

    def _test_connection(self, widget):
        """Test database connection"""
        try:
            params = {
                "db_type": self.db_type.value,
                "server": self.server_input.value,
                "database": self.db_input.value,
                "username": self.username_input.value,
                "password": self.password_input.value,
            }
            # Call your backend connection test here
            check_odbc()
            print(f"Testing connection: {params}")
            self.app.main_window.info_dialog(
                "Success", f"Connected to {params['db_type']} at {params['server']}"
            )
        except Exception as e:
            self.app.main_window.error_dialog("Error", str(e))

    def _save_and_exit(self, widget):
        """Save configuration and return to main view"""
        config = {
            "db_type": self.db_type.value,
            "server": self.server_input.value,
            "database": self.db_input.value,
            "username": self.username_input.value,
        }
        self.app.save_configuration(config)
        self.app._show_main_view()
