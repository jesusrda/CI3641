import unittest
import io
import sys
import calc

class TestEval(unittest.TestCase):
    ''' Testing eval function '''
    def test_eval_pre(self):
        expr = "+ * + 3 4 5 7".split()
        self.assertEqual(int(calc.Evaluator.eval(1,expr)), 42)
    
    def test_eval_pre2(self):
        expr = "/ * 3 - 6 3 2".split()
        self.assertEqual(int(calc.Evaluator.eval(1,expr)), 4)

    def test_eval_pos(self):
        expr = "8 3 - 8 4 4 + * +".split()
        self.assertEqual(int(calc.Evaluator.eval(0,expr)),69)

    def test_eval_pos2(self):
        expr = "3 6 - 5 2 / *".split()
        self.assertEqual(int(calc.Evaluator.eval(0,expr)),-6)

class TestShow(unittest.TestCase):
    ''' Testing show function '''
    def setUp(self):
        self.output = io.StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_show_pre(self):
        expr = "+ * + 3 4 5 7".split()
        calc.Evaluator.show(1,expr)
        output = self.output.getvalue()
        self.assertEqual(output, "( 3 + 4 ) * 5 + 7 \n")
    
    def test_show_pre2(self):
        expr = "/ * 3 - 6 3 2".split()
        calc.Evaluator.show(1,expr)
        output = self.output.getvalue()
        self.assertEqual(output, "3 * ( 6 - 3 ) / 2 \n")
    
    def test_show_pos(self):
        expr = " 8 3 - 8 4 4 + * +".split()
        calc.Evaluator.show(0,expr)
        output = self.output.getvalue()
        self.assertEqual(output, "8 - 3 + 8 * ( 4 + 4 ) \n")
    
    def test_show_pos2(self):
        expr = "3 6 - 5 2 / *".split()
        calc.Evaluator.show(0,expr)
        output = self.output.getvalue()
        self.assertEqual(output, "( 3 - 6 ) * ( 5 / 2 ) \n")

if __name__ == '__main__':
    unittest.main()
