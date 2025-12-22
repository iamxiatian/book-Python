import unittest


class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2) 


# pytest方式 - 更简洁直观，使用原生assert
def test_add():
    assert 1 + 1 == 2  # 直接用Python的assert语句


if __name__ == "__main__":
    unittest.main()
    