![](imgs/demo.gif)

# Alfred School Bookmarks

This is a little workflow I made to try and help navigate to all the websites, folders, books etc. that I use constantly throughout a semester. I am posting this as more of a demonstration seeing as what people want as a shortcut will vary for person to person, but if you want to use this is a very easy workflow to adapt.

## Configuration
In this workflow, here's what I wanted to get to quickly for each class:
1. Its folder
2. Its ebook
3. Its OneNote Page
4. The class website

So I created a small SQlite database called `classdata.db` to store the data for each class using the following SQL command (with some privacy stuff changed):

```SQL
CREATE TABLE "fall2020" (
	"name"			TEXT NOT NULL,
	"folderPath"		TEXT NOT NULL,
	"bookPath"		TEXT,
	"oneNote"		TEXT,
	"website"		TEXT
);

INSERT INTO fall2020 VALUES (
	'Algorithm Design',
	'~/Dropbox/School/algorithm design',
	'~/Dropbox/School/algorithm design/Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms 3rd Edition (2009).pdf',
    'onenote:https://d.docs.live.net/9478a1a4ec3795b7/somethingsomething',
	'https://myclasswebsite1'
	);
INSERT INTO fall2020 VALUES (
	'Compilier Construction',
	'~/Dropbox/School/compiler construction',
	'~/Dropbox/School/compiler construction/Keith Cooper, Linda Torczon - Engineering a Compiler-Elsevier Science & Technology (2011).epub',
	'onenote:https://d.docs.live.net/9478a1a4ec3795b7/somethingsomething',
	'https://myclasswebsite2'
	);
INSERT INTO fall2020 VALUES (
	'Computer Networks',
	'~/Dropbox/School/computer networks',
	'~/Dropbox/School/algorithm design/Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms 3rd Edition (2009).pdf',
    'onenote:https://d.docs.live.net/9478a1a4ec3795b7/somethingsomething',
    'https://myclasswebsite2'
	);
```

> Here's the result below (using DB Browser for SQLite)

![](imgs/db.png)

After that, it's basic python code, all I did was assign each one of the things I cared about to a modifier key:
- <kbd>⌘</kbd> = class website
- <kbd>⌥</kbd> = browse class folder
- <kbd>⇧</kbd> = open ebook
- no modifer = open OneOnte section

So if you want to adapt this for yourself, look through the `getClassData.py` file and make the adjustments for yourself.
    
