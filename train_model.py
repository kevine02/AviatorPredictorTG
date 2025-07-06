import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

data = pd.read_csv("data.csv")
scaler = MinMaxScaler()
scaled = scaler.fit_transform(data[["multiplier"]])

X, y = [], []
for i in range(5, len(scaled)):
    X.append(scaled[i-5:i])
    y.append(1 if scaled[i][0] > scaler.transform([[5]])[0][0] else 0)
X, y = np.array(X), np.array(y)

model = Sequential()
model.add(LSTM(50, input_shape=(5, 1)))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, y, epochs=20, batch_size=16)

model.save("model.h5")
joblib.dump(scaler, "scaler.save")
