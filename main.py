import pickle
import numpy as np

# Load model dan scaler
model = pickle.load(open('diabetes_model.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

# Data pasien
input_data = (6, 148, 72, 35, 0, 33.6, 0.627, 50)

# Ubah ke numpy array
input_array = np.asarray(input_data)

# Reshape
input_reshape = input_array.reshape(1, -1)

# Standardisasi
std_data = scaler.transform(input_reshape)

# Prediksi
prediction = model.predict(std_data)

print("Hasil Prediksi :", prediction[0])

if prediction[0] == 0:
    print("Pasien tidak terkena diabetes")
else:
    print("Pasien terkena diabetes")