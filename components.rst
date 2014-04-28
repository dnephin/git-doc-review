
Components
==========

Git
---

Git handles versioning, merging, and collaboration.

* git-doc-review - start reviewing a document
* git-doc-refresh (fetch, pull, sphinx-build)
* git-doc-submit (git commit, git push)
* commit hook for validating comment format

See :doc:`git-types`


Sphinx and Docutils
-------------------

The document format and rendering.

* conf.py
* add meta-data to each section to be able to reference sections in comments
* read document specific conf.py (name, version, etc)


Sphinx Theme
~~~~~~~~~~~~

A custom theme for documents. Includes a view of comments integrated with the
document. Allows for adding new comments to a doc.

* theme based on sphinx-bootstrap-theme
* includes editor javascript/html/css
* extract comment author name/email from git commits

Editor
~~~~~~

Js app to view comments and submit comments to the web server.

* mouseover/click to view add comments to a section

Web app and server
------------------

Serves sphinx document as html. Handles add comment requests and writes files.
Adds files to git repo.

* add comment - receive POST data, save file, git add, sphinx-build