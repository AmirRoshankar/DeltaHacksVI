#import tensorflow.compat.v1 as tf
import tensorflow as tf
import numpy.matlib
import numpy as np
import pandas as dp

infectReader = dp.read_cvs('cleanData1.csv')

tf.disable_v2_behavior()
print (tf.__version__)
numStates = 51

b = np.full((numStates, 1), tf.Variable([-1], tf.float32))
w = np.full((numStates, numStates), tf.Variable([1], tf.float32))

inTest = tf.placeholder(tf.float32, [numStates, 1])
outTest = tf.placeholder(tf.float32, [numStates, 1])

# Andy and Edward plz add Data in the form of a 50 length array of ints, and a 50 length arr of 1/0

x_data = getIn()
y_data = getOut()

learning_rate = 0.001

model = np.add(np.multiply(x_data,w), b)
delta = np.array(map(tf.squarenp, (np.subtract(model,y)))) # error
loss = np.array(map(tf.reduce_sum, delta))
optimizer = np.array(map(tf.train.GradientDescentOptimizer(learning_rate).minimize, loss))
init = tf.global_variables_initializer()

with tf.Session() as sess:
  sess.run(init)

  for i in range(10000):
    feed_dict_batch = {x: x_data, y:y_data}
    sess.run(optimizer, feed_dict = feed_dict_batch)

  approx_w, approx_b = sess.run([w, b])
  print ("w= ", approx_w, "and b= ", approx_b)
print ("hello")