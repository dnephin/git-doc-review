
from setuptools import setup, find_packages

setup(
    name='git-doc-review',
    version='1.0',
    description='',
    author='Daniel Nephin',
    author_email='dnephin@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'sphinx >= 1.2.2',
        'sphinx-bootstrap-theme >= 0.4',
        'dulwich >= 0.9.6',
    ], 
)
