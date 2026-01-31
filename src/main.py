#!/usr/bin/env python3
from nicegui import ui
from core import constants
from utils import get_version_from_file

with ui.header().classes(replace="row items-center") as header:
    with ui.tabs() as tabs:
        ui.tab(constants.NAV_HOME)
        ui.tab(constants.NAV_CONFIG)
        ui.tab(constants.NAV_LOG)

with ui.footer(value=False) as footer:
    ui.label(get_version_from_file())


with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon="contact_support").props("fab")

with ui.tab_panels(tabs, value=constants.NAV_HOME).classes("w-full"):
    with ui.tab_panel(constants.NAV_HOME):
        ui.label("Home")
    with ui.tab_panel(constants.NAV_CONFIG):
        ui.label("Config")
    with ui.tab_panel(constants.NAV_LOG):
        ui.label("Log")

ui.run(fastapi_docs=True)
