class Link:
    """A linked list with a first element and the rest."""

    empty: tuple = ()

    def __init__(self, first, rest=empty) -> None:
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __getitem__(self, index: int):
        if index == 0:
            return self.first
        else:
            return self.rest[index - 1]

    def __len__(self) -> int:
        return 1 + len(self.rest)

    def __repr__(self) -> str:
        return link_expression(self)


def link_expression(s: Link):
    if s.rest is Link.empty:
        rest = ""
    else:
        rest = ", " + link_expression(s.rest)
    return f"Link({s.first}{rest})"


class Tree:
    def __init__(self, label, branches=()) -> None:
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = branches

    def __repr__(self) -> str:
        if self.branches:
            return f"Tree({self.label}, {repr(self.branches)})"
        else:
            return f"Tree({self.label})"

    def is_leaf(self) -> bool:
        return not self.branches


def sum_nums(s: Link):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    # total = 0
    # while s is not Link.empty:
    #     total += s.first
    #     s = s.rest
    # return total
    if s is Link.empty:
        return 0
    else:
        return s.first + sum_nums(s.rest)


def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Implementation Note: you might not need all lines in this skeleton code
    product = 1
    for link in lst_of_lnks:
        if link is Link.empty:
            return Link.empty
        product = product * link.first
    rest_list = [link.rest for link in lst_of_lnks]
    return Link(product, multiply_lnks(rest_list))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])


def flip_two(s):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    # if s is Link.empty or s.rest is Link.empty:
    #     return
    # s.first, s.rest.first = s.rest.first, s.first
    # flip_two(s.rest.rest)

    # For an extra challenge, try writing out an iterative approach as well below!
    while s is not Link.empty and s.rest is not Link.empty:
        s.first, s.rest.first = s.rest.first, s.first
        s = s.rest.rest


def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 == 1:
        t.label = t.label + 1
    for b in t.branches:
        make_even(b)


def leaves(t):
    """Returns a list of all the labels of the leaf nodes of the Tree t.

    >>> leaves(Tree(1))
    [1]
    >>> leaves(Tree(1, [Tree(2, [Tree(3)]), Tree(4)]))
    [3, 4]
    """
    all_leaves: list = []
    if t.is_leaf():
        all_leaves.append(t.label)
    for b in t.branches:
        all_leaves.extend(leaves(b))
    return all_leaves


def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths
