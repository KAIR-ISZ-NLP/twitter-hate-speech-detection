import unittest
import PreprocessModule as pm

class PreprocessModuleTests(unittest.TestCase):

    def test_LowerCase(self):
        self.assertEqual(pm.LowerCase('FOO'), 'foo')
        self.assertEqual(pm.LowerCase('Foo'), 'foo')
        self.assertEqual(pm.LowerCase('fOo'), 'foo')
        self.assertEqual(pm.LowerCase('foO'), 'foo')

    def test_Hashtags(self):
        self.assertEqual(pm.RemoveHashtags('Zaczyna się wojna #DONBAS'), 'Zaczyna się wojna ')
        self.assertEqual(pm.RemoveHashtags('#loosers Znowu przegrana :('), ' Znowu przegrana :(')

    def test_RemovePunctuation(self):
        self.assertEqual(pm.RemovePunctuation('Zaczyna się wojna ...'), 'Zaczyna się wojna ')
        self.assertEqual(pm.RemovePunctuation('- Znowu przegrana :('), ' Znowu przegrana ')

    def test_RemoveMentions(self):
        self.assertEqual(pm.RemoveMentions('Zaczyna się wojna @Ukraine'), 'Zaczyna się wojna ')
        self.assertEqual(pm.RemoveMentions('@TSW Znowu przegrana :('), ' Znowu przegrana :(')

    def test_RemoveStopWords(self):
        self.assertEqual(pm.RemoveStopWords('Zaczyna się wojna'), 'Zaczyna wojna')

if __name__ == '__main__':
    unittest.main()