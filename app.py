import streamlit as st
from streamlit_option_menu import option_menu
from send_email import send
from google_sheets import GoogleSheets
import re
import uuid
from google_calendar import GoogleCalendar
import numpy as np
import datetime as dt 



##VARIABLES
page_title = "Club de Padel"
page_icon = "🎾"
layout = "centered"


horas = ["09:00","10:40", "14:00", "15:00", "16:30", "18:00", "19:30", "21:00"]
horasclase = ["07:00", "10:00", "15:00", "18:00"]
pistas = ["Pista 1", "Pista 2"]
profe = ["Instructor 1", "Instructor 2"]
tipoclase = ["12 Clases", "8 Clases", "4 Clases"]
personas = ["4 personas", "2 personas"]

document = "gestion-reservas-club"
sheet= "reservas"
sheet2="clases"
credentials = st.secrets ["sheets"]["credentials_sheet"]
idcalendar = "andreavmartinezsalas@gmail.com"
idcalendar2 = "f795cf7ccf1d3918a2eea9d0bf08b6ace18bc82384032d44d7fb23d39f6b03ef@group.calendar.google.com"
idcalendar3= "ef34651d3750c0d6fe7ceb328fb47df453da2edb180ba6d7581afedd0fba207f@group.calendar.google.com"
idcalendar4= "b78b8fd9048bc7c5b4e6b038ce3b1754925e1562dcd04b63187dd401914ca4af@group.calendar.google.com"
time_zone = "America/Caracas"

##FUNCIONES

def validate_email(email):
  pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
  if re.match(pattern, email):
    return True
  else:
    return False
    
def generate_uid():
  return str(uuid.uuid4())

def add_hour_and_half(time):
    parsed_time = dt.datetime.strptime(time, "%H:%M").time()
    new_time = dt.datetime.combine(dt.date.today(), parsed_time) + dt.timedelta(hours=1, minutes=30)
    return new_time.strftime("%H:%M")

   

st.set_page_config(page_title=page_title,page_icon=page_icon, layout=layout)



# Estilos CSS para el color de fondo de Bootstrap
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;  /* Color de fondo secundario de Bootstrap */
        }
        .header {
            background-color: #007bff;  /* Color del encabezado */
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
        }
        .stApp {
            background-color: #f8f9fa; /* Asegura que el fondo de la app también cambie */
        }
             .footer {
            position: static;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f8f9fa;  /* Color de fondo del footer */
            color: #b5b8b5;  /* Color del texto del footer */
            text-align: center;
            padding: 10px 0;
            font-size: 14px;
        }
        .social-icons a {
            color: #b5b8b5;  /* Color de los íconos de redes sociales */
            margin: 0 10px;  /* Espaciado entre íconos */
            text-decoration: none;  /* Sin subrayado */
        }
          <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">  
        }
    </style>
""", unsafe_allow_html=True)




st.image("assets/padelbanner.jpg", use_column_width=True)

st.markdown("""
    <div style="text-align: center;">
        <h2>¡Bienvenido a nuestro Club de Padel!</h2>
        <p>Aquí, la pasión por el pádel se vive a cada instante. Nuestras instalaciones están diseñadas para ofrecerte la mejor experiencia, con pistas de alta calidad y un ambiente amigable y acogedor.</p>
    </div>
