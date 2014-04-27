
Comment Tree
============

A comment tree references comments about a commit.

Filesystem
----------

Stored in `.git/refs/comments` as a file with the name of the commit it
references. Contains a reference to the tree.

Example:

.. code-block:: sh

    $ cat .git/refs/comments/49100a327a6fde8ff9dbade9918855c347bb6e29
    <some sha>


Git Object
----------

A tree object.

Example:

.. code-block:: sh

    $ git cat-file -p <some sha from above>
    100644 blob <some sha>   dev_comment_about_something.rst
    100644 blob <some sha>   another_comment_about_other.rst
    ...

    $ git cat-file -t <some sha from above>
    tree



Comment
=======

A comment references some text in a blob and contains some text as a comment.
The blob may be a blob in the original document, or another comment blob, but
must be contained within the same comment tree or the tree of the commit.


Git Object
----------

.. code-block:: raw

    blob 966419e5bd6f629c2aca4b4c0327cd35cb62f508
    ref "This is the title".Summary.[1@0:2@]
    author Daniel Nephin <dnephin@gmail.com> 1398637422 -0400
    position accept

    I would like to add the following evidence_ to this discussion to
    support this idea.

    .. _evidence: http://git-scm.com/book/en/Git-Internals



