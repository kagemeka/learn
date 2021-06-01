import os 
os.environ["TFHUB_MODEL_LOAD_FORMAT"] = "COMPRESSED"
import numpy as np 

import tensorflow as tf 
import tensorflow_hub as hub 
import tensorflow_datasets as tfds 

print(tf.__version__)

train_data, validation_data, test_data = tfds.load(
  name='imdb_reviews',
  split=('train[:60%]', 'train[60%:]', 'test'),
  as_supervised=True
)

x_train_batch, y_train_batch = next(iter(train_data.batch(10)))
print(x_train_batch)

embedding = 'https://tfhub.dev/google/nnlm-en-dim50/2'
hub_layer = hub.KerasLayer(
  embedding, input_shape=[], dtype=tf.string, trainable=True)


vec = hub_layer(x_train_batch[:3])
print(vec)


from tensorflow.keras import (
  layers, activations, losses, optimizers, metrics,
)
from tensorflow.keras.models import Sequential 
model = Sequential([
  hub_layer, 
  layers.Dense(units=1<<4, activation=activations.relu),
  layers.Dense(units=1),
])

model.summary()

model.compile(
  loss=losses.BinaryCrossentropy(from_logits=True),
  optimizer=optimizers.Adam(learning_rate=5e-4),
  metrics=metrics.BinaryAccuracy(threshold=0.0),
)

history = model.fit(
  train_data.shuffle(10**4).batch(1<<9),
  epochs=10,
  validation_data=validation_data.batch(1<<9),
  verbose=2,
)


results = model.evaluate(test_data.batch(1<<9), verbose=2)

for metrics, value in zip(model.metrics_names, results):
  print(f'{metrics}: {value}')






