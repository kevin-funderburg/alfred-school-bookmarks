#!/usr/bin/python
# encoding: utf-8

from __future__ import unicode_literals

import sys

import sqlite3
from sqlite3 import Error
from workflow import Workflow3, ICON_INFO, ICON_WARNING, ICON_ERROR


def main(wf):

    github_school = "https://git.txstate.edu"
    github_personal = "https://github.com/kevin-funderburg"
    github_icon = "icons/Icon-elusive-github@2x.png"
    database = r"classdata.db"
    sql = "SELECT * FROM fall2020;"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # execute_sql(conn, sql)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()

        for row in rows:
            name = row[0]
            folderPath = row[1]
            bookPath = row[2]
            oneNote = row[3]
            website = row[4]
            zoom = row[5]
            it = wf.add_item(uid=name,
                             title=name,
                             subtitle="open OneNote section",
                             arg=oneNote,
                             autocomplete=name,
                             valid=True,
                             icon="icon.png",
                             icontype="file")
            it.add_modifier('cmd',
                            subtitle="go to class website: " + website,
                            arg=website,
                            valid=True)
            it.add_modifier('alt',
                            subtitle="browse in Alfred",
                            arg=folderPath,
                            valid=True)
            it.add_modifier('shift',
                            subtitle=bookPath,
                            arg=bookPath,
                            valid=True)
            it.add_modifier('ctrl',
                            subtitle="go to zoom meeting",
                            arg=zoom,
                            valid=True)


    it = wf.add_item(uid=github_school,
                     title="github - texas state",
                     subtitle=github_school,
                     arg=github_school,
                     valid=True,
                     icon=github_icon,
                     icontype="file")

    it = wf.add_item(uid=github_personal,
                     title="github - personal",
                     subtitle=github_personal,
                     arg=github_personal,
                     valid=True,
                     icon=github_icon,
                     icontype="file")

    wf.send_feedback()


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


if __name__ == '__main__':
    wf = Workflow3()
    log = wf.logger
    sys.exit(wf.run(main))
