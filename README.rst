Bisda-API
===========

Getting Started
---------------

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

Prerequisites
~~~~~~~~~~~~~

You will need the following installed before you can run the server::

    Python3.5.4
    Python3-dev

Setting up project environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone and go to the project directory::

    $ git@gitlab.com:collo_swiss/BIsda_Api.git
    $ cd path/to/project/directory/Bisda_Api

In api/config, copy the local_settings and save it as local.py in the same directory.
You should set up your own database settings.

Create a py3.5.4 virtual environment::

    $ virtualenv -p python3 env_name # env_name is the name of your virtual environment

Alternatively, if you run::

    $ which python3

you will get the path to your python3. You can then run the following command to achieve the same
results (creating a python3 virtual environment) as above::

    $ virtualenv -p <output of {which python3} above> env_name # env_name is the name of your virtual environment


Start the virtual environment to work on the project.
Run the following command::

    $ source env_name/bin/activate  # env_name is the name of your virtual environment


Install Django 2.1::

    easy_install django==2.1

Install the requirements::

    $ pip install -r dev.txt

To set up the project database in the base directory, run::

    $ invoke setup  #  creates the database and runs migrations
    $ invoke run  #  runs the server at http://localhost:8080/

Basic Invoke Commands
------------------

Open the invoke_instructions file to view basic commands automated by tasks.py.


Running the Tests
-----------------

Install the test requirements and run test command::

    $ pip install -r requirements/test.txt
    $ invoke test

