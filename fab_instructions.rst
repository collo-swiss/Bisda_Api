Fab File Commands
=================

Getting Started
---------------

These are commands that let you execute Python functions via the command line.

Prerequisites
~~~~~~~~~~~~~

You will need to have set up the project database::

    $ fab setup  #  creates the database and runs migrations
    $ fab run  #  runs the server at http://localhost:8040/

Database Commands
-----------------

Make Migrations ona a particular app::

    $ fab make:app  # app here is the name of the app

Run migrations::

    $ fab migrate

Create a new app::

    $ fab create:app  #app here is the name of the app

Git Commands
------------

These are some of the git commands that can be run.

Adding all modified and new files in the current directory,
 and all subdirectories to the staging area and committing::

    $ fab commit

Fetching from the remote repository to the local one::

    $ fab pull

Updating the remote repository with the local one::

    $ fab push branch    #performs a git commit, then pull and finally push (with name of branch as 'branch').


