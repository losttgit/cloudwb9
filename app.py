from flask import Flask, render_template

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Routing untuk halaman utama
@app.route('/')
def index():
    # Data biodata untuk 4 anggota
    anggota_list = [
        {
            "nama": "AbdullaH Azzam Azed Vanhoutten",
            "nim": "22.83.0933",
            "education": "Universitas XYZ - Teknik Agama",
            "tentang": "Saya ingin jadi kapal laut.",
            "foto": "profile1.jpg"
        },
        {
            "nama": "Elizabeth Nagita P.S.H. Zachawerus",
            "nim": "22.83.0931",
            "education": "Universitas XYZ - Sistem Geoglogi",
            "tentang": "Fokus saya adalah menjadi hengker.",
            "foto": "profile2.jpg"
        },
        {
            "nama": "Muh. Faqih Muttaqin Playboy",
            "nim": "22.83.0910",
            "education": "Universitas XYZ - Ilmu Pertanian",
            "tentang": "Saya suka mengerjakan proyek IoT.",
            "foto": "profile3.jpg"
        },
        {
            "nama": "Rafli Ilham Prasetyo",
            "nim": "22.83.0907",
            "education": "Universitas XYZ - Teknik Kedokteran",
            "tentang": "Saya befokus untuk terus berfokus agar fokus.",
            "foto": "profile4.jpg"
        }
    ]
    # Render template HTML dengan data
    return render_template('index.html', anggota_list=anggota_list)


@app.route('/rafli')
def rafli():
    return render_template('rafli.html')

@app.route('/nagita')
def nagita():
    return render_template('nagita.html')

@app.route('/azzam')
def azzam():
    return render_template('azzam.html')

@app.route('/faqih')
def faqih():
    return render_template('faqih.html')

@app.route('/faqihprofile')
def faqihprofile():
    return render_template('faqih-profile.html')

@app.route('/azzamprofile')
def azzamprofile():
    return render_template('azzam-profile.html')

@app.route('/nagitaprofile')
def nagitaprofile():
    return render_template('nagita-profile.html')

@app.route('/rafliprofile')
def rafliprofile():
    return render_template('rafli-profile.html')

# Jalankan server Flask
if __name__ == '__main__':
    app.run(debug=True)
