import unittest
import calc
import strings


class TestCalc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Execute a method at starting of the class"""
        print("Start calc Test Class")

    @classmethod
    def tearDownClass(cls):
        """Execute a method at the end of the class"""
        print("End calc Test Class")

    def setUp(self):
        """Execute a method before every tests in class"""
        print("Start Test")

    def tearDown(self):
        """Execute a method after every tests in class"""
        print("End Test\n")

    def test_add(self):
        """Test Addition function"""
        self.assertEqual(calc.add(10, 5), 15)
        print("Add Test")

    def test_sub(self):
        """Test subtraction function"""
        self.assertEqual(calc.sub(10, 2), 8)
        print("Sub Test")

    def test_mul(self):
        """Test Multiplication function"""
        self.assertEqual(calc.mul(10, 5), 50)
        print("Mul Test")

    def test_div(self):
        """Test Division function"""
        self.assertEqual(calc.div(10, 2), 5, "Success")
        with self.assertRaises(ValueError):
            calc.div(10, 0)
        print("Div Test")


class TestStrings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Execute a method at starting of the class"""
        print("Start string Test Class")

    @classmethod
    def tearDownClass(cls):
        """Execute a method at the end of the class"""
        print("End string Test Class")

    def setUp(self):
        """Execute a method before every tests in class"""
        print("Start Test")

    def tearDown(self):
        """Execute a method after every tests in class"""
        print("End Test\n")

    def test_lowerString(self):
        """Test Lower String"""
        self.assertTrue(strings.lowerStr().islower())
        # self.assertTrue(strings.lowerStr().isupper())
        print("Lower String Test")

    def test_upperString(self):
        """Test Upper String"""
        self.assertTrue(strings.upperStr().isupper())
        print("Upper String Test")

    @unittest.skip("Don't Required..!!")
    def test_matchString(self):
        """Match the Strings"""
        self.assertEqual(strings.str(), "Hello")
        print("Match String Test")


if __name__ == '__main__':
    unittest.main()
