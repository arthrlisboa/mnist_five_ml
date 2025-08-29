Detector de Dígito 5 com Streamlit e Scikit-learnEste projeto é uma aplicação web desenvolvida em Python com Streamlit que utiliza um modelo de Machine Learning para classificar em tempo real se um dígito desenhado à mão é o número 5.O modelo utilizado é um SGDClassifier (Classificador de Gradiente Descendente Estocástico) treinado com o famoso dataset MNIST, que contém milhares de imagens de dígitos manuscritos.🚀 Screenshot da AplicaçãoAqui você pode ver a aplicação em funcionamento, classificando corretamente um dígito desenhado no canvas.![alt text](<Captura de tela 2025-08-29 000436.png>)
![alt text](<Captura de tela 2025-08-29 000624.png>)
🛠️ Tecnologias UtilizadasPython 3.10+Streamlit: Para a criação da interface web interativa.Scikit-learn: Para o treinamento e utilização do modelo de Machine Learning.Streamlit Drawable Canvas: Componente que permite o desenho livre na aplicação.Numpy & OpenCV: Para o pré-processamento e manipulação das imagens desenhadas.⚙️ Como Executar o Projeto LocalmenteSiga os passos abaixo para rodar a aplicação na sua máquina.1. Clone o repositório:git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Crie e ative um ambiente virtual:# Crie o ambiente
python -m venv .venv

# Ative o ambiente (Windows)
.venv\Scripts\activate

# Ative o ambiente (macOS/Linux)
source .venv/bin/activate
3. Instale as dependências:Com o ambiente virtual ativo, instale todas as bibliotecas necessárias.pip install -r requirements.txt
4. Execute a aplicação Streamlit:streamlit run app.py
Pronto! A aplicação será aberta automaticamente no seu navegador.