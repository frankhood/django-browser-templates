=============================
django-browser-templates
=============================

.. image:: https://badge.fury.io/py/django-browser-templates.svg
    :target: https://badge.fury.io/py/django-browser-templates

.. image:: https://travis-ci.org/nciccarone/django-browser-templates.svg?branch=master
    :target: https://travis-ci.org/nciccarone/django-browser-templates

.. image:: https://codecov.io/gh/nciccarone/django-browser-templates/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/nciccarone/django-browser-templates

Your project description goes here

Documentation
-------------

The full documentation is at https://django-browser-templates.readthedocs.io.

Quickstart
----------

Install django-browser-templates::

    pip install django-browser-templates

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'skels_manager',
        ...
    )

Add django-browser-templates's URL patterns:

.. code-block:: python

    from skels_manager import urls as skels_manager_urls


    urlpatterns = [
        ...
        url(r"^skels/", include(skels_manager_urls))
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
