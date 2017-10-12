import sys
import sqlite3
import base64
from time import sleep

from flag_replacers import REPLACE_FUNCS

DB = 'db/scores.db'

def replace_flag(task, flag):
    REPLACE_FUNCS[task](task, flag)

def change_flag(delay, task, flag):
    sleep(delay)

    conn = sqlite3.connect(DB)
    conn.execute('pragma foreign_keys=ON')

    c = conn.cursor()

    users = c.execute('update tasks set flag=? where name = ?', (flag, task))

    conn.commit()
    conn.close()

    replace_flag(task, flag)

if __name__ == "__main__":
    delay = int(sys.argv[1])
    task = sys.argv[2]
    flag = sys.argv[3]
    change_flag(delay, task, flag)
