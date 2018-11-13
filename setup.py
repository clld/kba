from setuptools import setup, find_packages


setup(
    name='kba',
    version='0.0',
    description='kba',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='SHH DLCE Dev',
    author_email='lingweb@shh.mpg.de',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=4.2.2',
        'clldmpg',
        'sqlalchemy',
        'waitress',
    ],
    extras_require={
        'dev': [
            'flake8',
            'tox',
        ],
        'test': [
            'psycopg2',
            'mock',
            'pytest>=3.1',
            'pytest-clld>=0.4',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
            'selenium',
            'zope.component>=3.11.0',
        ],
    },
    test_suite="kba",
    entry_points="""\
    [paste.app_factory]
    main = kba:main
""")
