This is the www.docker.io website repository
==============================================

It intends to be small, simple and straightforward.

Builds on
----------

* Django 1.5
* Twitter Bootstrap
* Includes tracking options such as from Google Analytics and Intercom.io


Making simple changes
---------------------

This project uses a simplified Django structure, and has the notable feature that all major text contained on this
 website can be maintained by changing the markdown files contained in /_pages/. There is a good chance this will
 be the only part you need to touch.

Files which can be easily be edited are in the _pages directory and have the .md extension.


Simple installation
-------------------

* Clone this repository
* ``pip install -r requirements.txt``
* run ``./local_setup.sh`` to setup everything related to the database.
* Done!

To preview the website run: `` ./manage.py runserver``. It will pick the local settings by default, which are
based on a local mysqlite database. Please note the tweets are now cached in the Database.

To load some data into the news, team page and events
``python manage.py loaddata base/migrations/[datafiles]``


Secrets
-------

Because this repository is in a public repository, we keep our secrets in environment variables. If you do not
set these keys, running the app might fail.

Most notable:

* SECRET_KEY
* MAILCHIMP_API_KEY


About the .md files
--------------------

Using markdown-formatted text allows separation of content (tekst) and markup (html). Depending on your setup
you might want to setup your editor to show the content with either markdown highlighting or jinja shortcuts.


Building CSS from LESS
-----------------------
We build our css from less, and we (heavily) customize bootstrap. The goal is to always have a working .css file
in the repository, so when you check it out you should not need to build the css. If, however you want to make
changes to it:

* Make changes to main.less (preferred over changing bootstrap's .less files
* Compile this using your favorite tool like recess or LiveReload

If you do make changes to the Bootstrap variables which should be reflected in the bootstrap-custom
* Find the makefile in the sources dir
* In that directory run npm install to install the required build libraries
* Run 'make docker-css' to compile the styles to bootsrap-custom

OR, if it mysteriously fails

lessc sources/less/bootstrap.less > bootstrap-custom.css


Development Guide:

IMPORTANT: IF YOU ARE RUNNING ON BLUEMIX MAKE SURE TO BIND A ELEPHANTSQL DB TO THE DJANGO APP. 

This is a two part application.
1. trycedocker: the base page that serves as a catalog for the tutorials. (https://hub.jazz.net/project/joshisa/trycedocker/overview)
2. trycedocker-tutorial: the tutorials. (https://hub.jazz.net/project/joshisa/trycedocker-tutorial/overview)

to run call the following from trycedocker: sudo pip install -r requirements.txt;  ./manage.py runserver

this will download all the dependencies from requirements.txt this includes the tutorial.
So everytime you want to update something, make sure to re-run this command and make sure any changes made to 
the tutorial have been committed to the repo: https://hub.jazz.net/project/joshisa/trycedocker-tutorial/overview


Install dev tools:
-------------------------------
install less: npm install -g less      
install coffee-script: npm install -g coffee-script

Updating questions
-------------------------------
All the questions are stored in a arrays. The basic tutorial is stored in 'q' while the advanced tutorial
is stored in 'adv_q' both of which can be found in steps.coffee. If you follow the pattern in the steps.coffee 
file it should be fairly trivial to figure out how to modify a question. When steps.cofee is modified you
will need to compile the .coffee files to javascript file. For this you will need to have coffee-script 
installed on your computer. see "Install dev tools" section above. 

Expected command: contains the strings that need to be included in the valid answer.

compilation command: coffee -c steps.coffee 
this will generate the steps.js file.

Updating the ice cli interpreter
--------------------------------
The interpreter is written in terminal.coffee, in the 'ice' function. The entire thing is really a giant set of 
if else statements. The logic flow is pretty straight forward. to generate the js files, run the following.

compilation command: coffee -c terminal.coffee 

Compiling the less to css
--------------------------------
styling can be found in the tutorial-style.less file. to compile to tutorial-style.css
run the following command: lessc tutorial-style.less > tutorial-style.css

Happy coding!


