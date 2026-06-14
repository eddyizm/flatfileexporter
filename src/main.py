#!/usr/bin/env python3
import sqlite3
import uuid
from nicegui import ui
from tasks import simulate_work_order

# Setup the state DB
with sqlite3.connect('poc.db') as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS jobs (id TEXT, data TEXT, status TEXT, result TEXT)')

def get_db_rows():
    with sqlite3.connect('poc.db') as conn:
        return [{'id': r[0], 'data': r[1], 'status': r[2], 'result': r[3]} for r in conn.execute('SELECT * FROM jobs')]

def process_input():
    for line in text_input.value.strip().split('\n'):
        if not line.strip(): continue
        
        
        result = simulate_work_order(line.strip())
        with sqlite3.connect('poc.db') as conn:
            conn.execute('INSERT INTO jobs VALUES (?, ?, ?, ?)', (result.id, line.strip(), 'Pending', '-'))
        # print(result.id)
    
    text_input.set_value('')
    grid.rows[:] = get_db_rows()
    grid.update()

with ui.column().classes('w-full p-4'):
    text_input = ui.textarea('Work Orders').classes('w-full')
    ui.button('Enqueue', on_click=process_input).classes('w-full')
    
    grid = ui.table(
        columns=[
            {'name': 'id', 'label': 'ID', 'field': 'id'},
            {'name': 'data', 'label': 'Data', 'field': 'data'},
            {'name': 'status', 'label': 'Status', 'field': 'status'},
            {'name': 'result', 'label': 'Result', 'field': 'result'},
        ], 
        rows=get_db_rows()
    ).classes('w-full mt-4')

# Poll every 2 seconds to refresh the table from poc.db
ui.timer(2.0, lambda: (setattr(grid, 'rows', get_db_rows()), grid.update()))

ui.run()