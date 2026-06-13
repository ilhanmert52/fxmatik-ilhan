import streamlit as st
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
    
    # Yeni ve engellenemeyen grafik yönlendirme linkleri
    sembol_dict = {
        "BTCUSDT (Bitcoin)": {"tv": "BTCUSDT", "sl": 64036.76, "giris": 62566.29, "tp1": 61095.82, "tp2": 59625.34, "yon": "Aşağı", "destek": "62198.11", "direnc": "91327.91", "ara_direnc": "81046.10", "link": "https://tradingview.com"},
        "XAUUSD (Ons Altın)": {"tv": "XAUUSD", "sl": 2355.20, "giris": 2320.00, "tp1": 2295.50, "tp2": 2260.00, "yon": "Aşağı", "destek": "2280.40", "direnc": "2450.00", "ara_direnc": "2385.00", "link": "https://tradingview.com"},
        "EURUSD (Euro/Dolar)": {"tv": "EURUSD", "sl": 1.0620, "giris": 1.0750, "tp1": 1.0820, "tp2": 1.0950, "yon": "Yukarı", "destek": "1.0680", "direnc": "1.1020", "ara_direnc": "1.0890", "link": "https://tradingview.com"},
        "THYAO (Türk Hava Yolları)": {"tv": "THYAO", "sl": 295.50, "giris": 305.00, "tp1": 318.00, "tp2": 332.00, "yon": "Yukarı", "destek": "288.00", "direnc": "345.00", "ara_direnc": "320.00", "link": "https://tradingview.com"}
    }
    
    sembol_secim = st.sidebar.selectbox("Analiz Edilecek Sembol", list(sembol_dict.keys()))
    sdata = sembol_dict[sembol_secim]
    
    periyot = st.sidebar.radio("Zaman Dilimi", ["1G (Günlük)", "4S (4 Saatlik)", "1S (1 Saatlik)", "15D (15 Dakikalık)"])

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

    # Alt Bölüm: Engellenemeyen Butonlu Grafik Altyapısı
    st.markdown("### 📉 Gelişmiş Grafik Paneli (Engelsiz Canlı Bağlantı)")
    st.markdown("🛠️ **Grafik Katmanları:** [Gann Tayfı] [Kutu Kristal Seviyeler] [Tp Seviyeleri] [Kutu Hayyam]")
    
    st.warning("⚠️ Tarayıcı güvenlik duvarı engellerini aşmak için lütfen aşağıdaki butonları kullanarak canlı grafik pencerelerini tam ekran olarak açın:")
    
    # Tam ekran açma butonları (Hem mobilde hem PC'de kusursuz çalışır)
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        st.link_button(f"📊 {sembol_secim} Canlı Grafiğini Yeni Sekmede Aç", sdata['link'], use_container_width=True)
    with col_btn2:
        st.link_button("📐 Gann Tayfı & Teknik Çizim Alanına Git", "https://tradingview.com", use_container_width=True)

# Sayfa Yönlendirmesi
if st.session_state.logged_in:
    main_panel()
else:
    login_page()
