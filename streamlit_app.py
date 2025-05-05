import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Kalkulator Sederhana", layout="centered")
st.title("Kalkulator Sederhana")

# CSS untuk styling tombol dan tampilan
st.markdown("""
<style>
    /* Style untuk display kalkulator */
    .calculator-display {
        font-size: 2em;
        text-align: right;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: #f9f9f9;
        height: 60px;
    }
    
    /* Style untuk tombol */
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 1.2em;
        border-radius: 5px;
        margin: 2px 0;
    }
    
    /* Warna khusus untuk tombol operasi */
    .operation {
        background-color: #f0ad4e !important;
        color: white !important;
    }
    
    /* Warna khusus untuk tombol clear */
    .clear {
        background-color: #d9534f !important;
        color: white !important;
    }
    
    /* Warna khusus untuk tombol equals */
    .equals {
        background-color: #5cb85c !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Inisialisasi state untuk menyimpan input
if 'calculation' not in st.session_state:
    st.session_state.calculation = ""

# Fungsi untuk menangani klik tombol
def button_click(value):
    if value == "C":
        st.session_state.calculation = ""
    elif value == "=":
        try:
            # Ganti simbol ÷ dengan / dan × dengan * untuk perhitungan
            expression = st.session_state.calculation.replace("÷", "/").replace("×", "*")
            result = eval(expression)
            st.session_state.calculation = str(result)
        except:
            st.session_state.calculation = "Error"
    else:
        st.session_state.calculation += value

# Tampilkan display kalkulator
st.markdown(f'<div class="calculator-display">{st.session_state.calculation or "0"}</div>', unsafe_allow_html=True)

# Buat layout tombol kalkulator
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("7", key="7"):
        button_click("7")
    if st.button("4", key="4"):
        button_click("4")
    if st.button("1", key="1"):
        button_click("1")
    if st.button("C", key="C"):
        button_click("C")

with col2:
    if st.button("8", key="8"):
        button_click("8")
    if st.button("5", key="5"):
        button_click("5")
    if st.button("2", key="2"):
        button_click("2")
    if st.button("0", key="0"):
        button_click("0")

with col3:
    if st.button("9", key="9"):
        button_click("9")
    if st.button("6", key="6"):
        button_click("6")
    if st.button("3", key="3"):
        button_click("3")
    if st.button(".", key="."):
        button_click(".")

with col4:
    if st.button("÷", key="/"):
        button_click("÷")
    if st.button("×", key="*"):
        button_click("×")
    if st.button("-", key="-"):
        button_click("-")
    if st.button("+", key="+"):
        button_click("+")

# Baris tambahan untuk tombol khusus
col5, col6, col7, col8 = st.columns(4)

with col5:
    if st.button("(", key="("):
        button_click("(")
with col6:
    if st.button(")", key=")"):
        button_click(")")
with col7:
    if st.button("^", key="^"):
        button_click("^")
with col8:
    if st.button("=", key="="):
        button_click("=")

# Terapkan CSS class ke tombol-tombol khusus
st.markdown("""
<script>
    // Tambahkan class CSS ke tombol-tombol khusus
    document.addEventListener('DOMContentLoaded', function() {
        const operationButtons = ['/', '*', '-', '+', '^', '(', ')'];
        operationButtons.forEach(op => {
            const btn = document.querySelector(`button[title="${op}"]`);
            if (btn) btn.classList.add('operation');
        });
        
        const clearBtn = document.querySelector('button[title="C"]');
        if (clearBtn) clearBtn.classList.add('clear');
        
        const equalsBtn = document.querySelector('button[title="="]');
        if (equalsBtn) equalsBtn.classList.add('equals');
    });
</script>
""", unsafe_allow_html=True)

# Petunjuk penggunaan
st.markdown("---")
st.markdown("**Petunjuk Penggunaan:**")
st.markdown("- Klik tombol angka dan operator untuk membentuk perhitungan")
st.markdown("- Gunakan **C** untuk menghapus semua")
st.markdown("- Gunakan **^** untuk perpangkatan (contoh: 2^3 = 8)")
st.markdown("- Tekan **=** untuk melihat hasil perhitungan")
