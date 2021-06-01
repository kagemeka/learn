import numpy as np 
import os 
cfd: str = os.path.dirname(os.path.abspath(__file__))

a = np.arange(12).reshape(2, 2, 3)
print(a)

b = np.arange(1, 19).reshape(2, 3, 3)
print(b)

print(a.dot(b))

import tensorflow as tf 

from tensorflow import keras 
from tensorflow.keras import (
  layers, activations, regularizers, initializers, 
  losses, optimizers, metrics, 
  callbacks)

import IPython 

import kerastuner as kt 

(x_train, y_train), (x_test, y_test) \
  = keras.datasets.fashion_mnist.load_data() 

x_train = x_train.astype('float32') / 255 
x_test = x_test.astype('float32') / 255


def model_builder(hp):
  model = keras.Sequential()
  model.add(layers.Flatten(input_shape=(28, 28)))
  
  hp_units = hp.Int(
    'units', min_value=1<<5, max_value=1<<9, step=1<<5)
  model.add(layers.Dense(
    units=hp_units, activation=activations.relu))
  model.add(layers.Dense(10))

  hp_learning_rate = hp.Choice(
    'learning_rate', values=[1e-2, 1e-3, 1e-4])
  
  model.compile(
    optimizer=optimizers.Adam(learning_rate=hp_learning_rate),
    loss=losses.SparseCategoricalCrossentropy(from_logits=True),
    metrics=['accuracy'])
  
  return model 


tuner = kt.Hyperband(
  model_builder,
  objective='val_accuracy',
  max_epochs=10,
  factor=3,
  directory='keras_tuning',
  project_name='using_kt',
  overwrite=True)

class ClearTrainingOutput(callbacks.Callback):
  def on_train_end(self, *args, **kwargs):
    IPython.display.clear_output(wait=True)


tuner.search(
  x_train, y_train, epochs=10,
  validation_data=(x_test, y_test),
  callbacks=[ClearTrainingOutput()],
)

best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
print(
  f'''
  The hyperparameter search is complete.
  The optimal number of units in the first densely-connected layer is {best_hps.get('units')} and the optimal learning
  rate for the optimizer is {best_hps.get('learning_rate')} .
  '''
)

model = tuner.hypermodel.build(best_hps)
model.fit(
  x_train, y_train, epochs=10, 
  validation_data=(x_test, y_test))


