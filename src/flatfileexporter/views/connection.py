import toga
from toga.style import Pack
from toga.style.pack import COLUMN


class ConnectionSection(toga.Box):
    def __init__(self, app):
        super().__init__(style=Pack(direction=COLUMN, padding=5))
        self.app = app

        self.db_type = toga.Selection(
            items=['SQL Server', 'PostgreSQL', 'MySQL'],
            style=Pack(padding=(0, 0, 5, 0))
        )

        self.server_input = toga.TextInput(placeholder='Server')
        self.db_input = toga.TextInput(placeholder='Database')
        self.username_input = toga.TextInput(placeholder='Username')
        self.password_input = toga.PasswordInput(placeholder='Password')

        self.test_btn = toga.Button(
            'Test Connection',
            on_press=self.test_connection,
            style=Pack(padding=(5, 0))
        )

        self.add(toga.Label('Database Type:'))
        self.add(self.db_type)
        self.add(toga.Label('Server:'))
        self.add(self.server_input)
        self.add(toga.Label('Database:'))
        self.add(self.db_input)
        self.add(toga.Label('Username:'))
        self.add(self.username_input)
        self.add(toga.Label('Password:'))
        self.add(self.password_input)
        self.add(self.test_btn)

    def test_connection(self, widget):
        try:

            params = {
                'db_type': self.db_type.value,
                'server': self.server_input.value,
                'database': self.db_input.value,
                'username': self.username_input.value,
                'password': self.password_input.value
            }

            # TODO Call backend (uncomment when ready)
            # from py.db.connector import test_connection
            # test_connection(**params)
            # self.app.main_window.dialog(toga.InfoDialog(
            #     'Success',
            #     f"Connected to {params['db_type']} at {params['server']}"
            # ))
            self.app.main_window.info_dialog(
                'Success',
                f"Connected to {params['db_type']} at {params['server']}"
            )
        except Exception as e:
            self.app.main_window.error_dialog('Error', str(e))
