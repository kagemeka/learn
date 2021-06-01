import tensorflow as tf 
from tensorflow.keras import layers

import numpy as np 

np.random.seed(0)
a = np.random.uniform(low=0, high=100, size=(5, 10, 360, 640, 3))



print(a)
input_layer = layers.InputLayer(
  input_shape=a.shape[2:])

a = input_layer(a)
print(a)
# pad = layers.ZeroPadding2D(padding=2)
# a = pad(a)
# print(a)


conv_lstm = layers.ConvLSTM2D(
  filters=1<<2,
  kernel_size=(3, 3))

# a = conv_lstm(a)
lstm = layers.LSTM(units=1<<6)
# lstm_cell = layers.LSTMCell()

# layers.AlphaDropout
# a = lstm_cell(a)

print(a)


# conv2 = layers.Conv1DTranspose

pool = layers.GlobalAvgPool3D()



a = pool(a)


print(a)

# dense = layers.Dense(1)
# a = dense(a)
# print(a)