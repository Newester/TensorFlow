#!/isr/bin/env python3
# _*_ coding:utf-8 _*_

'''
************* tensorflow.palceholder *************
placeholder 意思是占位符，相当于函数“形式参数”，运行时需要被赋值）

https://www.jianshu.com/p/195e4da1dde7

'''

import tensorflow as tf
import numpy as np

# 定义placeholder
input1 = tf.placeholder(tf.float32)
input2 = tf.placeholder(tf.float32)

# 定义乘法运算
output = tf.multiply(input1, input2)

# 通过session执行乘法运行
with tf.Session() as sess:
    # 执行时要传入placeholder的值
    print(sess.run(output, feed_dict = {input1:[7.], input2: [2.]}))

    