import streamlit as st
import streamlit_book as stb
from  PIL import Image, ImageEnhance
import pandas as pd

#Sidebar con logo Chiesi
c0, c1, c2= st.columns([2,3,2])

with c1:
    logo = Image.open(r'C:\Users\VeronicaCipriani\Desktop\KASANOVA\loader_Chiesi\chiesi_logo.jpg')
    st.sidebar.image(logo,  width=150)

st.sidebar.markdown("### App di caricamento dati")
st.sidebar.markdown("Identificare il dataset di input che si vuole caricare, e procedere con l'upload")



#Titolo e struttura
st.title("Caricamento")


#scelgo il tipo di file per il caricamento
st.subheader("Scelta tipologia di file:")
c2, c3 = st.columns([6, 2])
with c2:
    file_type = st.selectbox(
        "File da caricare", ['Excel', '.csv o file di testo'] , index=0)

    #se il file è di tipo testuale, imposto il reparatore
    if file_type == '.csv o file di testo':
        sep = st.text_input('Separatore:')


#procedo al caricamento del file
st.subheader("Upload:")

c4, c5 = st.columns([6, 2])

with c4:

    uploaded_file = st.file_uploader(
        "",
        key="1",
        help="Per adattare le dimensioni della pagina > Settings > turn on 'wide mode'",
        #accept_multiple_files = True,
    )

    if uploaded_file is not None:
        file_container = st.expander("Check your uploaded file")

        if file_type == 'Excel':
            shows = pd.read_excel(uploaded_file)

        if file_type == '.csv o file di testo':
            shows = pd.read_csv(uploaded_file, sep = sep)


        st.success("Caricamento completato")
        uploaded_file.seek(0)
        file_container.write(shows)
    
    else:
        st.info(
            f"""
                👆 Seleiona qui il file. 
                """
        )

        st.stop()


#qualche esplorazione
n_row = shows.shape[0]
st.write('Numero di record:')
st.write(n_row)

st.write(' ')

st.write('Numero di attributi:')
n_col = shows.shape[1]
st.write(n_col)
