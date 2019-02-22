..
    Copyright (C) 2019 CESNET.

    Invenio OARepo is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Installation
============

Invenio OARepo is on PyPI so all you need is:

.. code-block:: console

    $ pip install invenio-oarepo

Normally, your instance will specify the correct dependency on your database
and Elasticsearch version you use. If not, you can explict install the
dependencies via the following extra install targets:

- ``elasticsearch5``
- ``elasticsearch6``
- ``postgresql``
- ``mysql``

For instance:

.. code-block:: console

    $ pip install invenio-oarepo[postgresql,elasticsearch6]
