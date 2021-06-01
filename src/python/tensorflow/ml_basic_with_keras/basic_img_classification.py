import tensorflow as tf 
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential 
from tensorflow.keras import (
  layers, losses, optimizers, metrics, activations
)
import numpy as np
import matplotlib.pyplot as plt 
print(tf.__version__)


(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

class_names = [
  'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
  'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure() 
plt.imshow(x_train[0])
plt.colorbar()
plt.grid(False)
plt.show()


x_train, x_test = x_train/255, x_test/255

plt.figure(figsize=(10, 10))
for i in range(25):
  plt.subplot(5, 5, i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(x_train[i], cmap=plt.cm.binary)
  plt.xlabel(class_names[y_train[i]])


model = Sequential([
  layers.Flatten(input_shape=(28, 28)),
  layers.Dense(128, activation=activations.relu),
  layers.Dense(10),
])

model.compile(
  optimizer=optimizers.Adam(learning_rate=0.0005),
  loss=losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['accuracy'],

)

model.fit(x_train, y_train, epochs=10, verbose=2)

test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)

print(test_loss)

probability_model = tf.keras.Sequential([
  model, 
  tf.keras.layers.Softmax()])


predictions = probability_model.predict(x_test)
print(predictions.argmax(axis=1))


def plot_image(i, predictions_array, true_label, img):
  true_label, img = true_label[i], img[i]
  plt.grid(False)
  plt.xticks([]); plt.yticks([])
  plt.imshow(img, cmap=plt.cm.binary)
  predicted_label = np.argmax(predictions_array)
  color = 'blue' if predicted_label == true_label else 'red'
  plt.xlabel(f'{class_names[predicted_label]:2.0f}')





