#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from __future__ import print_function
import tensorflow as tf 

hello = tf.constant('Hello World !')
sess = tf.Session()

print(sess.run(hello))
sess.close()