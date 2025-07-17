import streamlit as st
import pandas as pd
from datetime import datetime
import qrcode
from io import BytesIO
import base64

# Configuración de la página
st.set_page_config(page_title="Registro de Asistencia", page_icon="📝")

# URL pública de la app (ponla cuando esté desplegada)
app_url = "https://movies-dataset-q8gsks5ohe.streamlit.app/"  # CAMBIA ESTO después de hacer el deploy

# Título y formulario
st.title("📝 Registro de Asistencia")
st.write("Introduce tu nombre y correo para registrar tu asistencia.")

nombre = st.text_input("Nombre")
email = st.text_input("Correo electrónico")

if st.button("Enviar"):
    if nombre.strip() and email.strip():
        # Guardar en CSV local
        df = pd.DataFrame([[nombre, email, datetime.now().isoformat()]],
                          columns=["Nombre", "Email", "Fecha"])
        df.to_csv("asistencia.csv", mode='a', index=False, header=False)
        st.success("✅ ¡Asistencia registrada!")
    else:
        st.warning("⚠️ Por favor, rellena ambos campos.")

# Generar y mostrar el código QR con la URL de la app
st.subheader("📱 Accede a esta página desde tu móvil")
qr = qrcode.make(app_url)
buf = BytesIO()
qr.save(buf, format="PNG")
st.image(buf.getvalue(), caption="Escanea este QR para abrir la app", use_column_width=False)


