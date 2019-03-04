from os.path import dirname, abspath

from fabric.api import lcd, lcd, settings

from api.config import settings as local

BASE_DIR = dirname(abspath(__file__))


def hello():
    print("Hi Swiss")


def test():
    local("tox")


def run():
    local('{}/manage.py runserver 8000'.format(BASE_DIR))


def shell():
    local('{}/manage.py shell'.format(BASE_DIR))


def create(app):
    local('mkdir -pv "api/{}"'.format(app))
    local('{}/manage.py startapp {} api/{}'.format(BASE_DIR, app, app))


def migrate():
    local('{}/manage.py migrate'.format(BASE_DIR))


def make(app):
    local('{}/manage.py makemigrations {}'.format(BASE_DIR, app))


def commit():
    local('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
    local('git add . && git commit')


# with settings(warn_only=True):
#     result = commit()
#     if result.return_code == 0:
#         pass
#     elif result.return_code == 2:
#         pass
#     else: #print error to user
#         print (result)
#         raise SystemExit()


def pull():
    local('git merge origin/develop')
    local('git pull origin develop')


def push(branch):
    commit()
    pull()
    local('git push origin {}'.format(branch))


def setup(*args):

    sudoer = '' if 'no-sudo' in args else 'sudo psql -p 5432 -h localhost -U postgres'
    db_name = local_settings.DATABASES.get('default').get('NAME')
    db_user = local_settings.DATABASES.get('default').get('USER')
    db_pass = local_settings.DATABASES.get('default').get('PASSWORD')

    with lcd(BASE_DIR):
        local('{} -c "DROP DATABASE IF EXISTS {}"'.format(
            sudoer, db_name
        ))
        local('{} -c "CREATE DATABASE {}"'.format(sudoer, db_name))
        local('{0} -c "DROP USER IF EXISTS {1}"'.format(
            sudoer, db_user
        ))
        local(
            '{} -c "CREATE USER {} WITH SUPERUSER CREATEDB CREATEROLE '
            'LOGIN PASSWORD \'{}\'"'.format(sudoer, db_user, db_pass)
        )
        local('{} -c  "CREATE EXTENSION IF NOT EXISTS pg_trgm"'.format(
            sudoer
        ))
        local('python manage.py migrate')
