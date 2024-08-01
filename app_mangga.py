import streamlit as st
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image as keras_image
from PIL import Image


# Load your trained model
model_path = 'mangga_model.h5' # Path to your saved model
model = load_model(model_path)

# Tentukan ukuran gambar dan nama kelas
IMAGE_WIDTH, IMAGE_HEIGHT = 224, 224
class_names = open("labels_mangga.txt", "r").readlines()
# Fungsi untuk memprediksi gambar
def predict(image, model):
    image = image.resize((IMAGE_WIDTH, IMAGE_HEIGHT))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction, axis=1)[0]
    confidence = np.max(prediction) * 100
    return predicted_class, confidence
# Streamlit UI
st.set_page_config(page_title="Deteksi Penyakit Mangga", page_icon="🍃", layout="wide")

# CSS to style the text appearance
st.markdown("""
  <style>
  .centered {
    text-align: center;
    color: #000000;
    font-weight: bold;
    font-family: 'Arial', sans-serif;
    font-size: 36px;
    margin-bottom: 30px;
  }
  .main {
    background-color: #f0f0f0;
  }
  .stText, .stHeader, .stSubheader, .stMarkdown {
    color: #000000;
    font-family: 'Arial', sans-serif;
    font-size: 18px;
    line-height: 1.6;
  }
  .stButton>button {
    background-color: #007a87;
    color: #ffffff;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
  }
  .stButton>button:hover {
    background-color: #00565e;
  }
  .stSidebar .css-1d391kg, .stSidebar .css-1e5imcs, .stSidebar .css-hxt7ib {
    background-color: #ffffff;
    color: #000000;
  }
  .stSidebar .stText, .stSidebar .stHeader, .stSidebar .stSubheader, .stSidebar .stMarkdown {
    color: #000000;
    font-size: 16px;
    line-height: 1.6;
  }
  .stSidebar .stButton>button {
    background-color: #007a87;
    color: #ffffff;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
  }
  .stSidebar .stButton>button:hover {
    background-color: #00565e;
  }
  h2, h3 {
    color: #000000 !important;
    text-align: center;
    font-size: 28px;
    margin-top: 30px;
    margin-bottom: 20px;
  }
  </style>
  """, unsafe_allow_html=True)

# Sidebar navigation
selected_menu = st.sidebar.selectbox("Navigasi Menu", ["Home", "Prediksi", "Tentang Aplikasi", "About Me"])

if selected_menu == "Home":
  st.markdown('<div class="logo" style="text-align:center;"><img src="C:\\Users\\User\\app_mangga\\image\\logo_unindra.png" style="width: 200px;"></div>', unsafe_allow_html=True)
  st.markdown('<h1 class="centered">🍃 Deteksi Penyakit pada Buah Mangga Menggunakan Pengolahan Citra Dengan Metode OpenCV 🍃</h1>', unsafe_allow_html=True)

  st.write("""
  Aplikasi ini menggunakan model pembelajaran mesin untuk mendeteksi berbagai jenis penyakit pada buah mangga dari gambar yang diunggah atau dari webcam secara real-time. 
  Pilih kategori penyakit di bawah ini untuk melihat detailnya:
  """)

  # Gambar terkait kategori penyakit mangga
  st.markdown('<h2>Kategori Penyakit Mangga</h2>', unsafe_allow_html=True)

  col1, col2, col3, col4, col5 = st.columns(5)

  with col1:
    st.markdown('### Alternaria')
    st.image('c:\\Users\\User\\app_mangga\\image\\alternaria_047.jpg', use_column_width=True)
    st.markdown('Penyakit Alternaria disebabkan oleh jamur Alternaria alternata, menimbulkan bercak coklat kehitaman pada buah, daun, dan batang mangga. Bercak-bercak ini sering berbentuk bulat atau oval dan dapat berkembang menjadi lesi yang lebih besar, merusak daging buah, dan menyebabkan daun gugur.')

  with col2:
    st.markdown('### Anthracnose')
    st.image('C:\\Users\\User\\app_mangga\\image\\anthracnose_016.jpg', use_column_width=True)
    st.markdown('Penyakit Anthracnose disebabkan oleh jamur Colletotrichum gloeosporioides, menimbulkan bercak hitam kecil yang berkembang menjadi lesi besar dan cekung pada buah. Munculnya jamur hitam pada permukaan buah mangga adalah tanda penyakit ini.')

  with col3:
    st.markdown('### Black Mould Rot')
    st.image('C:\\Users\\User\\app_mangga\\image\\aspergillus_004.jpg', use_column_width=True)
    st.markdown('Black Mould Rot disebabkan oleh jamur Aspergillus niger. Bagian yang terinfeksi menjadi lembek dan busuk, membuat buah tidak layak konsumsi dan berkualitas rendah.')

  with col4:
    st.markdown('### Healthy')
    st.image('C:\\Users\\User\\app_mangga\\image\\healthy_063.jpg', use_column_width=True)
    st.markdown('Buah mangga yang sehat memiliki warna yang cerah, rata-rata, dan tidak rusak. Daging buahnya padat, beraroma manis, dan bebas dari lubang atau kerusakan yang disebabkan oleh hama atau penyakit. Kulitnya halus dan tidak menunjukkan tanda-tanda busuk atau jamur.')

  with col5:
    st.markdown('### Stem and Rot')
    st.image('C:\\Users\\User\\app_mangga\\image\\lasio_001.jpg', use_column_width=True)
    st.markdown('Penyakit Stem and Rot disebabkan oleh jamur seperti Botrytis cinerea atau Alternaria alternata, menyebabkan busuk pada ujung batang buah. Area lunak dan coklat kehitaman di sekitar ujung buah menunjukkan bahwa infeksi dapat menyebar ke dalam buah, menyebabkan daging buah membusuk.')

  st.markdown("""
  <h2>Petunjuk Penggunaan Aplikasi</h2>
  <p style="color: #000000;">
  Pada menu *Home*, Anda dapat membaca deskripsi aplikasi dan melihat kategori penyakit mangga.<br>
  Pada menu *Prediksi*, Anda dapat mengunggah gambar buah mangga untuk melakukan prediksi penyakit.<br>
  Pada menu *Tentang Aplikasi*, Anda dapat mengetahui lebih lanjut tentang aplikasi ini.<br>
  Pada menu *About Me*, Anda dapat melihat informasi tentang pembuat aplikasi.
  </p>
  """, unsafe_allow_html=True)

