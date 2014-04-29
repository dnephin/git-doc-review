
from setuptools import setup, find_packages

setup(
    name='git-doc-review',
    version='1.0',
    description='',
    author='Daniel Nephin',
    author_email='dnephin@gmail.com',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'sphinx',
        'sphinx-bootstrap-theme',
    ], 
)
