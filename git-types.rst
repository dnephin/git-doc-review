
Comments
========

Comments are stored as blobs in the same git repo. They reference sections of
the document or other comments.

Filesystem
----------

Comments are stored in the `./comments` directory of the repo. Each comment is
stored in a file with a unique filename (based on username, and uuid). The
unique name should prevent conflicts.

A group of comments can be added and commited together.


Comment
-------

A comment references a section of the document or another comment.

Format
------

Example document reference

.. code-block:: yaml

    reference:
        type: document
        path: .summary.paragraph[0]
        highlight: "some text" # this is optional, not yet implemented

    content: "The rst document."

Example comment reference

.. code-block:: yaml

    reference:
        type: comment
        id: dnephin_af0334a.yaml # The unique filename of the comment 
        path: .paragraph[2]
        highlight: "some text" # this is optional, not yet implemented

    content: "The rst document."
