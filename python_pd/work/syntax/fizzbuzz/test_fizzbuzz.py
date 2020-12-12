from unittest import mock, TestCase, main

if __package__:
    from . import fizzbuzz
else:
    import fizzbuzz


path = f'{__package__}{"." if __package__ else ""}fizzbuzz'


def get_test_data():
    return [
        (1, ), (2, ), ('Fizz', ), (4, ), ('Buzz', ), ('Fizz', ), 
        (7, ), (8, ), ('Fizz', ), ('Buzz', ), (11, ), ('Fizz', ), 
        (13, ), (14, ), ('FizzBuzz', )
    ]


@mock.patch(path + '.print', create=True)
@mock.patch(path + '.input', create=True)
class FizzBuzzMainTests(TestCase):
    def setUp(self):
        self.errors_str = ('qwe', repr(''), '-1', '0', '000')
        self.expected_error = (('Введено некорректное значение', ), )

        expected_results = get_test_data()
        self.expected = [
            (s, expected_results[:i]) for i, s in enumerate(('1', '5', '15'))
        ]
        self.expected += [(s, self.expected_error) for s in self.errors_str]

    def test_main(self, mocked_input, mocked_print):
        for user_input, result in self.expected:
            with self.subTest(user_input=user_input, result=result):
                mocked_input.side_effect = user_input
                fizzbuzz.main()
                for call, res in zip(mocked_print.call_args_list, result):
                    self.assertEqual(call.args, res)
                mocked_input.reset_mock()
                mocked_print.reset_mock()


@mock.patch(path + '.print', create=True)
class FizzBuzzTests(TestCase):
    def setUp(self):
        self.errors_number = (-1, 0)

        expected_results = get_test_data()
        self.test_data = [(i, expected_results[:i]) for i in [1, 2, 3, 5, 15]]

    def test_fizzbuzz(self, mocked_print):
        for number, expected in self.test_data:
            with self.subTest(number=number):
                fizzbuzz.fizzbuzz(number)
                for call, res in zip(mocked_print.call_args_list, expected):
                    self.assertEqual(call.args, res)
                mocked_print.reset_mock()

    def test_exception(self, mocked_print):
        for number in self.errors_number:
            with self.subTest(number=number):
                fizzbuzz.fizzbuzz(number)
                self.assertFalse(mocked_print.called)


if __name__ == '__main__':
    main()
