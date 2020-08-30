-- this is an example of the SQL I executed, change it to fit your needs

CREATE TABLE "fall2020" (
	"name"				TEXT NOT NULL,
	"folderPath"		TEXT NOT NULL,
	"bookPath"			TEXT,
	"oneNote"			TEXT,
	"website"			TEXT,
	"zoom"				TEXT
);

INSERT INTO fall2020 VALUES (
	'Algorithm Design',
	'~/Dropbox/School/algorithm design',
	'~/Dropbox/School/algorithm design/Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms 3rd Edition (2009).pdf',
	'onenote:https://d.docs.live.net/somethingsomething
	'https://class1 website',
	'https://zoomlink'
	);
INSERT INTO fall2020 VALUES (
	'Compilier Construction',
	'~/Dropbox/School/compiler construction',
	'~/Dropbox/School/compiler construction/Keith Cooper, Linda Torczon - Engineering a Compiler-Elsevier Science & Technology (2011).epub',
	'onenote:https://d.docs.live.net/somethingsomething',
	'https://class2 website',
	'https://zoomlink'
	);
INSERT INTO fall2020 VALUES (
	'Computer Networks',
	'~/Dropbox/School/computer networks',
	'~/Dropbox/School/algorithm design/Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein - Introduction to Algorithms 3rd Edition (2009).pdf',
	'onenote:https://d.docs.live.net/somethingsomething',
	'https://class3 website',
	'https://zoomlink'
	);
