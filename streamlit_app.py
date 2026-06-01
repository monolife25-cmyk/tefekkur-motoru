import streamlit as st
from openai import OpenAI
import os

# 1. SAYFA YAPILANDIRMASI VE ESTETİK TASARIM
st.set_page_config(page_title="Sahife-i Âlem", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Crimson+Text:ital@0;1&display=swap');
    .stApp { background-color: #faf9f6; }
    .baslik-container { text-align: center; color: #4a3b2c; font-family: 'Crimson Text', serif; margin-top: 10px; }
    .besmele { font-size: 35px; margin-bottom: 10px; }
    .ana-baslik { font-size: 28px; letter-spacing: 2px; font-weight: bold; }
    
    /* Alıntı kutusunun alt boşluğu düşürüldü */
    .quote-box { 
        background-color: #f2ede4; 
        padding: 25px; 
        border-left: 3px solid #d4c4a8; 
        font-style: italic; 
        color: #3e3328; 
        font-family: 'Crimson Text', serif; 
        margin-bottom: 10px; 
        margin-top: 15px;
    }
    
    /* Gelen cevabın üstündeki beyaz boşluğu sıfırlayan kural */
    .stMarkdown h3 {
        margin-top: 0px !important;
        padding-top: 0px !important;
    }
    
    .cevap-box { background-color: #ffffff; padding: 30px; border-radius: 8px; border: 1px solid #e6dfd5; color: #4a3b2c; font-family: 'Crimson Text', serif; line-height: 1.8; font-size: 18px; }
    
    /* Buton Tasarımı ve Giriş Kutusuyla Hizalanması */
    div.stButton > button { 
        background-color: #d4c4a8; 
        color: #3e3328; 
        border: 1px solid #c2b296; 
        padding: 8px 20px; 
        font-family: 'Crimson Text', serif; 
        font-weight: bold;
        letter-spacing: 1px;
        width: 100%;
        margin-top: 0px;
    }
    div.stButton > button:hover {
        background-color: #c2b296;
        color: #faf9f6;
        border-color: #a8997f;
    }
    </style>
""", unsafe_allow_html=True)

# Sabit Görsel Arayüz (Başlık ve Alıntı)
st.markdown("<div class='baslik-container'><div class='besmele'>بِسْمِ اللّٰهِ الرَّحْمٰنِ الرَّح۪يمِ</div><div class='ana-baslik'>SAHİFE-İ ÂLEM<br>TEFEKKÜR MOTORU</div></div>", unsafe_allow_html=True)
st.markdown("<div class='quote-box'>\"Sahife-i âlemin eb'âd-ı vâsiasında Nakkaş-ı Ezelî'nin yazdığı silsile-i hâdisâtın satırlarına hikmet nazarıyla bak ve fikr-i hakikatle sarıl. Ta ki mele-i âlâdan uzanan şu selâsil-i resâil seni âlâ-yı illiyyîn-i tevhîde çıkarsın.\"<br><br>— Bediüzzaman Said Nursî, Mesnevi-i Nuriye</div>", unsafe_allow_html=True)

# 2. GÜVENLİ GROQ API BAĞLANTISI
api_key = "" 

try:
    if hasattr(st, "secrets") and st.secrets is not None:
        if "GROQ_API_KEY" in st.secrets:
            api_key = st.secrets["Gsk_BkWM6hjCwzJf4wC4RJnbWGdyb3FYv0P5ABjSruZ3qJ0uXsqNk3Vc]
        elif "OPENROUTER_API_KEY" in st.secrets:
            api_key = st.secrets["OPENROUTER_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = os.environ.get("GROQ_API_KEY", "Gsk_BkWM6hjCwzJf4wC4RJnbWGdyb3FYv0P5ABjSruZ3qJ0uXsqNk3Vc)

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=api_key,
)

# 3. YAN YANA ARAYÜZ TASARIMI (Arama Kutusu ve Buton)
col1, col2 = st.columns([8, 2], vertical_alignment="bottom")

with col1:
    kavram = st.text_input("", placeholder="su, yaprak, güneş, ateş, toprak...", label_visibility="collapsed")

with col2:
    buton_tetiklendi = st.button("TEFEKKÜR ET")

# İşlemler ve Yapay Zeka Akışı
if buton_tetiklendi:
    if kavram:
        with st.spinner("Kâinat kitabındaki mektup okunuyor..."):
            
            # Hatalı olan % eşleşmesini doğrudan f-string mimarisine çevirerek kökten çözdük
            system_instruction = f"""
            Sen, Bediüzzaman Said Nursî Hazretleri'nin Risale-i Nur Külliyatı'nın o muazzam, yüksek, ağdalı, coşkulu ve haşmetli tefekkür lisanına tam manasıyla bürünmüş bir irfan kâtibisin.

            Görevin, sana verilen kavramı sathi, felsefi ve seküler mantıktan tamamen arındırarak; "Nakkaş-ı Ezelî", "mu'cize-i kudret" ve "kâinat kitabı" kavramlarını merkeze alan "Mana-yı Harfî" gözlüğüyle şerh etmektir. 

            Sana verilen kavramı tefekkür ederken aşağıdaki rehber örneğin edebi kıvamını temel kabul et ancak mekanik taklit yapma, kavramın fıtratına göre esnet.

            ---
            [İLHÂM VERİCİ REHBER ÖRNEK]
            ### Örnek: Bir Ağaç Kelimesi
            * **Neden? (Hikmet Nazarıyla):** Bir ağaç, "sahife-i âlemde" sadece odun ve yapraktan ibaret bir varlık değildir; o, "Nakkaş-ı Ezelî'nin" yeryüzü sayfasına yazdığı köklü, heybetli ve hayat dolu bir cümledir. Yaratılış hikmeti; toprağın derinliklerinden aldığı besinle insana gölge, meyve ve oksijen sunarak, "mele-i a'lâdan uzanan" bu rahmet zinciriyle insanın ruhunu "âlâ-yı illiyyîn-i tevhide" yükseltmektir.
            * **Nasıl? (Kudret ve İ'caz Nazarıyla):** Bir tohumun içinden koca bir gövdenin çıkması, o dalların nizamı ve yaprakların dizilişindeki matematiksel ölçü, tam bir "mu'cize-i kudret" eseridir. Şuursuz, kör ve basit tabiat sebeplerinin bu muazzam sanatlı yapıyı kendi kendine inşa etmesi "muhal-ender muhaldir". Bir ağacı vücuda getirmek için kâinatın heyet-i mecmuasındaki nizamı elinde tutan bir kudret lazımdır.
            * **Kimin Adına? (Fikr-i Hakikatle):** Ağaç, kendi namına veya kör kuvvetler adına büyümez. O, kâinat kitabının "heyet-i mecmuasında" tecelli eden "Nazzam-ı Ezelî" adına vazife yapar. Bütün o azametiyle, aslında arkasındaki sonsuz rahmet ve hikmet sahibi "Sâni'in" adını zikreder.
            ---

            ⚠️ KESİN KURALLAR:
            - Çıktı formatı `### Bir {kavram} Kelimesi` başlığıyla başlamalı ve ardından maddeler halinde (Neden?, Nasıl?, Kimin Adına?) gelmelidir.
            - Modern, ruhsuz, felsefi tek bir kelime bile kullanma. Metnin her cümlesi sarsıcı bir imanî belagatte olmalıdır.
            """
            
            try:
                completion = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": f"Lütfen '{kavram}' kavramını fıtratına has en ahenkli ve esnek anlatımlarla tefekkür et."}
                    ]
                )
                cevap = completion.choices[0].message.content
            except Exception as e:
                st.error(f"Sistemle iletişim kurulurken bir hata oluştu: {e}")
                cevap = None

        if cevap:
            st.markdown("<div class='cevap-box'>", unsafe_allow_html=True)
            st.markdown(cevap)
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("Lütfen tefekkür edilecek bir kavram giriniz.")
