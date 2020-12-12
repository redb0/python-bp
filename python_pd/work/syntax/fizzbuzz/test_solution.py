from itertools import product
from unittest import mock, TestCase, main

if __package__:
    from . import solution
else:
    import solution


path = f'{__package__}{"." if __package__ else ""}solution'


@mock.patch(path + '.print', create=True)
@mock.patch(path + '.input', create=True)
class FizzBuzzSolutionTests(TestCase):
    def setUp(self):
        self.versions = ('1', '2', '3')

        expected_results = [
            (1, ), (2, ), ('Fizz', ), (4, ), ('Buzz', ), ('Fizz', ), 
            (7, ), (8, ), ('Fizz', ), ('Buzz', ), (11, ), ('Fizz', ), 
            (13, ), (14, ), ('FizzBuzz', )
        ]
        self.expected = [
            (s, expected_results[:i]) for i, s in enumerate(('1', '5', '15'))
        ]

        self.errors_str = ('qwe', repr(''), '-1', '0', '000')
        self.expected_error = ('Введено некорректное значение', )

    def test_main(self, mocked_input, mocked_print):
        for (user_input, result), v in product(self.expected, self.versions):
            with self.subTest(user_input=user_input, version=v, result=result):
                mocked_input.side_effect = [user_input, v]
                solution.main()
                for call, res in zip(mocked_print.call_args_list, result):
                    self.assertEqual(call.args, res)
                mocked_input.reset_mock()
                mocked_print.reset_mock()

    def test_main_errors(self, mocked_input, mocked_print):
        for user_input in self.errors_str:
            with self.subTest(user_input=user_input):
                mocked_input.side_effect = user_input
                solution.main()
                self.assertEqual(mocked_print.call_args.args,
                                 self.expected_error)
                mocked_input.reset_mock()
                mocked_print.reset_mock()


if __name__ == '__main__':
    main()
