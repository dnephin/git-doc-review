"""
Flask webapp to handle api requests to add comments.
"""

from flask import Flask, request, abort
from flask import make_response

app = Flask(
    'git_doc_review.api',
    static_url_path='',
    static_folder='./_build/html',
)


template = """

.. doc-reference:: %(reference)s

%(body)s
"""


def write_comment(comment):
    with open('./comments/%s.rst') as fh:
       fh.write(template.format(comment))


# TODO: include username in the title?
# TODO: include a unique id?
def get_filename(comment):
    return os.path.join('comments', '%s.rst' % comment['title'])



@app.route('/comment', methods=['POST'])
def add_comment():
    comment = request.get_json()
    # TODO: validation of comment
    filename = get_filename(comment)
    if os.path.exists(filename):
        return make_response("Duplicate filename", 400)
    write_comment(comment)
    return "ok"
        



if __name__ == "__main__":
    app.run()

