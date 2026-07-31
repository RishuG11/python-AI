import tensorflow as tf

model = tf.keras.models.load_model(r"C:\Users\gauta\OneDrive\Desktop\python AI\projects\myaigame\keras_model.h5", compile=False)

print("Model loaded successfully!")