import tensorflow as tf
hello = tf.constant('Nacho')
sess = tf.Session()
print(sess.run(hello))