import streamlit as st
import read_data
from datetime import datetime
import pytz

def callback_function():
    # Logging Message
    print(f"The user has changed to {st.session_state.current_user}")
    # Manuelles wieder ausführen
    #st.rerun()
    
data = read_data.get_person_data()
personlist = (read_data.get_person_list(data))

st.write("# EKG APP")
st.write("## Choose subject")

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
    'Subject',
    options = personlist, key="sbVersuchsperson",on_change = callback_function)
    st.write("Year of Birth: ", str(read_data.find_person_data_by_name(st.session_state.current_user)['date_of_birth']))
    st.write("The user has changed to:", (st.session_state.current_user), "at:", (str(datetime.now(pytz.timezone('Europe/Berlin'))))[:19])


with col2:
    image = read_data.get_picture(st.session_state.current_user)
    # Anzeigen eines Bilds mit Caption
    st.image(image, caption=st.session_state.current_user)