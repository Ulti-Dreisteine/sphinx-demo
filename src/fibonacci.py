# -*- coding: utf-8 -*-

import math

_SQRT_5 = math.sqrt(5)
_PHI = (1 + _SQRT_5) / 2


def approx_sum_fibonacci(n) -> int:
	"""
	:param n: Fibonacci数列项数
	:return: 数列求和结果
	"""
	return round(_PHI ** (n + 1) / _SQRT_5)



