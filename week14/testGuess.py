import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

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
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')


    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d e n t u ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f n t u ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l n t u ')

    def testGuess(self):
        self.assertEqual(self.g1.currentStatus, '_e_____')
        self.g1.guess('a')
        self.assertEqual(self.g1.currentStatus, '_e_a___')
        self.g1.guess('t')
        self.assertEqual(self.g1.currentStatus, '_e_a__t')
        self.g1.guess('u')
        self.assertEqual(self.g1.currentStatus, '_e_au_t')
        self.g1.guess('d')
        self.assertEqual(self.g1.currentStatus, 'de_au_t')
        self.g1.guess('f')
        self.assertEqual(self.g1.currentStatus, 'defau_t')
        self.g1.guess('l')
        self.assertEqual(self.g1.currentStatus, 'default')

        self.assertFalse(self.g1.guess('1'))
        self.assertFalse(self.g1.guess(' '))
        self.assertFalse(self.g1.guess('z'))
        self.assertFalse(self.g1.guess('h'))
        self.assertFalse(self.g1.guess('k'))
        self.assertFalse(self.g1.guess('@'))


        self.assertTrue(self.g1.guess('d'))
        self.assertTrue(self.g1.guess('def'))

if __name__ == '__main__':
    unittest.main()
