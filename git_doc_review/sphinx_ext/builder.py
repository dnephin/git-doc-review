
import os.path

from docutils import io
from sphinx.builders import Builder
from sphinx.builders import html
from sphinx.util import osutil


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

    def write(self, build_docnames, update_docnames, method='update'):
        # TODO: only rebuild updated?
        self.prepare_writing(build_docnames)

        def build_doc(docname):
            doctree = self.env.get_doctree(docname)
            doctree.settings = self.docsettings
            destination = io.StringOutput(encoding='utf-8')
            self.docwriter.write(doctree, destination)
            self.docwriter.assemble_parts()
            return self.docwriter.parts['fragment']

        def build_context(docname):
            body = build_doc(docname)
            return os.path.basename(docname), dict(body=body)

        self.info('building comments...')
        context = dict(build_context(name) for name in build_docnames)
        self.info('doing stuff... ')

        # TODO: get docname from config
        outfilename = os.path.join(self.outdir, 'comments.json')
        osutil.ensuredir(os.path.dirname(outfilename))
        self.dump_context(context, outfilename)
