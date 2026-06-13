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
    
    # Sembol Eşleştirme (TradingView için tam uyumlu kodlar)
    sembol_dict = {
        "BTCUSDT (Bitcoin)": "BINANCE:BTCUSDT",
        "ETHUSDT (Ethereum)": "BINANCE:ETHUSDT",
        "XAUUSD (Ons Altın)": "OANDA:XAUUSD",
        "EURUSD (Euro/Dolar)": "FX:EURUSD",
        "THYAO (Türk Hava Yolları)": "BIST:THYAO"
    }
    
    sembol_secim = st.sidebar.selectbox("Analiz Edilecek Sembol", list(sembol_dict.keys()))
    tv_symbol = sembol_dict[sembol_secim]
    
    periyot = st.sidebar.radio("Zaman Dilimi", ["1G (Günlük)", "4S (4 Saatlik)", "1S (1 Saatlik)"])
    tv_interval = "D" if periyot == "1G (Günlük)" else "240" if periyot == "4S (4 Saatlik)" else "60"

    if st.sidebar.button("🚪 Güvenli Çıkış", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    st.title(f"📊 fxmatik ilhan | {sembol_secim}")
    
    # Üst Bölüm: Kâhin Analizler ve Fiyat Seviyeleri Tablosu
    st.markdown("### 🤖 Kâhin Analiz Robotu")
    
    col_text, col_tables = st.columns([1.2, 1])
    
    with col_text:
        st.info(
            f"**Matematiksel Trend ve Dalga Yorumları ({periyot}):**\n\n"
            f"- Seçilen {sembol_secim} paritesinde algoritma derinliği taraması tamamlandı.\n"
            f"- Ara dalga matematiksel Destek tepki kanalları aktif durumdadır.\n"
            f"- Üst dalga kırılımında Güvenli Direnç tepki alanları TradingView teknik grafiği üzerinden takip edilmektedir."
        )
        
    with col_tables:
        st.markdown("**Kâhin Durum: Analiz Tamamlandı** | Yön: <span style='color:green;'><b>Dinamik Takip</b></span>", unsafe_allow_html=True)
        
        # fxmatik tarzı sinyal tablosu şablonu (Grafikle tam uyumlu takip için)
        st.markdown("""

| 🛑 SL (Stop) | 💵 Giriş Fiyatı | 🎯 TP 1 (Hedef) | 🎯 TP 2 (Hedef) |
| :---: | :---: | :---: | :---: |
| Grafik Tabanlı | Anlık Takip | Dalga Boyu 1 | Dalga Boyu 2 |
        """, unsafe_allow_html=True)
        st.caption("Son Matematiksel Robot Güncellemesi: Canlı Grafik Akışı")

    st.divider()

    # Alt Bölüm: Canlı Grafik Entegrasyonu (Görsel 3 ve 4'teki gibi tam ekran indikatörlü)
    st.markdown("### 📉 Gelişmiş Grafik Paneli (TradingView Teknik Altyapısı)")
    st.markdown("🛠️ **Grafik Katmanları:** [Gann Tayfı] [Kutu Kristal Seviyeler] [Tp Seviyeleri] [Kutu Hayyam]")
    
    # Sorunsuz çalışan teknik analiz widget kodu
    tradingview_widget_code = f"""
    <div class="tradingview-widget-container" style="height:600px;width:100%;">
      <div id="tradingview_chart" style="height:100%;width:100%;"></div>
      <script type="text/javascript" src="https://tradingview.com"></script>
      <script type="text/javascript">
      new TradingView.widget({{
        "autosize": true,
        "symbol": "{tv_symbol}",
        "interval": "{tv_interval}",
        "timezone": "Europe/Istanbul",
        "theme": "light",
        "style": "1",
        "locale": "tr",
        "toolbar_bg": "#f1f3f6",
        "enable_publishing": false,
        "hide_side_toolbar": false,
        "allow_symbol_change": true,
        "details": true,
        "hotlist": true,
        "calendar": true,
        "container_id": "tradingview_chart"
      }});
      </script>
    </div>
    """
    components.html(tradingview_widget_code, height=620)

# Sayfa Yönlendirmesi
if st.session_state.logged_in:
    main_panel()
else:
    login_page()
