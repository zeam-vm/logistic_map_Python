#-*- using:utf-8 -*-

import time
import cupy as cp

@cp.fuse
def logisticmap_calc(x, p, mu):
        return cp.mod(cp.multiply(mu, cp.multiply(x, cp.add(x, 1))), p)

def logisticmap_loopCalc(num, x, p, mu):
        for i in range(1, 10, 1):
                x = logisticmap_calc(x, p, mu)
        return x

cp.cuda.Stream.null.synchronize()
t1 = time.time()
x = cp.arange(1, int('0x2000000', 16), dtype=cp.int64)
logisticmap_loopCalc(10, x, 6700417, 22)
cp.cuda.Stream.null.synchronize()
t2 = time.time()
diff_time = t2 - t1
print('time: {0} sec'.format(diff_time))
