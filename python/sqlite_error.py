#!/usr/bin/env python
"""Illustrate database transaction management using sqlite3.
"""

import logging
import os
import sqlite3
import sys

DB_NAME = 'mydb.sqlite'
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('db_example')

def throws():
    raise RuntimeError('this is the error message')

def create_tables(cursor):
    log.info('Creating tables')
    cursor.execute("create table module (name text, description text)")

def insert_data(cursor):
    for module, description in [('logging', 'error reporting and auditing'),
                                ('os', 'Operating system services'),
                                ('sqlite3', 'SQLite database access'),
                                ('sys', 'Runtime services'),
                                ]:
        log.info('Inserting %s (%s)', module, description)
        cursor.execute("insert into module values (?, ?)", (module, description))
    return

def do_database_work(do_create):
    db = sqlite3.connect(DB_NAME)        
    try:
        cursor = db.cursor()
        if do_create:
            create_tables(cursor)
        insert_data(cursor)
        throws()
    except:
        db.rollback()
        log.error('Rolling back transaction')
        raise
    else:
        log.info('Committing transaction')
        db.commit()
    return

def main():
    do_create = not os.path.exists(DB_NAME)
    try:
        do_database_work(do_create)
    except Exception, err:
        log.exception('Error while doing database work')
        return 1
    else:
        return 0

if __name__ == '__main__':
    sys.exit(main())
