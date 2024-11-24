from flask import Flask, render_template, request
import tensorflow as tf
from PIL import Image
import numpy as np
import io
import base64
from detail_ras import detailRas

app = Flask(__name__)

# Memuat model
model = tf.keras.models.load_model('model/cat_model.h5')

# Daftar kelas kucing
classes = ["Abyssinian", "Bengal", "Bombay", "British Shorthair", "Domestic",
           "Maine Coon", "Persian", "Ragdoll", "Siamese", "Sphynx"]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/classify", methods=["GET", "POST"])
def classify():
    threshold = 85.0
    breed = None
    message = None
    img_base64 = None

    if request.method == "POST":
        file = request.files.get("upload")  # Ambil file yang diunggah
        if not file:
            return render_template("classify.html", message="Silakan unggah file gambar.")

        try:
            # Proses gambar
            img = Image.open(file.stream)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            img = img.resize((224, 224))  # Sesuaikan ukuran input model
            img_array = np.array(img) / 255.0  # Normalisasi
            img_array = np.expand_dims(img_array, axis=0)  # Tambahkan batch dimension

            # Konversi gambar ke Base64
            img_io = io.BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)
            img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')

            # Prediksi
            prediction = model.predict(img_array)
            predicted_class = np.argmax(prediction, axis=1)[0]
            confidence_score = np.max(prediction) * 100

            # Ambil nama kelas
            breed = classes[predicted_class]

            if confidence_score < threshold:
                message = "Foto ini kemungkinan bukan foto kucing, coba foto yang lainnya."
                breed = None
            else:
                message = None

        except Exception as e:
            message = f"Terjadi kesalahan saat memproses gambar: {e}"
            breed = None

    # Kirim data ke template
    return render_template(
        "classify.html",
        breed=breed,
        message=message,
        img=img_base64,
        char=detailRas.get(breed, {})
    )


if __name__ == '__main__':
    app.run(debug=True)
