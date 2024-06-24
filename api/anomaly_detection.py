# anomaly_detection.py
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load dataset
train_data, test_data = ...

# Create TensorFlow model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(2, activation='softmax')
])

# Compile model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(train_data, epochs=10)

# Create scikit-learn model
rf_model = RandomForestClassifier(n_estimators=100)

# Train scikit-learn model
rf_model.fit(train_data)

# Use models for anomaly detection
def detect_anomaly(data):
    tf_pred = model.predict(data)
    rf_pred = rf_model.predict(data)
    # Combine predictions and detect anomalies
    ...
