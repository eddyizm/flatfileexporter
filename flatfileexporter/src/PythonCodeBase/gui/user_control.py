import flet
from flet import UserControl, Text, Column, Row, ElevatedButton, TextField

class Counter(UserControl):
    def add_click(self, e):
        self.counter += 1
        self.text.value = str(self.counter)
        self.update()

    def build(self):
        self.counter = 0
        self.text = Text(str(self.counter))
        return Row([self.text, ElevatedButton("Add", on_click=self.add_click)])

def main(page):
    page.add(Counter(), Counter(), Counter())


flet.app(target=main)