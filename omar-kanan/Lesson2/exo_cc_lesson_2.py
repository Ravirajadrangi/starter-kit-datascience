import unittest
import collections

# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.


def string_times(string, n):
    if not isinstance(string, str) or not isinstance(n, int) or not n >= 0:
        return 'bad argument'

    return string * n


# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    if not isinstance(nums, list):
        return 'bad argument'

    for num in nums[:4]:
        if num == 9:
            return True
    return False


# Given a string, return the count of the number of times
# that a substring length 2 appears  in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count
# the end substring).
def last2(string):
    if not isinstance(string, str):
        return 'bad argument'

    last = string[-2:]
    i = 0
    for index, lettre in enumerate(string):
        if index != 0:
            if (string[index - 1] + string[index] == last):
                i += 1
    return i - 1


# Write a program that maps a list of words into a list of
# integers representing the lengths of the correponding words.
def length_words(array):
    if not isinstance(array, list):
        return 'bad argument'

    dico = [len(word) for word in array]
    return dico


# write fizzbuzz programm
def fizzbuzz():
    for num in range(1, 200):
        fizz = num % 3 == 0
        buzz = num % 5 == 0

        if fizz and (not buzz):
            print('Fizz')
        elif (not fizz) and buzz:
            print('Buzz')
        elif fizz and buzz:
            print('FizzBuzz')
        else:
            print(num)


# Write a function that takes a number and returns a list of its digits.
def number2digits(number):
    if not isinstance(number, int):
        return 'bad argument'

    string = str(number)
    return list(int(digit) for digit in string)


# Write function that translates a text to Pig Latin and back.
# English is translated to Pig Latin by taking the first letter of every word,
# moving it to the end of the word and adding 'ay'
def pigLatin(text):
    if not isinstance(text, str):
        return 'bad argument'

    words = text.split(' ')
    new_text = ''
    for word in words:
        new_text += word[1:] + word[0] + 'ay '

    return new_text[:-1].capitalize()


# Here's our "unit tests".
class Lesson1Tests(unittest.TestCase):

    def testStringTimes(self):
        self.assertEqual(string_times('Hel', 2), 'HelHel')
        self.assertEqual(string_times('Toto', 1), 'Toto')
        self.assertEqual(string_times('P', 4), 'PPPP')

    def testArrayFront9(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]), True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]), False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]), False)

    def testLast2(self):
        self.assertEqual(last2('hixxhi'), 1)
        self.assertEqual(last2('xaxxaxaxx'), 1)
        self.assertEqual(last2('axxxaaxx'), 2)

    def testLengthWord(self):
        self.assertEqual(length_words(['hello', 'toto']), [5, 4])
        self.assertEqual(
            length_words(['s', 'ss', '59fk', 'flkj3']), [1, 2, 4, 5])

    def testNumber2Digits(self):
        self.assertEqual(number2digits(8849), [8, 8, 4, 9])
        self.assertEqual(number2digits(4985098), [4, 9, 8, 5, 0, 9, 8])

    def testPigLatin(self):
        self.assertEqual(
            pigLatin("The quick brown fox"), "Hetay uickqay rownbay oxfay")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
