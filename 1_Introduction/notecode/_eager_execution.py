#!/usr/bin/env python3
# _*_ coding:utf-8 _*_



'''
************** tensorflow.contrib.eager **************
TensorFlow 的 Eager Execution 是一种命令式编程环境，可立即评估操作，无需构建图：操作会返回具体的值，而不是构建以后再运行的计算图。
这样能让您轻松地开始使用 TensorFlow 和调试模型，并且还减少了样板代码。

https://blog.csdn.net/weixin_39506322/article/details/82316423
'''
import tensorflow as tf

#关键
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()

x = [[2.]]
m = tf.matmul(x, x)
print(m)

# 动态图的构建可以使用python控制流
a = tf.constant(12)
counter = 0
while not tf.equal(a, 1):
 if tf.equal(a % 2, 0):
   a = a / 2
 else:
   a = 3 * a + 1
 print(a)
