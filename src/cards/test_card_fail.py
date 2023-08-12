from cards import Card


def test_equality_fail():
    c1 = Card("something", "josh")
    c2 = Card("else", "james")
    assert c1 == c2
