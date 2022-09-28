from unittest import TestCase

from app import get_store


class TestApi(TestCase):
    def setUp(self) -> None:
        self.store = get_store()

    def test_api_not_return_list(self):
        self.assertNotEqual(type(self.store), type([]))

    def test_api_return_dict(self):
        self.assertEqual(type(self.store), type({}))
