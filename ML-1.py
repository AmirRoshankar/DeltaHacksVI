# import tensorflow as tf
import tensorflow.compat.v1 as tf
import numpy as np

tf.disable_v2_behavior()
print (tf.__version__)

b = tf.Variable([.3], tf.float32)
w = tf.Variable([-.3], tf.float32)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

# x_data [-3,-2,-1,0,1,2,3]
# y_data [12,11,10,9,8,7,6]
x_data = [-3,-2,-1,0,1,2,3,  5, 0, 12] #tweak
y_data = [12,11,10,9,8,7,6,  4, 9, -3]

learning_rate = 0.001 #tweak

model = w*x + b
delta = tf.square(model-y) #error function
loss = tf.reduce_sum(delta)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)

  for i in range(1000): #tweak number of running time
    feed_dict_batch = {x: x_data, y: y_data}
    sess.run(optimizer, feed_dict = feed_dict_batch)

  approx_w, approx_b = sess.run([w,b])
  print("w =", approx_w, "and b =", approx_b)


print('hello bietch')
