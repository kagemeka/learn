import os 
import tensorflow as tf 
from tensorflow.keras.models import Sequential, Model 
from tensorflow.keras import (
  layers, activations, regularizers,
  losses, optimizers, metrics, 
  callbacks)


import os 
cfd: str = os.path.dirname(os.path.abspath(__file__))
root = f'{cfd}/..'

print(tf.version.VERSION)

(x_train, y_train), (x_test, y_test) \
  = tf.keras.datasets.mnist.load_data()

y_train = y_train[:1000]
y_test = y_test[:1000]

x_train = x_train[:1000].reshape(-1, 28 * 28) / 255 
x_test = x_test[:1000].reshape(-1, 28 * 28) / 255


def create_model():
  model = Sequential([
    layers.Dense(
      1<<9, activation=activations.relu, 
      input_shape=(28*28, )),
    layers.Dropout(0.2),
    layers.Dense(10),
  ])

  model.compile(
    optimizer=optimizers.Adam(learning_rate=1e-4),
    loss=losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=[metrics.SparseCategoricalAccuracy()])

  return model 

model = create_model() 
model.summary() 


checkpoint_path = f'{root}/training_1/cp.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = callbacks.ModelCheckpoint(
  filepath=checkpoint_path, 
  save_weights_only=True,
  verbose=2)


model.fit(
  x_train, y_train, 
  epochs=10, 
  validation_data=(x_test, y_test),
  callbacks=[cp_callback])


model = create_model() 
loss, acc = model.evaluate(
  x_test, y_test, verbose=2)
print(f'loss: {loss}, accuracy: {acc}')

model.load_weights(checkpoint_path)
loss, acc = model.evaluate(
  x_test, y_test, verbose=2)
print(f'loss: {loss}, accuracy: {acc}')

checkpoint_path = 'training_2/cp-{epoch:04}.ckpt'
checkpoint_dir = os.path.dirname(checkpoint_path)

batch_size = 32 
cp_callback = callbacks.ModelCheckpoint(
  filepath=checkpoint_path, 
  verbose=2, 
  save_weights_only=True,
  save_freq=5*batch_size)

model = create_model() 
model.save_weights(checkpoint_path.format(epoch=0))
model.fit(
  x_train, y_train,
  epochs=100, 
  callbacks=[cp_callback, callbacks.EarlyStopping(patience=5)],
  validation_data=(x_test, y_test),
  verbose=0)


latest_ckpt = tf.train.latest_checkpoint(checkpoint_dir)
print(latest_ckpt)

model = create_model() 

model.load_weights(latest_ckpt)
loss, acc = model.evaluate(
  x_test, y_test, verbose=2)
print(f'loss: {loss}, accuracy: {acc}')


model.save_weights(latest_ckpt)
model = create_model()
model.load_weights(latest_ckpt)
loss, acc = model.evaluate(
  x_test, y_test, verbose=2)
print(f'loss: {loss}, accuracy: {acc}')

model.save('entire_model', save_format='tf')

model = tf.keras.models.load_model('entire_model')
loss, acc = model.evaluate(
  x_test, y_test, verbose=2)
print(f'loss: {loss}, accuracy: {acc}')


