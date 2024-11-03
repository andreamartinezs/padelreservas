import smtplib
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart
import streamlit as st



def send(email, nombre, fecha, hora, pista):
 
 
 #credenciales
 user = st.secrets["emails"]["smtp_user"]
 password = st.secrets ["emails"]["smtp_password"]

 sender_email = "Club de Padel"
 # Configuracion del servidor
 msg = MIMEMultipart()
 
 smtp_server = "smtp.gmail.com"
 smtp_port = 587
 

 #Parametros del mensaje
 msg ['From'] = sender_email
 msg ['To'] = email
 msg ['Subject'] = 'Reserva de pista'

 #Cuerpo del mensaje
 message = f"""
 Hola {nombre},
 Su reserva ha sido realizada con exito.
 Fecha: {fecha}
 Hora: {hora}
 Pista: {pista}

 Gracias por confiar en nosotros.
 Un saludo.
 """
 msg.attach(MIMEText(message,'plain'))
 
  #conexion al servidor
 try:
   server = smtplib.SMTP(smtp_server, smtp_port) 
   server.starttls()
   server.login(user, password) 
   server.sendmail(sender_email , email, msg.as_string()) 
   server.quit()
   
 except smtplib.SMTPException as e:
        st.error(f"Error al enviar el email: {e}")  # Cambia a st.error para mostrar el error
        st.exception(e)  # Esto imprimirá el stack trace del error


#Clases

def send(nombreclase, emailclase, fechaclase, horaclase, profe):
 
 
 #credenciales
 user = st.secrets["emails"]["smtp_user"]
 password = st.secrets ["emails"]["smtp_password"]

 sender_email = "Club de Padel"
 # Configuracion del servidor
 msg = MIMEMultipart()
 
 smtp_server = "smtp.gmail.com"
 smtp_port = 587
 

 #Parametros del mensaje
 msg ['From'] = sender_email
 msg ['To'] = emailclase
 msg ['Subject'] = 'Reserva de clases de padel'

 #Cuerpo del mensaje
 message = f"""
 Hola {nombreclase},
 Su clase de padel ha sido agendada con exito.
 Fecha: {fechaclase}
 Hora: {horaclase}
 Con el Instructor:
 Profe: {profe}

 Gracias por confiar en nosotros.
 Un saludo.
 """
 msg.attach(MIMEText(message,'plain'))
 
  #conexion al servidor
 try:
   server = smtplib.SMTP(smtp_server, smtp_port) 
   server.starttls()
   server.login(user, password) 
   server.sendmail(sender_email , emailclase, msg.as_string()) 
   server.quit()
   
 except smtplib.SMTPException as e:
        st.error(f"Error al enviar el email: {e}")  # Cambia a st.error para mostrar el error
        st.exception(e)  # Esto imprimirá el stack trace del error