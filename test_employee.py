import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Nikos', 'Nikou', 50000)
        self.emp_2 = Employee('Prokopis', 'Pandhs', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Nikos.Nikou@email.com')
        self.assertEqual(self.emp_2.email, 'Prokopis.Pandhs@email.com')

        self.emp_1.first = 'Ninos'
        self.emp_2.first = 'Alekos'

        self.assertEqual(self.emp_1.email, 'Ninos.Nikou@email.com')
        self.assertEqual(self.emp_2.email, 'Alekos.Pandhs@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Nikos Nikou')
        self.assertEqual(self.emp_2.fullname, 'Prokopis Pandhs')

        self.emp_1.first = 'Ninos'
        self.emp_2.first = 'Alekos'

        self.assertEqual(self.emp_1.fullname, 'Ninos Nikou')
        self.assertEqual(self.emp_2.fullname, 'Alekos Pandhs')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Nikou/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Pandhs/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()