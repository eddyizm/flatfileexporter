import sqlite3
import random
import time

from huey.contrib.sql_huey import SqlHuey
from peewee import PostgresqlDatabase
import logging 

pg_db = PostgresqlDatabase(
    '<DBNAME>',
    user='<USER>',
    password="<PW>",
    host='<HOST>',
    port=<PORT>
)

huey = SqlHuey(name='ff_queue', database=pg_db, results=True)

log = logging.getLogger()

@huey.task(context=True)
def simulate_work_order(data, task=None) -> int:
    log.info('Simulate work')
    time.sleep(random.randint(3, 10))
    record_id = task.id
    with sqlite3.connect('poc.db') as conn:
        res = conn.execute(
            'UPDATE jobs SET status = ?, result = ? WHERE id = ?',
            ('Completed', f'Processed: {data}', record_id)
        )
        log.info(res)
        log.info('updated db')
    return 1
