import streamlit as st
import numpy as np
from sklearn.datasets import fetch_openml
from sklearn.linear_model import SGDClassifier
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import cv2 

@st.cache_resource
def carregar_e_treinar_modelo():
    """
    Esta funcao carrega o dataset MNIST e treina um classificador binário
    (SGDClassifier) para identificar o dígito 5.
    """
    
    mnist = fetch_openml('mnist_784', version=1, as_frame=False, parser='auto')
    X, y = mnist["data"], mnist["target"]
    y = y.astype(np.uint8)
    y_train_5 = (y == 5)
    sgd_clf = SGDClassifier(random_state=42)
    sgd_clf.fit(X, y_train_5)

    return sgd_clf


st.title("Detector do Dígito 5 ✍️")

st.markdown("""
Desenhe um único dígito no quadro abaixo. O modelo vai identificar se o digito desenhado é o número **5**.
""")

modelo = carregar_e_treinar_modelo()

st.sidebar.header("Configurações do Canvas")
stroke_width = st.sidebar.slider("Espessura do Traço: ", 10, 30, 20)
stroke_color = st.sidebar.color_picker("Cor do Traço: ", "#FFFFFF")
bg_color = st.sidebar.color_picker("Cor de Fundo: ", "#000000")

canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=280, 
    width=280,  
    drawing_mode="freedraw",
    key="canvas",
)

if st.button('É o número 5?'):
    if canvas_result.image_data is not None:       
        img_desenhada = cv2.cvtColor(canvas_result.image_data.astype('uint8'), cv2.COLOR_RGBA2GRAY)
        
        img_redimensionada = cv2.resize(img_desenhada, (28, 28), interpolation=cv2.INTER_NEAREST)
        vetor_imagem = img_redimensionada.flatten().reshape(1, -1)
        previsao = modelo.predict(vetor_imagem)
        if previsao[0]: 
            st.success("Sim, o modelo acredita que este é o número 5! 🎉")
        else: 
            st.error("Não, o modelo acredita que este não é o número 5. ❌")

    else:
        st.warning("Por favor, desenhe um número no quadro antes de prever.")
