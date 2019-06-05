""" 
Unit Test per Calculator Library
"""

import calculator

class TestCalculator():
	def test_add(self):
		assert 4 == calculator.add(2, 2)

	def test_substract(self):
		assert 3 == calculator.subtract(4,1)

	def test_multiplication(self):
		assert 100 = calculator.multiplication(10,10)
