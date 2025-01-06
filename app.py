import streamlit as st
import numpy as np

# Função para calcular a pontuação final
def calculate_final_score(scores):
    max_score = len(scores) * 10  # Pontuação máxima se todas as variáveis tiverem nota 10
    total_score = sum(scores)
    percentage_score = (total_score / max_score) * 100 if max_score > 0 else 0
    return percentage_score

# Lista de questões
questions = [
    "Makes me soup when I'm under the weather",
    "Makes repairs around the house",
    "Offers comfort when I'm down",
    "Opens up about personal hopes and fears",
    "Plays strategy games with me",
    "Prepares a relaxing bath for me",
    "Provides comfort during setbacks",
    "Puts together a fun date",
    "Recommends podcasts or courses for me",
    "Regularly expresses gratitude for us",
    "Rests their hand on my lap",
    "Runs their hands through my back",
    "Runs their hands through my hair",
    "Says 'I love you' and 'Thank you' every day",
    "Sends supportive messages during tough times",
    "Shares an insightful article with me",
    "Shares their thoughts and feelings openly",
    "Shares words of encouragement",
    "Shows interest in learning and growing",
    "Sits on my lap",
    "Sits quietly with me",
    "Solves riddles or brain teasers with me",
    "Spends time with my family",
    "Supports my career ambitions",
    "Supports my daily routine",
    "Supports my learning in a new hobby",
    "Surprises me with movie tickets",
    "Surprises me with something for my wellness",
    "Surprises me with something I've been wanting",
    "Takes a bike ride with me",
    "Takes out trash without being asked",
    "Tries new cafes with me",
    "Understands my feelings without asking",
    "Uses a gentle tone of voice with me",
    "Uses humor to bond with me",
    "Waters my plants without being asked",
    "Wraps their arms around me"
]

# Título da aplicação
st.markdown("<h1 style='color: darkblue;'>Relationship Questions</h1>", unsafe_allow_html=True)

# Processamento das respostas
scores = []
categories = []

st.write("Avalie as seguintes questões em uma escala de 1 a 10 (1: Discordo totalmente, 10: Concordo totalmente)")
for i, question in enumerate(questions):
    score = st.slider(f"{i+1}. {question}", 1, 10, 5)
    scores.append(score)
    categories.append(question)

# Calcula a pontuação final
if scores:
    percentage_score = calculate_final_score(scores)
    st.write(f"Pontuação Final: {percentage_score:.2f}%")

    # Identifica prioridades
    st.subheader("Prioridades")
    priorities = [question for question, score in zip(categories, scores) if score >= 8]
    if priorities:
        st.write("Os itens a seguir foram classificados como prioridades:")
        for i, priority in enumerate(sorted(priorities), start=1):
            st.write(f"{i}. {priority}")
    else:
        st.write("Nenhum item foi classificado como prioridade.")


