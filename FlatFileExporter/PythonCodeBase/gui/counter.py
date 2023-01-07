import flet
from flet import IconButton, Page, Row, Text, TextField, icons, ElevatedButton
from time import sleep


def add_hello_world(_page):
    t = Text(value="Hello, world!", color="green")
    # _page.controls.append(t)
    # _page.update()
    # t = Text()
    _page.add(t) # it's a shortcut for page.controls.add(t) and then page.update()

    for i in range(10):
        t.value = f"Step {i}"
        _page.update()
        sleep(1)

    _page.add(
        Row(controls=[
            TextField(label="Your name"),
            ElevatedButton(text="Say my name!")
        ])
    )

    return _page


def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"
    
    txt_number = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )

    page = add_hello_world(page)

    

flet.app(target=main) # run as native app
# flet.app(target=main, view=flet.WEB_BROWSER) # run as web app