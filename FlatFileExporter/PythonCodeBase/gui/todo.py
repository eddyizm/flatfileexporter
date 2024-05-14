import flet
from flet import Checkbox, ElevatedButton, Row, TextField, Text

def invis_vis_sample(page):
    first_name = TextField()
    last_name = TextField()
    first_name.disabled = True
    last_name.disabled = True
    page.add(first_name, last_name)


def main(page):
    

    def add_clicked(e):
        page.add(Checkbox(label=new_task.value))
        new_task.value = ''
        page.update()

    new_task = TextField(hint_text="Whats needs to be done?", width=300)
    page.add(Row([new_task, ElevatedButton("Add", on_click=add_clicked)]))
    
    invis_vis_sample(page)


flet.app(target=main)