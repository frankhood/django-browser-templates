=====
Usage
=====

To use django-browser-templates in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'skels_manager.apps.SkelsManagerConfig',
        ...
    )

Add django-browser-templates's URL patterns:

.. code-block:: python

    from skels_manager import urls as skels_manager_urls


    urlpatterns = [
        ...
        url(r'^', include(skels_manager_urls)),
        ...
    ]
