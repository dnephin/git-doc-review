
from docutils import io
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




def get_git_commit(filename):
    """Return author and email from last commit to filename."""
    # TODO


# TODO: reduce this to only the necessary parts by stripping the base class
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
    def write(self, build_docnames, update_docnames, method='update'):
        docnames = self.env.all_docs
        print "Docnames", docnames
        print build_docnames, update_docnames, method

        self.prepare_writing(build_docnames)

        def build_doc(docname):
            doctree = self.env.get_doctree(docname)
            doctree.settings = self.docsettings
            destination = io.StringOutput(encoding='utf-8')
            self.docwriter.write(doctree, destination)
            self.docwriter.assemble_parts()
            return self.docwriter.parts['fragment']

        doc = [build_doc(d) for d in build_docnames]
        print doc
        self.info('doing stuff... ')
        super(JsonCommentBuilder, self).write(build_docnames, update_docnames, method)

