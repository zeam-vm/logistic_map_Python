#-*- using:utf-8 -*-

import time
import numpy as np

def logisticmap_calc(x, p, mu):
	return np.mod(np.multiply(mu, np.multiply(x, np.add(x, 1))), p)

def logisticmap_loopCalc(num, x, p, mu):
	for i in range(1, 10, 1):
		x = logisticmap_calc(x, p, mu)
	return x

t1 = time.time()
x = np.array([i for i in range(1, int('0x2000000', 16), 1)])
#x = np.array([i for i in range(1, 10, 1)])
logisticmap_loopCalc(10, x, 6700417, 22)
t2 = time.time()
diff_time = t2 - t1
print('time: {0} sec'.format(diff_time))