import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Path ke data
file_path = "D:/Data Analyst/Project/Dicoding_Python/Dahboard/all_data.csv"

# Load data
all_df = pd.read_csv(file_path)

# Convert timestamp ke datetime
all_df['order_purchase_timestamp_y'] = pd.to_datetime(all_df['order_purchase_timestamp_y'])
all_df['order_purchase_timestamp_x'] = pd.to_datetime(all_df['order_purchase_timestamp_x'])

# Judul dashboard
st.title("E-Commerce Dashboard")

# Sidebar untuk navigasi
with st.sidebar:
    st.header("Navigasi")
    selected_section = st.radio("Pilih Visualisasi", [
        "Perbandingan Jumlah Orders Tahun 2017 dan 2018",
        "RFM Analysis",
        "Jumlah Customer per Negara Bagian dan Kota"
    ])
    selected_year = st.radio("Pilih Tahun", ["All", "2017", "2018"])

# Filter data berdasarkan tahun yang dipilih
if selected_year == "All":
    year_df = all_df
elif selected_year == "2017":
    year_df = all_df[all_df['order_purchase_timestamp_y'].dt.year == 2017]
else:
    year_df = all_df[all_df['order_purchase_timestamp_y'].dt.year == 2018]

if selected_section == "Perbandingan Jumlah Orders Tahun 2017 dan 2018":
    st.header("Perbandingan Jumlah Orders Tahun 2017 dan 2018")

    # Hitung jumlah order per bulan
    monthly_counts = year_df.groupby(year_df['order_purchase_timestamp_y'].dt.month)['order_id'].count()

    # Jika memilih "All", pisahkan berdasarkan tahun
    if selected_year == "All":
        monthly_counts_2017 = all_df[all_df['order_purchase_timestamp_y'].dt.year == 2017].groupby(
            all_df['order_purchase_timestamp_y'].dt.month)['order_id'].count()
        monthly_counts_2018 = all_df[all_df['order_purchase_timestamp_y'].dt.year == 2018].groupby(
            all_df['order_purchase_timestamp_y'].dt.month)['order_id'].count()
        combined_df = pd.DataFrame({'2017': monthly_counts_2017, '2018': monthly_counts_2018})
    else:
        combined_df = pd.DataFrame({selected_year: monthly_counts})

    # Plot visualisasi
    fig, ax = plt.subplots(figsize=(10, 6))
    combined_df.plot(kind='line', ax=ax, marker='o')
    ax.set_title(f"Jumlah Orders Tahun {selected_year}" if selected_year != "All" else "Perbandingan Jumlah Orders Tahun 2017 dan 2018", fontsize=14)
    ax.set_xlabel("Bulan", fontsize=12)
    ax.set_ylabel("Jumlah Orders", fontsize=12)
    ax.legend(title="Tahun")
    st.pyplot(fig)

elif selected_section == "RFM Analysis":
    st.header("RFM Analysis")

    # RFM Analysis berdasarkan data yang sudah difilter
    rfm_df = year_df.groupby(by="customer_id_x", as_index=False).agg({
        "order_purchase_timestamp_x": "max",  # Tanggal order terakhir
        "order_id": "nunique",               # Frekuensi
        "payment_value": "sum"               # Nilai total pembayaran
    })
    rfm_df.columns = ["customer_id_x", "max_order_timestamp", "frequency", "monetary"]
    rfm_df['recency'] = (year_df['order_purchase_timestamp_x'].max() - rfm_df['max_order_timestamp']).dt.days

    # Visualisasi Recency
    st.subheader("Top 5 Pelanggan dengan Recency Tertinggi")
    top_recency = rfm_df.sort_values(by="recency", ascending=True).head(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y="recency", x="customer_id_x", data=top_recency, ax=ax)
    ax.set_title("Top 5 Pelanggan dengan Recency Tertinggi", fontsize=14)
    ax.set_xlabel("Customer ID", fontsize=12)
    ax.set_ylabel("Recency (hari)", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Visualisasi Frequency
    st.subheader("Top 5 Pelanggan dengan Frequency Tertinggi")
    top_frequency = rfm_df.sort_values(by="frequency", ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y="frequency", x="customer_id_x", data=top_frequency, ax=ax)
    ax.set_title("Top 5 Pelanggan dengan Frequency Tertinggi", fontsize=14)
    ax.set_xlabel("Customer ID", fontsize=12)
    ax.set_ylabel("Frequency", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Visualisasi Monetary
    st.subheader("Top 5 Pelanggan dengan Monetary Tertinggi")
    top_monetary = rfm_df.sort_values(by="monetary", ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(y="monetary", x="customer_id_x", data=top_monetary, ax=ax)
    ax.set_title("Top 5 Pelanggan dengan Monetary Tertinggi", fontsize=14)
    ax.set_xlabel("Customer ID", fontsize=12)
    ax.set_ylabel("Monetary", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

elif selected_section == "Jumlah Customer per Negara Bagian dan Kota":
    st.header("Jumlah Customer per Negara Bagian dan Kota")

    # Jumlah customer per negara bagian
    bystate_df = year_df.groupby(by="customer_state").customer_id_x.nunique().reset_index()
    bystate_df.rename(columns={"customer_id_x": "customer_count"}, inplace=True)

    # Plot jumlah customer per negara bagian
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x='customer_state', y='customer_count', data=bystate_df, ax=ax, palette="Blues")
    ax.set_title("Jumlah Customer dari setiap Negara Bagian", fontsize=15)
    ax.set_xlabel("Negara Bagian", fontsize=12)
    ax.set_ylabel("Jumlah Customer", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Jumlah customer per kota (top 10 kota dengan jumlah customer terbanyak)
    bycity_df = year_df.groupby("customer_city").customer_id_x.nunique().reset_index()
    bycity_df.rename(columns={"customer_id_x": "customer_count"}, inplace=True)
    top_cities = bycity_df.sort_values(by="customer_count", ascending=False).head(10)

    # Plot jumlah customer per kota
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(x="customer_city", y="customer_count", data=top_cities, ax=ax, palette="Greens")
    ax.set_title("Jumlah Customer dari Setiap Kota (Top 10)", fontsize=15)
    ax.set_xlabel("Kota", fontsize=12)
    ax.set_ylabel("Jumlah Customer", fontsize=12)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)
