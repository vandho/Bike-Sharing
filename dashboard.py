import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style="dark")


def create_registered_df(df):
    registered_df = df.groupby(by="weekday").agg({
        "registered": "sum"
    })
    
    return registered_df

def create_casual_df(df):
    casual_df = df.groupby(by="weekday").agg({
        "casual": "sum"
    })

    return casual_df

def create_day_cuaca_registered_df(df):
    day_cuaca_registered_df = df.groupby(by=["weekday", "weathersit", "workingday"]).agg({
        "registered": "sum"
    })

    return day_cuaca_registered_df

def create_day_cuaca_casual_df(df):
    day_cuaca_casual_df = df.groupby(by=["weekday", "weathersit", "workingday"]).agg({
        "casual": "sum"
    })
    
    return day_cuaca_casual_df

main_df = pd.read_csv("data\day.csv")

with st.sidebar:
    st.image("bicycle.png")


registered_df = create_registered_df(main_df)
casual_df = create_casual_df(main_df)
day_cuaca_registered_df = create_day_cuaca_registered_df(main_df)
day_cuaca_casual_df =  create_day_cuaca_casual_df(main_df)

st.title("Bike Sharing Dasboard")

st.header("Hari - hari dalam seminggu")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

sns.barplot(
    y="registered",
    x="weekday",
    data=registered_df,
    palette=["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4", "#D3D3D3"],
    ax=ax[0]
)

ax[0].set_ylabel("Pengguna")
ax[0].set_xlabel("Hari")
ax[0].set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "sabtu"])
ax[0].set_title("Registered", loc="center", fontsize=15)

sns.barplot(
    y="casual",
    x="weekday",
    data=casual_df,
    palette=["#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#72BCD4"],
    ax=ax[1]
)

ax[1].set_ylabel("Pengguna")
ax[1].set_xlabel("Hari")
ax[1].set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "sabtu"])
ax[1].set_title("Casual", loc="center", fontsize=15)

st.pyplot(fig)
st.markdown('''Pada pertanyaan pertama explorasi data diambil sampel pengguna biasa dan pengguna member, dari eksplorasi data yang telah dilakukan pengguna biasa 
            memakai layanan terbanyak pada hari Sabtu dan hari Minggu menduduki nomor 
            dua terbanyak, dapat disimpulkan bahwa pengguna biasa menggunakan layanan untuk kebutuhan 
            rekreasi dan hiburan. Pengguna member cenderung stabil menggunakan layanan pada 
            hari kerja namun pengguna paling banyak pada hari kamis, dapat kita ambil bahwa pengguna member 
            menggunakan layanan untuk meningkatkan efisiensi dalam mobilitas kerja, entah itu menuju kantor, 
            menuju tempat meeting terdekat, dan menuju setasiun ketika pulang kerja.
            Pada hari kerja kita bisa menempatkan unit - unit sepeda pada area kantor, layanan transportasi,
            dan pusat kegiatan masyarakat agar para pengguna member dapat mengakses layanan sepeda dengan mudah.
            Pada hari libur dapat ditempatkan pada tempat rekreasi agar pengguna umum dapat menggunakan layanan
            karena kecenderungan dari pengguna umum menggunakan pelayanan pada hari libur atau akhir pekan.
            ''')

st.header("Pengaruh cuaca")

st.subheader("Regiter User")
cr = sns.catplot(
    data=day_cuaca_registered_df,
    kind="bar",
    x="weekday",
    y="registered",
    col="workingday",
    hue="weathersit"
)
cr.set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu"])
cr.set_xlabels("Weekday")
cr.set_ylabels(None)
cr.set_titles("Registered User")
plt.show()
st.pyplot(cr)

st.subheader("Casual User")
cs = sns.catplot(
    data=day_cuaca_casual_df,
    kind="bar",
    x="weekday",
    y="casual",
    col="workingday",
    hue="weathersit"
)
cs.set_xticklabels(["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu"])
cs.set_xlabels("Weekday")
cs.set_ylabels("Casual User")
plt.show()
st.pyplot(cs)

st.markdown('''
        Hasil dari eksplorasi pertanyaan kedua membuktikan bahwa ada 3 jenis 
        sampel cuaca 1) Clear, Few clouds, Partly cloudy, Partly cloudy, 2) Mist + Cloudy, Mist + Broken clouds, Mist + 
        Few clouds, Mist, 3) Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds. 
        terdaftar memiliki kecenderungan menggunakan layanan sepeda pada hari - hari kerja, 
        namun ketika cuaca berkabut tidak banyak menggunakan layanan dan pengguna paling sedikit 
        ketika cuaca sedang tidak bagus seperti hujan ringan, badai, dan turun salju. Untuk pengguna 
        biasa banyak menggunakan pelayanan pada akhir pekan, cuaca cerah berawan menempati urutan yang tertinggi, 
        cuaca berkabut dan badai tidak banyak pengguna biasa yang menggunakan pelayanan, ini dikarenakan mereka 
        akan menunggu cuaca untuk bagus dulu. Hal ini dapat ditarik kesimpulan bahwa cuaca dapat mempengaruhi 
        para pengguna dalam menggunakan layanan sepeda, sehingga ketika cuaca sedang tidak bersahabat maka pengguna 
        cenderung memilih untuk jalan kaki atau menggunakan transportasi umum.
''')