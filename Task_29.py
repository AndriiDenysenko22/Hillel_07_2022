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
        print('Unique first_name:', *record)


def get_firstname() -> None:
    query_sql = f'''
        SELECT FirstName,COUNT(FirstName)
            FROM customers
            GROUP BY FirstName;
    '''
    result = execute_query(connection, query_sql)
    unwrap_query_result(result)


get_firstname()
