from unittest import TestCase
from text_finder import find_substring


class TestCharSubstring(TestCase):
    @staticmethod
    def setup_test(substring, string, expected_indexes):
        return find_substring(substring, string) == expected_indexes

    def test_one_char_substring_one_line_text(self):
        assert self.setup_test('s', 'abrakadabrasabracadabra', [(1, 11, 1, 11)]) is True

    def test_one_char_substring_many_line_text(self):
        assert self.setup_test('s', 'abrakadabrasabracadabra\nabrakadabrasabracadabra\nabrakadabrasabracadabra',
                               [(1, 11, 1, 11), (2, 11, 2, 11), (3, 11, 3, 11)]) is True

    def test_one_char_substring_text_with_empty_lines(self):
        assert self.setup_test('s', 'abrakadabrasabracadabra\n\n\nabrakadabrasabracadabra\n\n\nabrakadabrasabracadabra',
                               [(1, 11, 1, 11), (4, 11, 4, 11), (7, 11, 7, 11)]) is True

    def test_one_char_substring_text_with_empty_line_in_begin(self):
        assert self.setup_test('s', '\nabrakadabrasabracadabra\nabrakadabrasabracadabra\nabrakadabrasabracadabra',
                               [(2, 11, 2, 11), (3, 11, 3, 11), (4, 11, 4, 11)]) is True

    def test_one_char_substring_text_with_empty_line_in_end(self):
        assert self.setup_test('s', 'abrakadabrasabracadabra\nabrakadabrasabracadabra\nabrakadabrasabracadabra\n',
                               [(1, 11, 1, 11), (2, 11, 2, 11), (3, 11, 3, 11)]) is True

    def test_one_char_substring_text_empty(self):
        assert self.setup_test('s', '', []) is True

    def test_one_char_substring_text_same(self):
        assert self.setup_test('s', 's', []) is True

    def test_one_char_substring_text_many_same_chars(self):
        assert self.setup_test('s', 'ssssssssssssssssssssss',
                               [(1, 0, 1, 0), (1, 1, 1, 1), (1, 2, 1, 2), (1, 3, 1, 3), (1, 4, 1, 4), (1, 5, 1, 5),
                                (1, 6, 1, 6), (1, 7, 1, 7), (1, 8, 1, 8), (1, 9, 1, 9), (1, 10, 1, 10), (1, 11, 1, 11),
                                (1, 12, 1, 12), (1, 13, 1, 13), (1, 14, 1, 14), (1, 15, 1, 15), (1, 16, 1, 16),
                                (1, 17, 1, 17), (1, 18, 1, 18), (1, 19, 1, 19), (1, 20, 1, 20)]) is True

    def test_one_char_substring_text_many_same_chars_many_lines(self):
        assert self.setup_test('s', 'ssssss\nssssss\nssss',
                               [(1, 0, 1, 0), (1, 1, 1, 1), (1, 2, 1, 2), (1, 3, 1, 3), (1, 4, 1, 4), (1, 5, 1, 5),
                                (2, 0, 2, 0), (2, 1, 2, 1), (2, 2, 2, 2), (2, 3, 2, 3), (2, 4, 2, 4), (2, 5, 2, 5),
                                (3, 0, 3, 0), (3, 1, 3, 1), (3, 2, 3, 2)]) is True

    def test_one_char_substring_text_without_subs(self):
        assert self.setup_test('s', 'abracadabra\nabracadabra\nabracadabra', []) is True


class TestDigitSubstring(TestCase):
    @staticmethod
    def setup_test(substring, string, expected_indexes):
        return find_substring(substring, string) == expected_indexes

    def test_one_digit_substring_one_line_text(self):
        assert self.setup_test('6', 'abrakadabra6abracadabra', [(1, 11, 1, 11)]) is True

    def test_one_digit_substring_many_line_text(self):
        assert self.setup_test('6', 'abrakadabra6abracadabra\nabrakadabra6abracadabra\nabrakadabra6abracadabra',
                               [(1, 11, 1, 11), (2, 11, 2, 11), (3, 11, 3, 11)]) is True

    def test_one_digit_substring_text_with_empty_lines(self):
        assert self.setup_test('6', 'abrakadabra6abracadabra\n\n\nabrakadabra6abracadabra\n\n\nabrakadabra6abracadabra',
                               [(1, 11, 1, 11), (4, 11, 4, 11), (7, 11, 7, 11)]) is True

    def test_one_digit_substring_text_with_empty_line_in_begin(self):
        assert self.setup_test('6', '\nabrakadabra6abracadabra\nabrakadabra6abracadabra\nabrakadabra6abracadabra',
                               [(2, 11, 2, 11), (3, 11, 3, 11), (4, 11, 4, 11)]) is True

    def test_one_digit_substring_text_with_empty_line_in_end(self):
        assert self.setup_test('6', 'abrakadabra6abracadabra\nabrakadabra6abracadabra\nabrakadabra6abracadabra\n',
                               [(1, 11, 1, 11), (2, 11, 2, 11), (3, 11, 3, 11)]) is True

    def test_one_digit_substring_text_empty(self):
        assert self.setup_test('6', '', []) is True

    def test_one_digit_substring_text_same(self):
        assert self.setup_test('6', '6', []) is True

    def test_one_digit_substring_text_many_same_chars(self):
        assert self.setup_test('6', '6666666666666666666666',
                               [(1, 0, 1, 0), (1, 1, 1, 1), (1, 2, 1, 2), (1, 3, 1, 3), (1, 4, 1, 4), (1, 5, 1, 5),
                                (1, 6, 1, 6), (1, 7, 1, 7), (1, 8, 1, 8), (1, 9, 1, 9), (1, 10, 1, 10), (1, 11, 1, 11),
                                (1, 12, 1, 12), (1, 13, 1, 13), (1, 14, 1, 14), (1, 15, 1, 15), (1, 16, 1, 16),
                                (1, 17, 1, 17), (1, 18, 1, 18), (1, 19, 1, 19), (1, 20, 1, 20)]) is True

    def test_one_digit_substring_text_many_same_chars_many_lines(self):
        assert self.setup_test('6', '666666\n666666\n6666',
                               [(1, 0, 1, 0), (1, 1, 1, 1), (1, 2, 1, 2), (1, 3, 1, 3), (1, 4, 1, 4), (1, 5, 1, 5),
                                (2, 0, 2, 0), (2, 1, 2, 1), (2, 2, 2, 2), (2, 3, 2, 3), (2, 4, 2, 4), (2, 5, 2, 5),
                                (3, 0, 3, 0), (3, 1, 3, 1), (3, 2, 3, 2)]) is True

    def test_one_digit_substring_text_without_subs(self):
        assert self.setup_test('6', 'abracadabra\nabracadabra\nabracadabra', []) is True


