from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
import csv
import os

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "allfahri_desain_local_key"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/kirim-pesan", methods=["POST"])
def kirim_pesan():

    nama = request.form.get("nama", "").strip()
    email = request.form.get("email", "").strip()
    layanan = request.form.get("layanan", "").strip()
    pesan = request.form.get("pesan", "").strip()

    if not all([nama, email, layanan, pesan]):
        flash("Semua kolom wajib diisi.", "error")
        return redirect("/#kontak")

    file_baru = not os.path.exists("pesan_masuk.csv")

    with open(
        "pesan_masuk.csv",
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        if file_baru:
            writer.writerow([
                "Waktu",
                "Nama",
                "Email",
                "Layanan",
                "Pesan"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            nama,
            email,
            layanan,
            pesan
        ])

    flash("Pesan berhasil dikirim!", "success")

    return redirect("/#081293045208")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )