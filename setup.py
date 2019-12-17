# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 CESNET.
#
# Invenio OARepo is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Open Access Repository for Invenio"""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()

INVENIO_VERSION=os.environ.get('INVENIO_VERSION', '3.1.1')

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'isort>=4.3.3',
    'pydocstyle>=2.0.0',
    'pytest-cov>=2.5.1',
    'pytest-pep8>=1.0.6',
    'Sphinx>=1.5.1',
    'invenio[base,auth,metadata,postgresql,elasticsearch6]~={0}'.format(INVENIO_VERSION),
]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'tests': tests_require,
    'deploy': [
        'this_is_just_a_library_install_oarepo_package_to_have_a_complete_repository_deployment>=1.0.0'
    ]
}

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=2.6.2',
]

install_requires = [
    'Flask-BabelEx>=0.9.3',
    # 'Flask-Debugtoolbar>=0.10.1',
]


packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('invenio_oarepo', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='invenio-oarepo',
    version=version,
    description=__doc__,
    long_description=readme,
    keywords='invenio-oarepo oarepo Invenio',
    license='MIT',
    author='Miroslav Bauer',
    author_email='bauer@cesnet.cz',
    url='https://github.com/oarepo/invenio-oarepo',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'oarepo = invenio_app.cli:cli',
        ],
        'invenio_base.blueprints': [
            'invenio_oarepo = invenio_oarepo.views:blueprint',
        ],
        # 'invenio_base.apps': [
        #     'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
        # ],
        'invenio_config.module': [
            'invenio_oarepo = invenio_oarepo.config',
        ],
        'invenio_i18n.translations': [
            'messages = invenio_oarepo',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 4 - Beta',
    ],
)
