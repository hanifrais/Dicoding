# Deskripsi
Proyek ini bertujuan untuk menganalisis data dari E-Commerce Public Dataset. Tujuan utama dari proyek ini adalah untuk mengekstrak wawasan dan informasi yang dapat digunakan dari data yang dianalisis.

# Struktur Direktori
- `/data`: Direktori ini berisi data yang digunakan dalam proyek, dalam format .csv.
- `/dashboard`: Direktori ini berisi file `app.py.py` yang digunakan untuk membangun dashboard hasil analisis data.
- `Proyek_Analisis_Data (2).ipynb`: File Jupyter Notebook ini digunakan untuk melakukan analisis data.

# Instalasi
Setelah mengunduh file `Dicoding_Python`, pastikan Anda memiliki lingkungan Python yang sesuai dan pustaka yang diperlukan. Anda dapat menginstal pustaka-pustaka yang diperlukan dengan menjalankan perintah berikut:

```
pip install streamlit
pip install -r dashboard/requirements.txt
```

# Setup Environment
### 1.Buka terminal atau command prompt.

### 2.Arahkan ke direktori proyek (pastikan kamu sudah berada di dalam folder tempat proyek atau file Python kamu berada). Misalnya, untuk masuk ke direktori tertentu, gunakan perintah:

```
cd path/to/your/project/directory
```
### 3.Buat environment virtual (opsional, jika kamu ingin menggunakan environment terisolasi):

```
python -m venv env
```

Setelah itu, aktifkan environment virtual:

- Untuk Windows:
```
.\env\Scripts\activate
```
- Untuk macOS/Linux:
```
source env/bin/activate
```
### 4.Install paket yang dibutuhkan dengan menggunakan pip:
```
pip install pandas matplotlib seaborn streamlit
```
### 5.Verifikasi instalasi dengan menjalankan perintah untuk memeriksa apakah pustaka sudah terpasang dengan benar:
```
pip show pandas matplotlib seaborn streamlit
```


# Menjalankan Streamlit App
Untuk menjalankan dashboard, gunakan perintah berikut:
```bash
cd dicoding/dashboard/
streamlit run app.py.py
```
