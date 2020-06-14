# Lesson-04-SetUp
### 1. setUp and tearDown
```
class TestPerson(unittest.TestCase):
    def test_get_full_name(self):
        p1 = Person('Bill', 'Gates', 15)
        p2 = Person('Steve', 'Jobs', 25)
        self.assertEqual(p1.get_full_name(), 'Bill Gates')
        self.assertEqual(p2.get_full_name(), 'Steve Jobs')

    def test_is_adult(self):
        p1 = Person('Bill', 'Gates', 15)
        p2 = Person('Steve', 'Jobs', 25)
        self.assertEqual(p1.is_adult(), False)
        self.assertEqual(p2.is_adult(), True)
```
From lesson 3, we created 2 person objects in each test methods to check for the result of methods 'get_full_name()' and 'is_adult()'. It could be quite tricky if we create person objects in every test methods. The setUp() and tearDown() methods allow you to define instructions that will be executed before and after each test method. 

```
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
```
### 4. Exercise
1.Complete the 'test_calculate.py' to test method 'add(a,b)' and method 'subtract(a,b)' in the 'calculate.py'