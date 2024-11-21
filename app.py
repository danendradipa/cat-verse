from flask import Flask, render_template, request
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Memuat model
model = tf.keras.models.load_model('model/cat_model.h5')

# Rute untuk halaman utama (index)
@app.route("/")
def index():
    return render_template("index.html")

# Rute untuk halaman klasifikasi
@app.route("/classify", methods=["GET", "POST"])
def classify():
    threshold = 85.0  # Menetapkan threshold kepercayaan
    breed = None
    message = None

    if request.method == "POST":
        # Mengambil file gambar yang diupload
        file = request.files["upload"]
        if file:
            # Membuka file gambar menggunakan PIL
            img = Image.open(file.stream)

            # Mengubah ukuran gambar sesuai input yang diinginkan oleh model
            img = img.resize((224, 224))  # Sesuaikan dengan ukuran input model Anda

            # Mengkonversi gambar ke array dan normalisasi
            img_array = np.array(img) / 255.0  # Normalisasi pixel

            # Tambahkan batch dimension
            img_array = np.expand_dims(img_array, axis=0)

            # Melakukan prediksi dengan model
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction, axis=1)[0]
            confidence_score = np.max(prediction) * 100  # Skor kepercayaan

            # Daftar kelas kucing
            classes = ["Abyssinian", "Bengal", "Bombay", "British Shorthair", "Domestic", "Maine Coon", "Persian", "Ragdoll", "Siamese", "Sphynx"]

            # Mengambil nama kelas berdasarkan prediksi
            breed = classes[predicted_class]

            # Jika skor kepercayaan lebih rendah dari threshold, tampilkan pesan peringatan
            if confidence_score < threshold:
                message = "Foto ini kemungkinan bukan foto kucing, coba foto yang lainnya."
                breed = None
            else:
                message = None  # Menghilangkan pesan jika skor kepercayaan cukup

            # Menampilkan hasil prediksi ke halaman
            return render_template("classify.html", breed=breed, message=message)

    return render_template("classify.html", breed=breed, message=message)

if __name__ == '__main__':
    app.run(debug=True)
