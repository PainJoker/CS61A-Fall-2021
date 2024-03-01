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


def extend_link(s: Link, t: Link):
    if s is Link.empty:
        return t
    else:
        return Link(s, extend_link(s.rest, t))


def add(s: Link, v: int):
    """Lecture quiz for ordered Link s.

    >>> s = Link(1, Link(3, Link(5)))
    >>> add(s, 0)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 3)
    Link(0, Link(1, Link(3, Link(5))))
    >>> add(s, 4)
    Link(0, Link(1, Link(3, Link(4, Link(5)))))
    >>> add(s, 8)
    Link(0, Link(1, Link(3, Link(4, Link(5, Link(8))))))
    """
    assert s is not Link.empty, "Reach the end!"
    if s.first > v:
        s.first, s.rest = v, Link(s.first, s.rest)
    elif s.first < v and s.rest is Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest, v)
    return s


def map_link(f, s: Link) -> Link:
    if s is Link.empty:
        return s
    else:
        return Link(f(s.first), map_link(f, s.rest))


def keep_if_link(f, s: Link) -> Link:
    if f(s.first):
        return Link(s.first, keep_if_link(s.rest))
    else:
        return Link(keep_if_link(s.rest))


def joint_link(s: Link, separator: str) -> Link:
    if s is Link.empty:
        return ""
    elif s.rest is Link.empty:
        return str(s.first)
    else:
        return str(s.first) + separator + joint_link(s.rest, separator)


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


def fib_tree(n: int) -> Tree:
    if n == 1:
        return Tree(0)
    elif n == 2:
        return Tree(1)
    else:
        left = fib_tree(n - 2)
        right = fib_tree(n - 1)
        return Tree(left.label + right.label, [left, right])


def sum_label(t: Tree):
    return t.label + sum([sum_label(b) for b in t.branches])


def empty(s: Link):
    return s is Link.empty


def set_contains(s: Link, v):
    """Return True if and only if set s contains v."""
    if empty(s):
        return False
    elif s.first == v:
        return True
    else:
        return set_contains(s.rest, v)


def adjoin_set(s: Link, v):
    """Return a set containing all element of s and element v."""
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)


def intersect_set(set1, set2) -> Link:
    """Return a set containing all elements common to set1 and set2."""
    return keep_if_link(lambda v: set_contains(set2, v), set1)


def union_set(set1: Link, set2: Link) -> Link:
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = keep_if_link(lambda v: not set_contains(set2, v), set1)
    return extend_link(set1_not_set2, set2)
