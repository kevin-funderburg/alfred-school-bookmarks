![demo](imgs/demo.gif)

# Alfred School Bookmarks

This little workflow was made to quickly and easily get to all the websites, folders, ebooks, zoom meetings  etc. that I need to access many times daily in school. It has turned out to be one of the most useful and highly used out of all my workflows so I wanted to share it, but since everyone is different I figured I would at least post the code and show how easily you could adjust it for yourself.

> Because of this, this repo is more of a demonstration on building an Alfred workflow rather than sharing an executable workflow to be installed.

_Here's a screenshot of the workflow itself:_

![wholeworkflow](imgs/workflow.png)


## Configuration
In this workflow, here's what I wanted to get to quickly for each class:
1. Its folder
2. Its ebook
3. Its OneNote Page
4. The class website
5. the zoom meeting (for COVID-19)

I did this by assigning the values for each one to a modifier key as in the following table.

modifer  |  opens
--|--
 <kbd>⌘</kbd> |  class website
 <kbd>⌥</kbd> |  class folder
 <kbd>⇧</kbd> |  ebook
 <kbd>⌃</kbd> |  zoom meeting
 no modifer |  OneNote section

So to store the data for each of these paths, I created a small SQlite database called `classdata.db` to store the data for each class using the following SQL command (with some privacy stuff changed):

```SQL
-- you can change these columns to whatever
-- information you would like

CREATE TABLE "fall2020" (
	"name"			TEXT NOT NULL,
	"folderPath"	TEXT NOT NULL,
	"bookPath"		TEXT,
	"oneNote"		TEXT,
	"website"		TEXT
    "zoom"          TEXT
);

INSERT INTO fall2020 VALUES (
	'Algorithm Design',
	'~/Dropbox/School/algorithm design',
	'~/Dropbox/School/algorithm design/Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms 3rd Edition (2009).pdf',
	'onenote:https://d.docs.live.net/9478a1a4ec3795b7/somethingsomething',
	'https://myclasswebsite1',
	'https://zoomurl'
	);
INSERT INTO fall2020 VALUES (
	'Compilier Construction',
	'~/Dropbox/School/compiler construction',
	'~/Dropbox/School/compiler construction/Keith Cooper, Linda Torczon - Engineering a Compiler-Elsevier Science & Technology (2011).epub',
	'onenote:https://d.docs.live.net/9478a1a4ec3795b7/somethingsomething',
	'https://myclasswebsite2',
	'https://zoomurl'
	);
INSERT INTO fall2020 VALUES (
	'Computer Networks',
	'~/Dropbox/School/computer networks',
	'~/Dropbox/School/algorithm design/Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms 3rd Edition (2009).pdf',
	'onenote:https://d.docs.live.net/9478a1a4ec3795b7/somethingsomething',
	'https://myclasswebsite2',
	'https://zoomurl'
	);

```

> Here's the result below (using DB Browser for SQLite)

![db](imgs/db.png)

Once the data is stored, you just need to make sure the `def execute_sql`function in the `getClassData.py` file fits your information. Below points out where to make the change.

```python
def execute_sql(conn, sql):
    log.info("query: " + sql)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        name = row[0]			#
        folderPath = row[1]		#
        bookPath = row[2]		# adjust these variables for your information
        oneNote = row[3]		#
        website = row[4]		#
        zoom = row[5]			#
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
```

- Once that's squared away, just make sure the `Script Filter` action lookds like this:
![scriptfilter](imgs/scriptfilter.png)

- Then just make the rest of the actions look something like this:
![actions](imgs/actions.png)


And that's it! I really recommend this one, super quick and useful, but also makes me feel much more organized.
