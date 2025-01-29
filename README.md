# Deskripsi
Proyek ini bertujuan untuk menganalisis data dari E-Commerce Public Dataset. Tujuan utama dari proyek ini adalah untuk mengekstrak wawasan dan informasi yang dapat digunakan dari data yang dianalisis.

# Struktur Direktori
- `/data`: Direktori ini berisi data yang digunakan dalam proyek, dalam format .csv.
- `/dashboard`: Direktori ini berisi file `app.py.py` yang digunakan untuk membangun dashboard hasil analisis data.
- `Proyek_Analisis_Data (2).ipynb`: File Jupyter Notebook ini digunakan untuk melakukan analisis data.

# Setup Environment
### Clone repository ini ke komputer lokal Anda menggunakan perintah berikut:
```
git clone https://github.com/hanifraisss/Dicoding.git
```
### Buka terminal atau command prompt.

### Arahkan ke direktori proyek (pastikan kamu sudah berada di dalam folder tempat proyek atau file Python kamu berada). Misalnya, untuk masuk ke direktori tertentu, gunakan perintah:

```
cd path/to/your/project/directory
```
### Buat environment virtual (opsional, jika kamu ingin menggunakan environment terisolasi):

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
### Install paket yang dibutuhkan dengan menggunakan pip:
```
pip install pandas matplotlib seaborn streamlit
```
### Verifikasi instalasi dengan menjalankan perintah untuk memeriksa apakah pustaka sudah terpasang dengan benar:
```
pip show pandas matplotlib seaborn streamlit
```


# Menjalankan Streamlit App
#### Pastikan lokasi data file yang telah kamu clone sudah sesuai 
#### Jika belum sesuai, datanya dapat di sesuaikan dengan lokasi yang anda simpan
#### khususnya untuk load data pada app.py di line 7 yang berisi : file_path = "D:/Data Analyst/Project/Dicoding_Python/Dahboard/all_data.csv". dapat anda ubah sesuai tempat anda menyimpan filenya yang telah anda clone/unduh


Untuk menjalankan dashboard, gunakan perintah berikut:
```bash
cd dashboard
streamlit run app.py
```
