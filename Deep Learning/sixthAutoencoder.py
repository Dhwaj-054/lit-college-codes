import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# Load MNIST
(x_train, _), (x_test, _) = mnist.load_data()

# Normalize
x_train = x_train.astype("float32") / 255
x_test = x_test.astype("float32") / 255

# Flatten images
x_train = x_train.reshape(len(x_train), 784)
x_test = x_test.reshape(len(x_test), 784)



# ---------------- PCA ----------------
pca = PCA(n_components=32)

x_train_pca = pca.fit_transform(x_train)
x_test_pca = pca.transform(x_test)

x_test_pca_reconstructed = pca.inverse_transform(x_test_pca)

pca_mse = mean_squared_error(x_test, x_test_pca_reconstructed)

print("PCA MSE:", pca_mse)

# ---------------- Autoencoder ----------------
input_dim = 784
encoding_dim = 32

input_layer = Input(shape=(input_dim,))

# Encoder
encoded = Dense(encoding_dim, activation='linear')(input_layer)

# Decoder
decoded = Dense(input_dim, activation='linear')(encoded)

autoencoder = Model(input_layer, decoded)

# Slower optimizer
autoencoder.compile(
    optimizer='sgd',
    loss='mse'
)

# Train with fewer epochs
autoencoder.fit(
    x_train,
    x_train,
    epochs=5,
    batch_size=256,
    shuffle=True,
    validation_data=(x_test, x_test),
    verbose=1
)

# Reconstruction
x_test_auto = autoencoder.predict(x_test)

auto_mse = mean_squared_error(x_test, x_test_auto)

print("Autoencoder MSE:", auto_mse)


print("\nFinal Comparison")
print("PCA MSE:", pca_mse)
print("Autoencoder MSE:", auto_mse)
