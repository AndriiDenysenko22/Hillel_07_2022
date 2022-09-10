import sqlite3
import os

from typing import List

db_pass = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_pass)


def execute_query(connection,
                  query_sql: str) -> List:
    cur = connection.cursor()
    result = cur.execute(query_sql)
    return result


def unwrap_query_result(records: List) -> None:
    for record in records:
        print('The sum of all orders:', *record)


def get_income() -> None:
    query_sql = f'''
        SELECT SUM(UnitPrice*Quantity)
            FROM invoice_items;
    '''
    result = execute_query(connection, query_sql)
    unwrap_query_result(result)


get_income()