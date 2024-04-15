import streamlit as st
import read_data

data = read_data.get_person_data()
personlist = (read_data.get_person_list(data))

st.write("# EKG APP")
st.write("## Versuchsperson auswählen")

# Session State wird leer angelegt, solange er noch nicht existiert
if 'current_user' not in st.session_state:
    st.session_state.current_user = 'None'

# Anlegen des Session State. Bild, wenn es kein Bild gibt
if 'picture_path' == {}:
    st.session_state.picture_path = 'data/pictures/none.jpg'

col1, col2 = st.columns(2)

with col1:
   # Dieses Mal speichern wir die Auswahl als Session State
    st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = personlist, key="sbVersuchsperson")
    st.write("Geburtsjahr: ", read_data.find_person_data_by_name(st.session_state.current_user)['date_of_birth'])

with col2:
    image = read_data.get_picture(st.session_state.current_user)
    # Anzeigen eines Bilds mit Caption
    st.image(image, caption=st.session_state.current_user)