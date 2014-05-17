
from docutils.parsers.rst import Directive
from docutils import nodes


class reference_node(nodes.Invisible, nodes.Element):
    pass


def visit_reference_node(self, node):
    pass


class ReferenceDirective(Directive):
    pass



    

