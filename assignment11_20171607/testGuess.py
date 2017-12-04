import unittest

from hangman import Hangman
from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Hangman()

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('1') # 1일때는 영어가 아니므로 출력이 되면 안된다.
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('&') # & 기호일때도 영어가 아니므로 출력이 안된다.
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('1')
        self.assertEqual(self.g1.displayGuessed(), ' 1 a e n t u ')
        self.g1.guess('&')
        self.assertEqual(self.g1.displayGuessed(), ' & 1 a e n t u ')

    def testDecreaseLife(self):
        self.assertEqual(self.g2.remainingLives, 7)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 6)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 5)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 4)
        self.g2.decreaseLife()
        self.assertEqual(self.g2.remainingLives, 3)
if __name__ == '__main__':
    unittest.main()
