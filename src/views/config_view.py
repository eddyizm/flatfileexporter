# views/config_view.py
from nicegui import ui, app

def config_page_content():
    ui.label("Configuration Settings").classes('text-h5')
    with ui.card():
        ui.input('SQL Server Address').bind_value(app.storage.user, 'db_host')
        ui.number('Port', value=1433)
        ui.button('Save Config', on_click=lambda: ui.notify('Saved!'))