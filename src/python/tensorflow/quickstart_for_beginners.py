import tensorflow as tf 

from tensorflow.keras import (
  layers, losses, activations, optimizers, metrics)
from tensorflow.keras.models import Sequential 
import numpy as np 

mnist = tf.keras.datasets.mnist 

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train/255, x_test/255 

model = Sequential([
  layers.Flatten(input_shape=(28, 28)),
  layers.Dense(128, activation=activations.relu),
  layers.Dropout(0.2), 
  layers.Dense(10),
])

import numpy as np

predictions = model(x_train[:1]).numpy()
print(predictions)

print(tf.nn.softmax(predictions).numpy())

losses.BinaryCrossentropy(from_logits=False)

model.compile(
  optimizer=optimizers.Adam(learning_rate=0.001),
  loss=losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=[metrics.SparseCategoricalAccuracy()])


model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test, verbose=2)


probability_model = Sequential([
  model, 
  layers.Softmax(),
])


pred = model.predict(x_test)
print(pred)
print(pred.argmax(axis=1))


