import unittest

def create_phone_number(n):
    return "({0}) {1}-{2}".format("".join(str(x) for x in n[:3]), "".join(str(x) for x in n[3:6]), "".join(str(x) for x in n[6:]))



class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")

    def test_2(self):
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")

    def test_3(self):
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")

    def test_4(self):
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")                
