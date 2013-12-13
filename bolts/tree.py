# TODO this is untested

class TreeNode(object):

    """
    Represents a node in a tree.
    
    A tree node has a single parent, a list of children,
    and a reference to the data it contains.
    """

    def __init__(self, data=None):
        self._parent = None
        self.children = []
        self.data = data

    def __repr__(self):
        return 'TreeNode({})'.format(repr(self.data))

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        # If this node already has a parent,
        # delete this node from that parent's children
        if self._parent:
            self._parent.children.remove(self)
        self._parent = value
        self._parent.children.append(self)

    def walk(self):
        yield self
        for child in self.children:
            for node in child.walk():
                yield node


class TreeBuilder(object):

    """
    Given records, return a tree of TreeBuilder.TreeNode instances.

    The records must define an ID and parent IDs. By default,
    TreeBuilder looks for "ID" and "parent_IDs" attributes on the record.
    Alternatively, you can subclass TreeBuilder and override the
    "_record_ID" and "_record_parent_IDs" methods.

    If you want to provide a custom TreeNode class, subclass TreeBuilder
    and override the TreeNode attribute.

    >>> records = load_records()
    >>> tree = TreeBuilder().build(records)
    >>> tree.children[0].data.foo
    'foo'
    >>> sub = tree.children[0].children
    >>> sub[0].children[0].foo
    'foo'
    """

    TreeNode = TreeNode

    def _record_parent_IDs(self, record):
        return record.parent_IDs

    def _record_ID(self, record):
        return record.ID

    def build(self, records):

        root = self.TreeNode(None)

        by_ID = {}

        def link(node, parent_ID):
            try:
                parent = by_ID[parent_ID]
                if parent is not node:
                    node.parent = parent

            except KeyError:
                pass

        # Orphans are records without a parent.
        orphans = []

        for record in records:
            parent_IDs = self._record_parent_IDs(record)

            # Important! If a record has multiple parents,
            # multiple nodes are created.
            for parent_ID in parent_IDs:

                node = self.TreeNode(record)

                ID = self._record_ID(record)
                if ID:
                    by_ID[ID] = node

                link(node, parent_ID)

                if not node.parent:
                    orphans.append((node, parent_ID))

        # It's possible that the records were defined out of order,
        # and the parent came after the child, so make a second pass
        # and attempt to link any orphans to their parents.
        #
        # If no parents were found for the orphan, link it to the root node.
        for orphan, parent_ID in orphans:
            link(orphan, parent_ID)
            if not orphan.parent:
                orphan.parent = root

        return root
