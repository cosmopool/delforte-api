from setuptools import setup

setup(
    name='zione',
    packages=['zione'],
    version="1.0.0",
    include_package_data=True,
    install_requires=[
        'Flask==2.0.3',
        'flask-restx==0.5.1',
        'marshmallow==3.14.1',
        'psycopg==3.0.9',
        'psycopg[binary]',
        'Flask-JWT-Extended==4.3.1',
    ],
)
