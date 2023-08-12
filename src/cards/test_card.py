import unittest

import cards
from cards import Card


class TestCard(unittest.TestCase):
    def test_field_access(self):
        c = Card("something", "brian", "todo", 123)
        assert c.summary == "something"
        assert c.owner == "brian"
        assert c.state == "todo"
        assert c.id == 123

    def test_defaults(self):
        c = Card()
        assert c.summary is None
        assert c.owner is None
        assert c.id is None
        assert c.state == "todo"

    def test_equality(self):
        c1 = Card("some stuff", "josh", "todo", 1)
        c2 = Card("some stuff", "josh", "todo", 1)
        assert c1 == c2

    def test_equality_with_diff_id(self):
        c1 = Card("test stuff", "james", "todo", 1)
        c2 = Card("test stuff", "james", "todo", 2)
        assert c1 == c2

    def test_inequality(self):
        c1 = Card("a thing", "a name", "todo", 1)
        c2 = Card("a different thing", "a diff name", "done", 1)
        assert c1 != c2

    def test_from_dict(self):
        c1 = Card("test stuff", "james", "todo", 1)
        c2_dict = {
            "summary": "test stuff",
            "owner": "james",
            "state": "todo",
            "id": 1
        }
        c2 = Card.from_dict(c2_dict)
        assert c1 == c2


    def test_to_dict(self):
        c1 = Card("test stuff", "james", "todo", 1)
        c2 = c1.to_dict()
        c2_expected = {
            "summary": "test stuff",
            "owner": "james",
            "state": "todo",
            "id": 1
        }
        assert c2 == c2_expected


if __name__ == '__main__':
    unittest.main()
