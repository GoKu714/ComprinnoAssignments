import unittest
import LoginTests
import ForgotPassword

login_tests = unittest.TestLoader.loadTestsFromTestCase(LoginTests.LoginTests)
forgot_password = unittest.TestLoader.loadTestsFromTestCase(ForgotPassword.FogotPassword)

test_suite = unittest.TestSuite([login_tests, forgot_password])

unittest.TextTestRunner(verbosity=2).run(test_suite)
