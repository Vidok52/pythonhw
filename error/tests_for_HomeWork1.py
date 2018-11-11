import unittest
import lab1
import io
import sys
import copy

class TestLab1(unittest.TestCase):
    def test_printer(self):
        capt = io.StringIO()
        sys.stdout = capt
        lab1.printer("Anton")
        sys.stdout = sys.__stdout__
        result = capt.getvalue().rstrip()
        self.assertEqual(result, "Hello Anton!")
    
    def test_second_1(self):
        random = [1,2,3,4,5]
        result = lab1.sum(random)
        comparator = 0
        for i in random: 
            comparator += i
        self.assertEqual(result,comparator)
    
    def test_second_2(self):
        random = [2,3,5,6,11]
        result = lab1.multiply(random)
        comparator = 1
        for i in random:
            comparator = comparator * i
        self.assertEqual(result,comparator)
    
    def test_third(self):
        result = "Anton"
        result = result[::-1]
        self.assertEqual(result,lab1.reverse("Anton"))
    
    def test_fourth(self):
        self.assertEqual("True",lab1.isPalindrome("rar"))
        self.assertEqual("False",lab1.isPalindrome("Anton"))
    
    def test_fifth(self):
        value = [1,4,5,6]
        result = []
        for i in value:
            result.append("=##=" * i)
        self.assertEqual(result,lab1.histogram([1,4,5,6]))
    
    def test_sixth(self):
        key = 5
        ChipStr1 = ""
        for i in "Anton Golovin":
            num1 = ord(i)
            chr1 = chr(num1 + key)
            ChipStr1 = ChipStr1 + chr1
        self.assertEqual(ChipStr1,lab1.caesarCipher("Anton Golovin",5))
    
    def test_seventh(self):
        matrix = [[1,2,3],[2,3,1],[3,1,2]]
        result = copy.deepcopy(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])): result[j][i] = matrix[i][j]
        self.assertEqual(result,lab1.diagonalReverse(matrix))
    
    def test_eights(self):
        expected_output = "You got it!"
        self.assertEqual(lab1.game(0,1), expected_output)

    def test_ninth(self):
        result = "Its ok"
        self.assertEqual(result,lab1.br("[][[[[][]]][]]"))

    def test_tenth(self):
        dictionary = {}
        for i in "mississippi":
            if i in dictionary:
                dictionary[i] += 1
            else:
                dictionary[i] = 1
        self.assertEqual(dictionary,lab1.charFreq("mississippi"))
    
    def test_ninth(self):
        self.assertEqual("111000",lab1.decToBin(56))

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)