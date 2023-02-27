import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.figure_factory as ff

st.write("PRUEBA SI ERES APTO PARA EL CREDITO")

#Se consigue la edad
edad = st.slider("Seleccione su edad", 0, 70)
#Se consigue el trabajo
trabajo = st.selectbox("Trabajo",
                      ("technician", "unknown", "blue-collar", "admin", "housemaid", "retired", "services", "entrepreneur", "management"))
#Se consigue el esatdo civil
estadoCivil = st.selectbox("Estado civil", ("married", "divorced", "single"))
#Se consigue el nivel de educación de la persona
estudios = st.selectbox("Nivel educativo",
                        ("high.school", "unknown", "basic.9y", "professional.course", "university.degree", ""))
#Se consigue el default
default = st.selectbox("Default", ("no", "unknown"))
#Se consigue si tiene casa
casa = st.selectbox("Alojamiento", ("no", "yes", "unknown"))
#Se consigue si tiene algun prestamo
prestamo = st.selectbox("Prestamos", ("no", "yes", "unknown"))
#Se consigue el contacto
contacto = st.selectbox("Contacto", ("cellular", "telephone"))
#Se consigue el mes
mes = st.selectbox("Mes", ("may", "jun", "jul", "aug", "oct", "nov", "apr", "sep"))
#Se consigue el día
dia = st.selectbox("Dia", ("mon", "thu", "fri", "wed", "tue"))
#Se consigue la campaña
campaña = st.slider("Seleccione su numero de campaña", 0, 20)
#Se consigue los pdays
pdays = st.slider("Seleccione su pdays", 0, 1500)
#Se consigue el previusly
previusly = st.slider("Indique su previusly", 0, 10)
#Se consigue el poutcome
poutcome = st.selectbox("poutcome", ("failure", "nonexistent", "success"))
#Se consigue el emp.var.rate
empvarrate = st.number_input("emp.var.rate", (-3.40))
#Se consigue cons.price.idx
conspriceidx = st.number_input("cons.price.idx", (92.20))
#Se consigue el cons.conf.idx
consconfidx = st.number_input("cons.conf.idx", (-50.80))
#Se consigue el valor euribor3m
euribor3m = st.number_input("euribor3m", (0.63))
# Se consigue el nr.employed
nremployed = st.number_input("nr.employed", (4963.60))

#SE REALIZA EL ENVIO DE DATOS
envio = st.button("¡ENVIAR!")





