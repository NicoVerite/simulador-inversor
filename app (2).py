
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finanzas App", layout="centered")
st.title("💼 Finanzas App")
st.markdown("### Tu cartera, tu visión, tus decisiones. Pero con el respaldo de un análisis profesional.")
st.markdown("*Descubrí cómo invertir de forma inteligente, incluso si nunca lo hiciste.*")
st.markdown("---")

st.header("📋 Definí tu Perfil de Inversor")
horizonte = st.selectbox("¿Cuál es tu horizonte de inversión?", ["Corto plazo (<1 año)", "Mediano plazo (1-3 años)", "Largo plazo (>3 años)"])
riesgo = st.radio("¿Qué nivel de riesgo estás dispuesto a asumir?", ["Bajo", "Medio", "Alto"])
objetivo = st.selectbox("¿Cuál es tu objetivo principal?", ["Preservar capital", "Obtener ingresos periódicos", "Maximizar crecimiento del capital"])
capital = st.number_input("¿Con cuánto capital querés invertir? (en ARS)", min_value=10000, step=10000)

if st.button("Generar Estrategia"):
    if riesgo == "Bajo":
        cartera = {
            "Bonos y Lecaps": 0.4,
            "CEDEARs conservadores": 0.4,
            "Acciones locales estables": 0.1,
            "Liquidez": 0.1
        }
    elif riesgo == "Medio":
        cartera = {
            "Acciones locales (YPF, GGAL)": 0.4,
            "CEDEARs y bonos": 0.3,
            "Liquidez": 0.1,
            "Acciones de crecimiento": 0.2
        }
    else:
        cartera = {
            "Acciones locales con alto potencial": 0.5,
            "Acciones tecnológicas (TTWO, etc.)": 0.2,
            "Liquidez": 0.1,
            "Bonos volátiles": 0.2
        }

    st.subheader("📊 Distribución sugerida de tu cartera")
    df = pd.DataFrame.from_dict(cartera, orient='index', columns=['% de Capital'])
    df['ARS'] = df['% de Capital'] * capital
    st.dataframe(df.style.format({"% de Capital": "{:.0%}", "ARS": "$ {:,.0f}"}))

    st.success("Estrategia generada según tu perfil y la visión de mercado actual.")
    st.markdown("---")

    st.markdown("### 📩 ¿Querés una asesoría personalizada?")
    st.markdown(
        "¿Querés que analicemos tu situación y diseñemos una estrategia como esta, "
        "pero personalizada para vos?  
👉 Contactame directamente desde acá y hablamos sin compromiso."
    )

    whatsapp_url = "https://wa.me/543751599873"
    st.markdown(f"[📲 Quiero una asesoría personalizada]({whatsapp_url})", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("**Eduardo Verité**  
*Asesor Financiero Independiente*  
*Especialista en Estrategias de Inversión y Macroeconomía Argentina*")
