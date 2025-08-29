# Detector de Dígito 5 com Streamlit e Scikit-learn

Este projeto é uma aplicação web desenvolvida em Python com **Streamlit** que utiliza um modelo de Machine Learning para classificar em tempo real se um dígito desenhado à mão é o número 5.

O modelo utilizado é um **SGDClassifier** (Classificador de Gradiente Descendente Estocástico) treinado com o famoso dataset **MNIST**, que contém milhares de imagens de dígitos manuscritos.

---

## 🚀 Screenshots da Aplicação

Abaixo, a aplicação em funcionamento, classificando um dígito como "não é o 5" e outro corretamente como o número 5.

| Não é o número 5 | É o número 5 |
| :-----------------: | :--------------: |
| ![Exemplo de classificação negativa]![alt text](<Captura de tela 2025-08-29 000624.png>) | ![Exemplo de classificação positiva].![alt text](<Captura de tela 2025-08-29 000436.png>) |

**Observação:** Para que as imagens apareçam, você precisa fazer o upload delas no GitHub. O jeito mais fácil é editar o `README.md` diretamente no site do GitHub e arrastar os seus arquivos de print para o local indicado (`URL_DA_IMAGEM_AQUI`).

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* **Streamlit:** Para a criação da interface web interativa.
* **Scikit-learn:** Para o treinamento e utilização do modelo de Machine Learning.
* **Streamlit Drawable Canvas:** Componente que permite o desenho livre na aplicação.
* **Numpy & OpenCV:** Para o pré-processamento e manipulação das imagens desenhadas.

---

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação na sua máquina.

**1. Clone o repositório:**
```bash
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
cd seu-repositorio

**2. Crie e ative um ambiente virtual:# Crie o ambiente**
python -m venv .venv

# Ative o ambiente (Windows)
.venv\Scripts\activate

# Ative o ambiente (macOS/Linux)
source .venv/bin/activate
3. Instale as dependências:Com o ambiente virtual ativo, instale todas as bibliotecas necessárias.pip install -r requirements.txt
4. Execute a aplicação Streamlit:streamlit run app.py
Pronto! A aplicação será aberta automaticamente no seu navegador.
