
from git_doc_review.sphinx_ext import builder

def setup(app):
    app.add_builder(builder.JsonCommentBuilder) 
