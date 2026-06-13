import streamlit as st
import streamlit.components.v1 as components

# Sayfa Genişlik Ayarı (Mobil ve PC uyumlu)
st.set_page_config(page_title="fxmatik ilhan", page_icon="📈", layout="wide")

# Giriş Kontrolü Mekanizması
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 1. GİRİŞ EKRANI
def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>🔒 fxmatik ilhan</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: gray;'>Kişisel Analiz ve Sinyal Platformu</p>", unsafe_allow_html=True)
    
    # Giriş Kutusu Merkezleme
    _, col_main, _ = st.columns([1, 2, 1])
    with col_main:
        email = st.text_input("E-posta Adresiniz", placeholder="ilhan@mail.com")
        password = st.text_input("Şifreniz", type="password", placeholder="••••••••")
        
        if st.button("Sisteme Giriş Yap", use_container_width=True):
            # Sadece sizin kullanacağınız giriş bilgileri
            if email == "ilhan@fxmatik.com" and password == "ilhan123":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Hatalı giriş bilgisi!")

# 2. ANA PANEL EKRANI
def main_panel():
    # Sol Menü (Sidebar)
    st.sidebar.title("📈 fxmatik ilhan")
    st.sidebar.write("Hoş geldiniz, İlhan Bey")
    
    # Sembol Seçimi
    sembol = st.sidebar.selectbox(
        "Analiz Edilecek Sembol",
        ["BTCUSDT", "ETHUSDT", "XAUUSD", "EURUSD", "THYAO"]
    )
    
    # Zaman Dilimi Seçimi (Görsel 3'teki gibi)
    periyot = st.sidebar.radio("Zaman Dilimi", ["1G (Günlük)", "4S (4 Saatlik)", "1S (1 Saatlik)", "15D (15 Dakikalık)"])
    
    if st.sidebar.button("🚪 Güvenli Çıkış", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    # Ana İçerik Alanı
    st.title(f"📊 fxmatik ilhan | {sembol} Analiz Paneli")
    
    # Üst Bölüm: Kâhin Analizler ve Robotik Cümleler (Görsel 2)
    st.markdown("### 🤖 Kâhin Analiz Robotu")
    
    col_text, col_tables = st.columns([1.2, 1])
    
    with col_text:
        st.info(
            f"**Matematiksel Trend ve Dalga Yorumları ({periyot}):**\n\n"
            "- 2026-01-11 tarihinden itibaren 153 gündür Ana dalga önemli Direnç tepkisi 91327.91 kanalı devam ediyor.\n"
            "- 2026-05-15 tarihinden itibaren ara dalga Güvenli Direnç tepkisi 81046.10 kanalı devam ediyor.\n"
            "- 2026-06-12 tarihinden itibaren ara dalga Destek tepkisi 62198.11 kanalı aktif durumdadır."
        )
        
    with col_tables:
        # Görsel 2'deki Sinyal Tablosu Yapısı
        st.markdown("**Kâhin Durum: Güvenli İşlem** | <span style='color:red;'><b>Yön: Aşağı</b></span>", unsafe_allow_html=True)
        
        # Tablo Verisi
        st.markdown("""

| 🛑 SL (Stop) | 💵 Giriş Fiyatı | 🎯 TP 1 (Hedef) | 🎯 TP 2 (Hedef) |
| :---: | :---: | :---: | :---: |
| <span style='color:red;'>64036.76</span> | **62566.29** | <span style='color:green;'>61095.82</span> | <span style='color:green;'>59625.34</span> |
        """, unsafe_allow_html=True)
        
        st.caption("Son Robot Güncellemesi: 2026-06-13 20:11")

    st.divider()

    # Alt Bölüm: TradingView Canchi Grafik Entegrasyonu (Görsel 3 ve 4)
    st.markdown("### 📉 Gelişmiş Grafik Paneli (TradingView & Gann Altyapısı)")
    
    # Butonlar (Görsel 3 üstündeki menüler gibi)
    st.markdown("🛠️ **Grafik Katmanları:** [Gann Tayfı] [Kutu Kristal Seviyeler] [Tp Seviyeleri] [Kutu Hayyam]")
    
    # TradingView Teknik Grafik Widget Kodu (Hem mobilde hem PC'de tam oturur)
    tradingview_widget_code = f"""
    <div class="tradingview-widget-container" style="height:500px;width:100%;">
      <div id="tradingview_chart"></div>
      <script type="text/javascript" src="https://tradingview.com"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "{sembol if 'XAU' not in sembol else 'FX:XAUUSD'}",
        "interval": "D" if "{periyot}" == "1G (Günlük)" else "240",
        "timezone": "Europe/Istanbul",
        "theme": "light",
        "style": "1",
        "locale": "tr",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "hide_side_toolbar": false,
        "allow_symbol_change": true,
        "container_id": "tradingview_chart"
      }});
      </script>
    </div>
    """
    # Grafiği ekrana gömelim
    components.html(tradingview_widget_code, height=520)

# Sayfa Yönlendirmesi
if st.session_state.logged_in:
    main_panel()
else:
    login_page()
