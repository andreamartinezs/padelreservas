import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Landing Page - Padel Services", layout="wide")

# Estilo personalizado
st.markdown("""
<style>
    .navbar {
        display: flex;
        justify-content: flex-end;
        background-color: #333;
        padding: 10px;
    }
    .navbar a {
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        text-align: center;
    }
    .hero {
        height: 550px;
        background-image: url('assets/padelbanner.jpg');
        background-size: cover;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
    }
    .hero button {
        padding: 15px 30px;
        font-size: 18px;
        background-color: #28a745;
        color: white;
        border: none;
        cursor: pointer;
    }
    .services, .partners, .about, .contact-form {
        padding: 50px;
        text-align: center;
    }
    .card {
        background-color: white;
        border-radius: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
        width: 200px;
        padding: 20px;
        margin: 10px;
    }
    .footer {
        background-color: #333;
        color: white;
        text-align: center;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Navbar
st.markdown('<div class="navbar">'
            '<a href="#home">Home</a>'
            '<a href="#services">Services</a>'
            '<a href="#about">About Us</a>'
            '<a href="#contact">Contact</a>'
            '</div>', unsafe_allow_html=True)

# Hero section
st.markdown('<div class="hero">'
            '<h1 style="color:white;">¡Bienvenido a nuestro club de Padel!</h1>'
            '<button>Reserva ya</button>'
            '</div>', unsafe_allow_html=True)

# Services section
st.header("Services")
col1, col2, col3 = st.columns(3)
with col1:
    st.image('assets/pistacard.jpeg', width=100)
    st.subheader("Alquiler de Pistas de Padel")
with col2:
    st.image('assets/padelcard1.jpg', width=100)
    st.subheader("Clases de Padel")
with col3:
    st.image('assets/cafeteria.jpg', width=100)
    st.subheader("Cafetería")

# Partners section
st.header("Nuestros Socios")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image('assets/adidas.png', width=100)
with col2:
    st.image('assets/gatore.png', width=100)
with col3:
    st.image('assets/wpt.jpg', width=100)
with col4:
    st.image('assets/spotify-logo.png', width=100)

# About section
st.header("Sobre Nosotros")
st.write("Somos una empresa dedicada al padel, ofreciendo las mejores instalaciones y servicios para que disfrutes de este apasionante deporte. Nuestro objetivo es brindar una experiencia única a todos nuestros clientes, desde alquiler de pistas hasta clases personalizadas.")

# Contact form section
st.header("Contacto")
name = st.text_input("Tu nombre")
email = st.text_input("Tu email")
message = st.text_area("Tu mensaje")
if st.button("Enviar"):
    st.success("Mensaje enviado!")

# Footer section
st.markdown('<div class="footer">'
            '<p>Síguenos en nuestras redes sociales:</p>'
            '<a href="https://facebook.com" target="_blank"><i class="fab fa-facebook-f"></i></a>'
            '<a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>'
            '<a href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>'
            '<a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin-in"></i></a>'
            '</div>', unsafe_allow_html=True)