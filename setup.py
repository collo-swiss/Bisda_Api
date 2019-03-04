import os
import re
import ast
from setuptools import find_packages, setup


# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


_version_re = re.compile(r'__version__\s+=\s+(.*)')


with open('api/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name="Mammoth-Api",
    version=version,
    author="mesozi developers",
    author_email="gathumbi@mesozi.com",
    description="",
    license="BSD",
    keywords="mammoth",
    url="https://gitlab.com/mesozi/mammoth/api",
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=[
        'Django~=1.11.1',
        'django-filter==1.0.2',
        'djangorestframework==3.6.3',
        'psycopg2==2.7.1',
        'dj-database-url==0.4.2',
        'django-rest-auth==0.9.1',
        'djangorestframework-jwt==1.10.0',
        'django-cors-headers==2.0.2'
    ],
    classifiers=[
        "Development Status :: 1 - Alpha",
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        "License :: OSI Approved :: BSD License",
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