""", unsafe_allow_html=True)
selected= option_menu(menu_title=None, options=["Reservar", "Pistas","Detalles", "Clases"],
                      icons=["calendar3","building-add","list","calendar3"],
                      orientation="horizontal",
                      styles={
        "container": {"padding": "0!important", "background-color": "#f8f9fa"},  # Color de fondo del contenedor
        "icon": {"color": "#54c116", "font-size": "25px"},  # Color del icono
        "nav-link": {"font-size": "21px", "text-align": "left", "margin": "0px", "padding": "10px", "color": "#495057"},
        "nav-link-selected": {"background-color": "#495057", "color": "white"},  # Estilo del elemento seleccionado
    })


if selected == "Clases":
  st.subheader("Agenda tu clase de padel")
  c1,c2 = st.columns(2)

  
  nombreclase = c1.text_input("Escribe tu nombre*")
  emailclase = c2.text_input("Escribe tu email*")
  fechaclase = c1.date_input("Fecha:")
  horaclase = c2.selectbox("Hora:",horasclase)
  tipoclase = c1.selectbox("Tipo de clase:",tipoclase)
  personas =c2.selectbox("Cantidad de personas:",personas)
  profe = c1.selectbox("Instructor:",profe)
  notasclase = c2.text_area("Notas:")

  if fechaclase:
    if profe == "Instructor 1":
        id = idcalendar3
    elif profe == "Instructor 2":
        id = idcalendar4

    calendar = GoogleCalendar(credentials, idcalendar)
    hours_blocked = calendar.get_events_start_time(str(fechaclase))
    result_hours = np.setdiff1d(horas, hours_blocked)
  agendar= st.button("Agendar")

  if agendar:
                 
    if nombreclase == "":
      st.warning("El nombre es obligatorio")
    elif emailclase =="":
      st.warning("El email es obligatorio")
    elif not validate_email(emailclase):
      st.warning("El email no es valido")
    else:
      with st.spinner("Agendando clase..."):
        #Crear evento en google calendar
        parsed_time = dt.datetime.strptime(horaclase, "%H:%M").time()
        hours1 = parsed_time.hour 
        minutes1 = parsed_time.minute
        end_hours= add_hour_and_half(horaclase)
        parsed_time2 = dt.datetime.strptime(end_hours, "%H:%M").time()
        hours2 = parsed_time2.hour
        minutes2= parsed_time2.minute
        start_time= dt.datetime(fechaclase.year, fechaclase.month, fechaclase.day, hours1+4, minutes1).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
        end_time= dt.datetime(fechaclase.year, fechaclase.month, fechaclase.day, hours2+4, minutes2).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
        calendar= GoogleCalendar(credentials, id)
        calendar.create_event(nombreclase,start_time,end_time,time_zone)
        #Crear registro en google sheet
        uid = generate_uid()
        data =[[nombreclase, emailclase, str(fechaclase),horaclase, tipoclase, personas, profe, notasclase,uid]]
        gs = GoogleSheets(credentials,document,sheet2)
        range = gs.get_last_row_range()
        gs.write_data(range,data)
        #Enviar email al usuario
        #send(email, nombre, fecha, hora, pista)
    st.success("Su clase ha sido agendada con exito")



    #Mejoras en el front de la seccion detalles con st.markdown


if selected == "Detalles":

    st.markdown("""
    <style>
          
    
      .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        font-family: Arial, sans-serif;
      }

      .subheader {
        font-size: 24px;
        margin-top: 20px;
        color: #333;
      }

      .map {
        width: 100%;
        height: 450px;
        border: 0;
      }
      .horarios {
        display: flex;
        justify-content: space-between;
        margin-top: 10px;
        padding: 10px 0;
        border-bottom: 1px solid #ccc;
      }

      .contact-info {
        margin-top: 10px;
      }

      .instagram {
        margin-top: 10px;
        color: #3f729b;
      }

      .instagram a {
        text-decoration: none;
        color: inherit;
      }
    </style>
                                 
      <div class="subheader">Ubicación</div>
      <iframe class="map" src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d125830.19382557349!2d-63.273219534195306!3d9.749666153617119!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8c3340ccdd67a481%3A0x498e5fe3065f3956!2sMatur%C3%ADn%206201%2C%20Monagas!5e0!3m2!1ses!2sve!4v1717741037142!5m2!1ses!2sve" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>

      <div class="subheader">Horarios</div>
      <div class="horarios">
        <div>Lunes</div>
        <div>10:00 - 20:00</div>
      </div>
      <div class="horarios">
        <div>Martes</div>
        <div>10:00 - 20:00</div>
      </div>
      <div class="horarios">
        <div>Miércoles</div>
        <div>10:00 - 20:00</div>
      </div>
      <div class="horarios">
        <div>Jueves</div>
        <div>10:00 - 20:00</div>
      </div>
      <div class="horarios">
        <div>Viernes</div>
        <div>10:00 - 20:00</div>
      </div>
      <div class="horarios">
        <div>Sábado</div>
        <div>10:00 - 21:00</div>
      </div>
      <div class="horarios">
        <div>Domingo</div>
        <div>10:00 - 19:00</div>
      </div>

      <div class="subheader">Contacto</div>
      <div class="contact-info">0414-998-5619</div>

      <div class="subheader">Instagram</div>
      <div class="instagram">Síguenos <a href="https://www.instagram.com/andreamartinezs/?hl=es-la" target="_blank">aquí</a> en Instagram</div>
    </div>
    """, unsafe_allow_html=True)


if selected == "Pistas":
    st.write("##")
    st.image("assets/cancha.jpg", caption="Pista 1 ")
    st.image("assets/cancha2.jpg", caption="Pista 2 ")

if selected == "Reservar":
  st.subheader("Reserva tu pista")
  c1,c2 = st.columns(2)

  nombre = c1.text_input("Escribe tu nombre*")
  email = c2.text_input("Escribe tu email*")
  fecha = c1.date_input("Fecha:")
  pista = c1.selectbox("Pista:",pistas)
  
  if fecha:
    if pista == "Pista 1":
        id = idcalendar
    elif pista == "Pista 2":
        id = idcalendar2

    calendar = GoogleCalendar(credentials, idcalendar)
    hours_blocked = calendar.get_events_start_time(str(fecha))
    result_hours = np.setdiff1d(horas, hours_blocked)
  
  hora = c2.selectbox("Hora:",result_hours)
  notas = c2.text_area("Notas:")

  #CSS para cambiar el color del botón
  st.markdown(
      """
      <style>
      .stButton > button {
          background-color: #1274e2;
          color: white;
          border: 2px solid transparent; /* Borde inicial transparente */
          transition: border 0.3s; /* Transición suave */}

      .stButton > button:hover {
          border: 2px solid green;
          color: white;
      }
       .stButton > button:active {
        background-color: green; /* Color verde al hacer clic */
    }
      </style>
      """,
      unsafe_allow_html=True
  )
  enviar = st.button("Reservar")

    ##BACKEND
   
    #Inicializar last_reservation_time si no existe
  if "last_reservation_time" not in st.session_state:
      st.session_state.last_reservation_time = None

  if enviar:
      current_time = dt.datetime.now()
      
        #Verificar si el usuario ha hecho una reservación recientemente
      if st.session_state.last_reservation_time and (current_time - st.session_state.last_reservation_time).total_seconds() < 20:
          st.warning("Por favor, espere unos segundos antes de realizar otra reservación.")
      else:                       
            #Verificar campos obligatorios
          if nombre == "":
              st.warning("El nombre es obligatorio")
          elif email == "":
              st.warning("El email es obligatorio")
          elif not validate_email(email):
              st.warning("El email no es válido")
          else:
              with st.spinner("Reservando pista..."):
                    #Crear evento en Google Calendar
                  parsed_time = dt.datetime.strptime(hora, "%H:%M").time()
                  hours1 = parsed_time.hour 
                  minutes1 = parsed_time.minute
                  end_hours = add_hour_and_half(hora)
                  parsed_time2 = dt.datetime.strptime(end_hours, "%H:%M").time()
                  hours2 = parsed_time2.hour
                  minutes2 = parsed_time2.minute
                  start_time = dt.datetime(fecha.year, fecha.month, fecha.day, hours1-4, minutes1).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
                  end_time = dt.datetime(fecha.year, fecha.month, fecha.day, hours2-4, minutes2).astimezone(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S')
                  
                  calendar = GoogleCalendar(credentials, id)
                  calendar.create_event(nombre, start_time, end_time, time_zone)
                
                    #Crear registro en Google Sheets
                  uid = generate_uid()
                  data = [[nombre, email, pista, str(fecha), hora, notas, uid]]
                  gs = GoogleSheets(credentials, document, sheet)
                  range = gs.get_last_row_range()
                  gs.write_data(range, data)
                  
                    #Enviar email al usuario
                  send(email, nombre, fecha, hora, pista)
                  
                    #Actualizar la hora de la última reservación
                  st.session_state.last_reservation_time = current_time

                  st.success("Su pista ha sido reservada con éxito, una confirmación se enviará a su correo electrónico en los próximos minutos.")

# Footer con íconos de redes sociales
st.markdown("""
    <div class="footer">
        2024 &copy; Club de padel website. Todos los derechos reservados.
        <div class="social-icons">
            <a href="https://www.instagram.com" target="_blank">
                <i class="fab fa-instagram"></i>
            </a>
            <a href="https://www.whatsapp.com" target="_blank">
                <i class="fab fa-whatsapp"></i>
            </a>
        </div>
    </div>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
""", unsafe_allow_html=True)




        