if selected_menu == "Prediksi":
  st.markdown('<h1 class="centered">Prediksi Penyakit Mangga</h1>', unsafe_allow_html=True)

  uploaded_file = st.file_uploader("Unggah gambar buah mangga", type=["jpg", "png", "jpeg"])
  if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)
        
        predicted_class, confidence = predict(image, model)
        
        class_description = {
    0: "Alternaria: Penyakit ini disebabkan oleh jamur Alternaria yang menyebabkan bercak hitam atau cokelat pada daun, buah, dan ranting.Pencegahan: Menjaga kebersihan kebun, menghindari penyiraman berlebihan pada daun, menggunakan fungisida secara rutin, dan memastikan sirkulasi udara yang baik di sekitar tanaman.",
    1: "Anthracnose: Penyakit ini disebabkan oleh jamur Colletotrichum yang menyebabkan bercak cokelat atau hitam pada daun, ranting, dan buah. Pencegahan: Menghindari kelembaban berlebih di sekitar tanaman, memangkas dan membuang bagian tanaman yang terinfeksi, mengaplikasikan fungisida terutama saat cuaca lembab, dan menjaga jarak tanam yang cukup untuk sirkulasi udara yang baik.",
    2: "Black Mould Rot: Penyakit ini disebabkan oleh jamur Aspergillus niger yang menyebabkan bercak hitam pada buah dan pembusukan. Pencegahan: Menjaga kebersihan kebun dengan membuang buah yang jatuh atau busuk, menghindari kerusakan fisik pada buah, menggunakan fungisida yang sesuai, dan menjaga kelembaban tanah yang tepat.",
    3: "Healthy: Tanaman dalam kondisi sehat tanpa tanda-tanda penyakit. Pencegahan: Menjaga kebersihan dan kesehatan kebun dengan perawatan yang baik, melakukan pemangkasan rutin untuk sirkulasi udara yang baik, memberikan nutrisi yang cukup sesuai kebutuhan tanaman, dan menghindari penyiraman berlebihan serta memastikan drainase yang baik.",
    4: "Stem and Rot: Penyakit ini dapat disebabkan oleh berbagai patogen termasuk jamur seperti Phytophthora yang menyebabkan pembusukan pada batang atau akar. Pencegahan: Menjaga kebersihan kebun dengan membuang bagian tanaman yang terinfeksi, menghindari genangan air dan memastikan drainase yang baik, menggunakan fungisida secara rutin, dan memberikan nutrisi yang cukup untuk meningkatkan ketahanan tanaman."
}

        
        st.markdown(f"<p class='black-text'><strong>Prediksi Kelas:</strong> {class_names[predicted_class]}</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='black-text'><strong>Akurasi:</strong> {confidence:.2f}%</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='black-text'><strong>Deskripsi:</strong> {class_description[predicted_class]}</p>", unsafe_allow_html=True)


