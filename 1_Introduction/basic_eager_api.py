#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from __future__ import absolute_import,division,print_function
import tensorflow as tf
import numpy as np
import tensorflow.contrib.eager as tfe

tfe.enable_eager_execution()

a = tf.constant(2)
b = tf.constant(3)
c = a + b
print('a + b = %i' % c)
d = a * b
print('a * b = %i' % d)

a = tf.constant([[2.,1.],[1.,0.]], dtype=tf.float32)
b = tf.constant([[3.,0.],[5.,1.]],dtype=np.float32)
c = a + b
print('a + b = %s' % c)
d = tf.matmul(a,b)
print('a * b = %s' % d)

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        print(a[i][j])



