'''
인공지능 훈련 및 관찰

인공지능이 어떻게 학습하는지 관찰할 수 있다

'''


import os
import tensorflow as tf
from tensorflow.core.protobuf import saver_pb2
import driving_data
import model
import numpy as np
import time

begin = time.strftime('%Y-%m-%d_%H-%M-%S')

LOGDIR = './save'

# Sets the threshold for what messages will be logged.
tf.logging.set_verbosity(tf.logging.ERROR)

# TensorFlow = 연산을 실행하기 위한 클래스
# Session 객체 = Operation 객체가 실행되고 Tensor 객체가 계산되는 환경을 캡슐화한다

# 생성시 자기 자신을 기본 세션으로 설치한다 -- 무슨 말? 세션을 시작한다?
sess = tf.InteractiveSession()

L2NormConst = 0.001

# Returns all variables created with trainable=True
# trainable 변수와 non-trainable 변수의 차이점?
train_vars = tf.trainable_variables()

start_learning_rate = 0.5e-3    ###1e-3
adjust_learning_rate = 1e-5

onehot_labels = tf.one_hot(indices=tf.reshape(tf.cast(model.y_, tf.int32),[-1]), depth=4)

loss = tf.losses.softmax_cross_entropy( onehot_labels=onehot_labels, logits=model.y)
#loss = tf.nn.softmax_cross_entropy_with_logits_v2( labels=onehot_labels, logits=model.y)
train_step = tf.train.AdamOptimizer(start_learning_rate).minimize(loss)

loss_val = tf.losses.softmax_cross_entropy( onehot_labels=onehot_labels, logits=model.y)
#loss_val = tf.nn.softmax_cross_entropy_with_logits_v2( labels=onehot_labels, logits=model.y)
#train_step = tf.train.AdamOptimizer(start_learning_rate).minimize(loss)

###sess.run(tf.initialize_all_variables())
sess.run(tf.global_variables_initializer())




'''
create a summary to monitor cost tensor
'''

###tf.scalar_summary("loss", loss)
tf.summary.scalar("loss", loss)

tf.summary.scalar("loss_val", loss_val)

# merge all summaries into a single op
###merged_summary_op = tf.merge_all_summaries()
merged_summary_op = tf.summary.merge_all()

saver = tf.train.Saver(write_version = tf.train.SaverDef.V2)
#saver.restore(sess, "save/model.ckpt")

# op to write logs to Tensorboard
logs_path = './logs'
summary_writer = tf.summary.FileWriter(logs_path, graph=tf.get_default_graph())

epochs = 13   ###8  ###12  ###20  
batch_size = 100

# train over the dataset about 30 times
for epoch in range(epochs):
  for i in range(int(driving_data.num_images/batch_size)):
    xs, ys = driving_data.LoadTrainBatch(batch_size)
    ###train_step.run(feed_dict={model.x: xs, model.y_: ys, model.keep_prob: 0.8})
    train_step.run(feed_dict={model.x: xs, model.y_: ys, model.keep_prob: 0.7})
    loss_value = loss.eval(feed_dict={model.x: xs, model.y_: ys, model.keep_prob: 1.0})
    #print("Epoch: %d, Step: %d, Loss: %g" % (epoch, epoch * batch_size + i, loss_value))
    print("Epoch: %d, Step: %d, Loss: %g" % (epoch, i, loss_value))


    if i % 10 == 0:
      xs_val, ys_val = driving_data.LoadValBatch(batch_size)
      ###xs, ys = driving_data.LoadTrainBatch(batch_size)
      loss_val = loss.eval(feed_dict={model.x:xs_val, model.y_: ys_val, model.keep_prob: 1.0})
      print("Epoch: %d, Step: %d, Loss_val: %g" % (epoch, i, loss_val))


    # write logs at every iteration
    summary = merged_summary_op.eval(feed_dict={model.x:xs, model.y_: ys, model.keep_prob: 1.0})
    summary_writer.add_summary(summary, epoch * driving_data.num_images/batch_size + i)

    if i % batch_size == 0:
      if not os.path.exists(LOGDIR):
        os.makedirs(LOGDIR)
      checkpoint_path = os.path.join(LOGDIR, "model.ckpt")
      filename = saver.save(sess, checkpoint_path)
      print("Model saved in file: %s" % filename)


correct_prediction = tf.equal(tf.argmax(onehot_labels, 1), tf.argmax(model.y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print('Train Accuracy:', sess.run(accuracy, feed_dict={model.x: xs, model.y_: ys, model.keep_prob: 1.0}))
print('Validation Accuracy:', sess.run(accuracy, feed_dict={model.x: xs_val, model.y_: ys_val, model.keep_prob: 1.0}))

end = time.strftime('%Y-%m-%d_%H-%M-%S')
print('begin: ', begin)
print('end: ', end)

print("Run the command line:\n" \
          "--> tensorboard --logdir=./logs --port=6006" \
          "\nThen open http://0.0.0.0:6006/ into your web browser")

#os.system("sudo -s shutdown -h now")
