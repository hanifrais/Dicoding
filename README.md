# Deskripsi
Proyek ini bertujuan untuk menganalisis data dari E-Commerce Public Dataset. Tujuan utama dari proyek ini adalah untuk mengekstrak wawasan dan informasi yang dapat digunakan dari data yang dianalisis.

# Struktur Direktori
- `/data`: Direktori ini berisi data yang digunakan dalam proyek, dalam format .csv.
- `/dashboard`: Direktori ini berisi file `app.py` yang digunakan untuk membangun dashboard hasil analisis data.
- `Proyek_Analisis_Data (1).ipynb`: File Jupyter Notebook ini digunakan untuk melakukan analisis data.

# Instalasi
Setelah mengunduh file `Dicoding_Python`, pastikan Anda memiliki lingkungan Python yang sesuai dan pustaka yang diperlukan. Anda dapat menginstal pustaka-pustaka yang diperlukan dengan menjalankan perintah berikut:

```bash
pip install streamlit
pip install -r dashboard/requirements.txt
```

# Setup Environment
## Menggunakan Anaconda
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Menggunakan Shell/Terminal
```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

# Menjalankan Streamlit App
Untuk menjalankan dashboard, gunakan perintah berikut:
```bash
streamlit run dashboard.py
```
