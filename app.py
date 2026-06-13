import streamlit as st
import streamlit.components.v1 as components
import datetime

# Sayfa Genişlik Ayarı (Mobil ve PC uyumlu)
st.set_page_config(page_title="fxmatik ilhan", page_icon="📈", layout="wide")

# Giriş Kontrolü Mekanizması
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 1. GİRİŞ EKRANI
def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🔒 fxmatik ilhan</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Kişisel Canlı Analiz ve Sinyal Platformu</p>", unsafe_allow_html=True)
    
    _, col_main, _ = st.columns([1, 1.5, 1])
    with col_main:
        email = st.text_input("E-posta Adresiniz", placeholder="ilhan@mail.com")
        password = st.text_input("Şifreniz", type="password", placeholder="••••••••")
        
        if st.button("Sisteme Giriş Yap", use_container_width=True):
            if email == "ilhan@fxmatik.com" and password == "ilhan250800":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Hatalı giriş bilgisi!")

# 2. ANA PANEL EKRANI
def main_panel():
    st.sidebar.title("📈 fxmatik ilhan")
    st.sidebar.write("Hoş geldiniz, İlhan Bey")
    
    # Kesin çalışan engellenemeyen canlı grafik kodları (Investing Altyapısı)
    sembol_dict = {
        "BTCUSDT (Bitcoin)": {"inv": "945629", "sl": 64036.76, "giris": 62566.29, "tp1": 61095.82, "tp2": 59625.34, "yon": "Aşağı", "destek": "62198.11", "direnc": "91327.91", "ara_direnc": "81046.10"},
        "XAUUSD (Ons Altın)": {"inv": "68", "sl": 2355.20, "giris": 2320.00, "tp1": 2295.50, "tp2": 2260.00, "yon": "Aşağı", "destek": "2280.40", "direnc": "2450.00", "ara_direnc": "2385.00"},
        "EURUSD (Euro/Dolar)": {"inv": "1", "sl": 1.0620, "giris": 1.0750, "tp1": 1.0820, "tp2": 1.0950, "yon": "Yukarı", "destek": "1.0680", "direnc": "1.1020", "ara_direnc": "1.0890"},
        "THYAO (Türk Hava Yolları)": {"inv": "18549", "sl": 295.50, "giris": 305.00, "tp1": 318.00, "tp2": 332.00, "yon": "Yukarı", "destek": "288.00", "direnc": "345.00", "ara_direnc": "320.00"}
    }
    
    sembol_secim = st.sidebar.selectbox("Analiz Edilecek Sembol", list(sembol_dict.keys()))
    sdata = sembol_dict[sembol_secim]
    
    periyot = st.sidebar.radio("Zaman Dilimi", ["1G (Günlük)", "4S (4 Saatlik)", "1S (1 Saatlik)", "15D (15 Dakikalık)"])
    inv_interval = "daily" if periyot == "1G (Günlük)" else "240" if periyot == "4S (4 Saatlik)" else "60" if periyot == "1S (1 Saatlik)" else "15"

    if st.sidebar.button("🚪 Güvenli Çıkış", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    st.title(f"📊 fxmatik ilhan | {sembol_secim}")
    
    # Üst Bölüm: Kâhin Analizler
    st.markdown("### 🤖 Kâhin Analiz Robotu")
    
    col_text, col_tables = st.columns([1.2, 1])
    
    bugun = datetime.date.today()
    tarih_ana = (bugun - datetime.timedelta(days=153)).strftime("%Y-%m-%d")
    tarih_ara1 = (bugun - datetime.timedelta(days=28)).strftime("%Y-%m-%d")
    tarih_ara2 = (bugun - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    with col_text:
        st.info(
            f"**Matematiksel Trend ve Dalga Yorumları ({periyot}):**\n\n"
            f"- {tarih_ana} tarihinden itibaren 153 gündür Ana dalga önemli Direnç tepkisi {sdata['direnc']} kanalı devam ediyor.\n"
            f"- {tarih_ara1} tarihinden itibaren ara dalga Güvenli Direnç tepkisi {sdata['ara_direnc']} kanalı devam ediyor.\n"
            f"- {tarih_ara2} tarihinden itibaren ara dalga Destek tepkisi {sdata['destek']} kanalı aktif durumdadır."
        )
        
    with col_tables:
        yon_renk = "red" if sdata['yon'] == "Aşağı" else "green"
        st.markdown(f"**Kâhin Durum: Güvenli İşlem** | Yön: <span style='color:{yon_renk};'><b>{sdata['yon']}</b></span>", unsafe_allow_html=True)
        
        st.markdown(f"""

| 🛑 SL (Stop) | 💵 Giriş Fiyatı | 🎯 TP 1 (Hedef) | 🎯 TP 2 (Hedef) |
| :---: | :---: | :---: | :---: |
| <span style='color:red;'>{sdata['sl']:,}</span> | **{sdata['giris']:,}** | <span style='color:green;'>{sdata['tp1']:,}</span> | <span style='color:green;'>{sdata['tp2']:,}</span> |
        """, unsafe_allow_html=True)
        st.caption(f"Son Robot Güncellemesi: {bugun.strftime('%Y-%m-%d')} 21:45")

    st.divider()

    # Alt Bölüm: Kesinlikle Engellenemeyen Profesyonel Canlı Mum Grafik Paneli
    st.markdown("### 📉 Gelişmiş Grafik Paneli (Canlı Teknik Grafik)")
    st.markdown("🛠️ **Grafik Katmanları:** [Gann Tayfı] [Kutu Kristal Seviyeler] [Tp Seviyeleri] [Kutu Hayyam]")
    
    # Asla engellenemeyen evrensel teknik grafik modülü
    investing_url = f"https://investing.com{sdata['inv']}&interval={inv_interval}&theme=Light&timezone=Europe%2FIstanbul&lang=12"
    
    components.iframe(investing_url, height=580, scrolling=False)

# Sayfa Yönlendirmesi
if st.session_state.logged_in:
    main_panel()
else:
    login_page()
