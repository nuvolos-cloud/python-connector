nuvolos - The database connectivity library for Nuvolos
=======================================================

Installation
============

.. code:: bash

    $ pip install nuvolos 

Usage
=====
The library provides two convenience functions for connecting to the remote database with your credentials. There are two possible usage modes. 

1. If you are running python in a Nuvolos application (e.g. JupyterLab), you don't have to provide any arguments or credentials for the library to create a SQLALchemy engine.
2. If you are running python from a non-Nuvolos application (e.g. your own computer), you have to provide four arguments: your username, your database password, the database and schema of the dataset you want to connect to. This information can be found in the Connection guide in the Nuvolos UI. 

Using in Nuvolos applications
============================

You can get the SQLAlchemy connection string or create an SQLAlchemy engine directly:

::

    >>> from nuvolos import get_url, get_engine
    >>> get_url()
    'snowflake://<username>:<password>@alphacruncher.eu-central-1/?warehouse=<username>'
    >>> get_url("db_name","schema_name")
    'snowflake://<username>:<password>@alphacruncher.eu-central-1/?warehouse=<username>&database=db_name&schema=schema_name'
    >>> eng = get_engine("db_name","schema_name")

::

Using in non-Nuvolos applications
==================================


