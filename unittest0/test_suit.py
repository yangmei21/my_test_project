import unittest
from unittest0.test_admin_login import TestAdminLogin
from unittest0.test_del_bussinfo import TestDelshopinfo


class TestSuite(unittest.TestCase):
    def test_suitrun(self):
        suite=unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAdminLogin))
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDelshopinfo))

        runner=unittest.TextTestRunner()
        runner.run(suite)


if __name__ == '__main__':
    unittest.main()