if selected_menu == "Tentang Aplikasi":
  st.markdown('<h1 class="centered">Tentang Aplikasi</h1>', unsafe_allow_html=True)
  st.write("""
  Deskripsi Website: Website ini dirancang sebagai bagian dari tugas akhir atau skripsi dengan judul "Deteksi Penyakit Pada Buah Mangga Menggunakan Pengolahan Citra Dengan Metode OpenCV". Website ini memanfaatkan teknologi machine learning untuk mendeteksi penyakit pada buah mangga melalui pengolahan citra. Pengguna dapat melakukan prediksi penyakit baik dengan mengunggah gambar buah mangga atau menggunakan kamera untuk mendapatkan prediksi secara real-time.

  Spesifikasi Teknis:
  - Bahasa Pemrograman: Python
  - Framework: Streamlit untuk antarmuka pengguna (GUI)
  - Model Machine learning: TensorFlow/Keras dengan format model .h5

  Fungsionalitas:
  - Pengguna dapat mengunggah gambar buah mangga untuk mendapatkan prediksi tentang kemungkinan adanya penyakit.
  - Fitur deteksi penyakit juga tersedia menggunakan kamera untuk mendapatkan prediksi secara langsung dari gambar yang diambil.

  Desain dan Tampilan:
  - Desain website dirancang untuk menjadi user-friendly, dengan antarmuka yang intuitif untuk memudahkan pengguna dalam mengakses fungsionalitas deteksi penyakit pada buah mangga.
  - Penggunaan warna dan elemen desain yang mendukung tujuan edukatif dan informatif, sesuai dengan tema penelitian tentang pengolahan citra dan deteksi penyakit.
  """)


if selected_menu == "About Me":
  st.markdown('<h1 class="centered">About Me</h1>', unsafe_allow_html=True)
  st.write("""
  Risky Andryan adalah seorang mahasiswa semester 8 jurusan Teknik Informatika di Universitas Indraprasta PGRI Jakarta. Dia memiliki minat yang mendalam dalam pengembangan perangkat lunak, khususnya dalam bidang pengolahan citra dan machine learning. Sebagai bagian dari penelitian akademisnya, Risky sedang menyelesaikan tugas akhir dengan judul "Pengolahan Citra Pendekteksian Penyakit pada Buah Mangga Menggunakan Metode OpenCV", yang melibatkan pengembangan website interaktif menggunakan Python dan framework Streamlit.

  Selain akademis, Risky juga aktif dalam berbagai proyek pengembangan perangkat lunak dan memiliki keahlian dalam menggunakan TensorFlow/Keras untuk implementasi model machine learning dengan format .h5. Dia memiliki kemampuan untuk mengintegrasikan teknologi machine learning dengan aplikasi praktis seperti deteksi penyakit pada tanaman melalui analisis gambar.

  Risky memiliki dedikasi yang tinggi dalam mengejar pengetahuan baru dan keterampilan teknis untuk memperluas pengaruhnya dalam dunia teknologi. Dia juga memiliki keahlian dalam komunikasi dan kerja sama tim, serta mampu mengatasi tantangan teknis dengan pendekatan yang kreatif dan solutif.
  
  informasi Pribadi:
  - Nama: Risky Andryan
  - Tanggal Lahir: Bekasi, 14 Oktober 2002
  - Alamat: Kranggan Wetan, JL. Sumur Binong Gg. Mushola Nurja'an RT. 004/013
  - Status Pendidikan: Mahasiswa semester 8 Teknik Informatika, Universitas Indraprasta PGRI Jakarta, tahun 2020

  contact person/media sosial:
  - Email: riskyandryan66@gmail.com    
  - WhatsApp: [Risky Andryan](https://wa.me/6289609158801)
  - Instagram: [riskyandrya_](https://www.instagram.com/riskyandrya_)
  - LinkedIn: [Risky Andryan](https://www.linkedin.com/in/riskyandryan)
  - GitHub: [github.com/riskyandryan](https://github.com/riskyandryan)
  
  Terima kasih telah menggunakan aplikasi ini!
  """)

  # Hak Cipta
st.sidebar.write('<p style="color:white;">© 2024 Deteksi Penyakit Mangga</p>', unsafe_allow_html=True)
