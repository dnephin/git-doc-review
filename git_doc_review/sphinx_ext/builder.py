
from sphinx.builders import Builder
from sphinx.builders import html


class GitDocReviewBuilder(Builder):
    """A sphinx builder which composes two other builders. A
    standard HTMLBuilder is used for the primary document and a json
    document builder is used for the comments.
    """

    name    = 'git-doc-review'
    format  = 'html'

    def init(self):
        self.doc_builder = html.StandaloneHTMLBuilder(self.app)
        self.comment_builder = JsonBuilder(self.app)

    def get_outdated_docs(self):
        # TODO:
        return (list(self.doc_builder.get_outdated_docs()) + 
                list(self.comment_builder.get_outdated_docs()))




def get_git_committer(filename):
    """Return author and email from last commit to filename."""
    # TODO


class JsonCommentBuilder(html.JSONHTMLBuilder):
    """Build a directory of comments into a json document.
    
    Json for each comment should include:
    * git author/email
    * source filename
    * comment as html
    * response "position"
    
    """

    name    = 'comments'
    out_suffix = '.json'

    # get_target_uri
    # get_outdated_docs
    # write_doc
    # preapre_writing

    def dump_context(self, context, filename):
        print filename, context
        #import ipdb; ipdb.set_trace()
