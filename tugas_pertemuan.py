import streamlit as st

# Menyisipkan CSS untuk sidebar dan tombol
st.markdown("""
    <style>
    .sidebar {
        background-color: #407BFF;  
        padding: 10px;             
    }

    .sidebar .stButton > button {
        background-color: #ffffff;  /* Background of buttons */
        color: #407BFF;             /* Text color of buttons */
        border: none;               
        padding: 10px;              /* Adjusted padding for button */
        border-radius: 5px;        
        font-size: 16px;           
        width: 100%;                /* Full width for buttons */
        cursor: pointer;           
    }

    .sidebar .stButton > button:hover {
        background-color: #e0e0e0; 
    }

    .logo {
        font-size: 24px;          
        font-weight: bold;        
        color: #407BFF;           /* Title color */
        text-align: center;       
        margin-bottom: 20px;      
    }

    .content button {
        background-color: #407BFF; /* Button color */
        color: white;               /* Button text color */
        border: none;               /* No border */
        padding: 8px;              /* Padding */
        width: 100%;               /* Full width */
    }
    </style>
""", unsafe_allow_html=True)

# Judul halaman
st.title("Proyek Sederhana dengan Menerapkan While Loop Menggunakan Streamlit")

# Menyimpan halaman yang dipilih dalam session state
if 'page' not in st.session_state:
    st.session_state.page = "home"

# Menampilkan teks logo yang lebih besar
st.sidebar.markdown('<div class="logo"><a href="" style="text-decoration:none;">Pemdasin.aja</a></div>', unsafe_allow_html=True)
# Link untuk navigasi dengan tombol
if st.sidebar.button("PinTech", key="pinTech"):
    st.session_state.page = "pinTech"
if st.sidebar.button("CountAppsTech", key="countappstech"):
    st.session_state.page = "countappstech"

# Menampilkan konten berdasarkan halaman yang dipilih
if st.session_state.page == "home":
    st.markdown("<h2>Selamat Datang di Pemdasin.aja</h2>", unsafe_allow_html=True)
    st.image("coding.png", width=500)

elif st.session_state.page == "pinTech":
    st.markdown("""
            <h3>Program PinTech</h3>
        """, unsafe_allow_html=True)
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.image("pintech.png", width=500)
    st.markdown("</div>", unsafe_allow_html=True)
    

    # Variabel untuk PIN dan percobaan
    pin = 1234
    attempts = st.session_state.get('attempts', 0)
    max_attempts = 3

    # Form input PIN dengan placeholder
    inputPIN = st.text_input("Masukkan PIN", type="password", placeholder="Contoh: 32143")
    
    if st.button("Check Pin Anda!"):
        if inputPIN == "":  # Memeriksa apakah input kosong
            st.error("Silakan masukkan PIN sebelum menekan tombol Check Pin Anda.")
        else:
            if attempts < max_attempts:
                if inputPIN.isdigit() and int(inputPIN) == pin:
                    st.success("PIN benar!")
                    attempts = 0  # Reset attempts if PIN is correct
                else:
                    attempts += 1
                    st.error("PIN salah, silakan coba lagi.")
            else:
                st.error("Anda telah menggunakan semua percobaan. Tidak bisa memasukkan input PIN kembali.")
        
        # Simpan attempts dalam session state
        st.session_state.attempts = attempts  # Save attempts in session state

    st.markdown("</div></div>", unsafe_allow_html=True)

elif st.session_state.page == "countappstech":
    st.markdown("<h2>Program Hitung Banyak Angka Genap dan Angka Ganjil</h2>", unsafe_allow_html=True)
    st.image("math.png", width=500)

    batas = st.number_input("Masukkan batas angka:", min_value=1, value=1)
    # Inisialisasi variabel
    ganjil = 0
    genap = 0
    i = 1  # Inisialisasi counter untuk while loop

    # Loop untuk menghitung angka ganjil dan genap
    while i <= batas:
        if i % 2 == 0:
            genap += 1
        else:
            ganjil += 1
        i += 1 

    # Tampilkan hasil perhitungan
    st.write(f"Banyak angka ganjil: {ganjil}")
    st.write(f"Banyak angka genap: {genap}")
