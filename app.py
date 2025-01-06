import streamlit as st
from fpdf import FPDF
import io

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

st.write("Please rate the following questions on a scale of 1 to 10 (1: Strongly disagree, 10: Strongly agree)")
for i, question in enumerate(questions):
    score = st.slider(f"{i+1}. {question}", 1, 10, 5)
    scores.append(score)
    categories.append(question)

# Identifica prioridades
if scores:
    st.subheader("Priority")
    priorities = [question for question, score in zip(categories, scores) if score >= 8]
    if priorities:
        st.write("The following items have been classified as priorities:")
        for i, priority in enumerate(sorted(priorities), start=1):
            st.write(f"{i}. {priority}")

        # Geração do PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Priority Items", ln=True, align='C')
        pdf.ln(10)
        for i, priority in enumerate(sorted(priorities), start=1):
            pdf.cell(0, 10, txt=f"{i}. {priority}", ln=True)

        # Salvar em memória para download
        pdf_buffer = io.BytesIO()
        pdf_buffer.write(pdf.output(dest='S').encode('latin1'))
        pdf_buffer.seek(0)

        # Botão para baixar o PDF
        st.download_button(
            label="Download PDF",
            data=pdf_buffer,
            file_name="priorities.pdf",
            mime="application/pdf"
        )
    else:
        st.write("No items were classified as priority.")

# Botão para finalizar
if st.button("Finish"):
    st.write("Thank you for participating!")


