from setuptools import find_packages, setup

VERSION = "2.0.3"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-eventlog.svg
    :target: https://pypi.python.org/pypi/pinax-eventlog/

==============
Pinax EventLog
==============

.. image:: https://img.shields.io/pypi/v/pinax-eventlog.svg
    :target: https://pypi.python.org/pypi/pinax-eventlog/

\ 

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-eventlog.svg
    :target: https://circleci.com/gh/pinax/pinax-eventlog
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-eventlog.svg
    :target: https://codecov.io/gh/pinax/pinax-eventlog
.. image:: https://img.shields.io/github/contributors/pinax/pinax-eventlog.svg
    :target: https://github.com/pinax/pinax-eventlog/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-eventlog.svg
    :target: https://github.com/pinax/pinax-eventlog/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-eventlog.svg
    :target: https://github.com/pinax/pinax-eventlog/pulls?q=is%3Apr+is%3Aclosed

\ 

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\ 

``pinax-eventlog`` provides an easy and clean interface for logging diagnostic
as well as business intelligence data about activity that occurs in your site.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
| 1.11            |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
| 2.0             |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="an event logger for Django projects",
    name="pinax-eventlog",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-eventlog/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "eventlog": []
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.0',
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "django>=1.11",
        "six",
        'django-jsonfield'
    ],
    dependency_links=[
        'git+https://github.com/massware/django-jsonfield.git#egg=django-jsonfield',
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    zip_safe=False
)
