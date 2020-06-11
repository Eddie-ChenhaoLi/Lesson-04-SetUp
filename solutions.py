import unittest
from person import Person


class TestPerson(unittest.TestCase):

    def setUp(self):
        print('Test start.')
        self.p1 = Person('Bill', 'Gates', 15)
        self.p2 = Person('Steve', 'Jobs', 25)

    def tearDown(self):
        print('Test finish.')

    def test_get_full_name(self):
        self.assertEqual(self.p1.get_full_name(), 'Bill Gates')
        self.assertEqual(self.p2.get_full_name(), 'Steve Jobs')

    def test_is_adult(self):
        self.assertEqual(self.p1.is_adult(), False)
        self.assertEqual(self.p2.is_adult(), True)

    def test_get_info(self):
        self.assertEqual(self.p1.get_info(), 'Bill Gates: 15')
        self.assertEqual(self.p2.get_info(), 'Steve Jobs: 25')

    def test_get_email(self):
        self.assertEqual(self.p1.get_email(), 'Bill.Gates@email.com')
        self.assertEqual(self.p2.get_email(), 'Steve.Jobs@email.com')