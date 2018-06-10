
import unittest


class TestFailed(unittest.TestCase):
    def test_failed(self):
        assert True

    def test_exception(self):
        assert 1 == 2

    def test_error(self):
        raise EOFError