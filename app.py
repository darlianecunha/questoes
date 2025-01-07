import streamlit as st
from fpdf import FPDF
import io

# Lista de questões
questions = [
    "Accepts me as I am", "Admires my accomplishments", "Apologises when they're wrong",
    "Appreciates my intelligence", "Asks how my day was", "Assists me in making difficult decisions",
    "Attends family events with me", "Bakes me a homemade treat", "Brings me a drink", "Builds trust through honesty",
    "Buys me a book by my favourite author", "Buys me a new pair of shoes",
    "Buys me a plant", "Buys me flowers just because",
    "Buys me my favourite snack", "Buys me new clothes",
    "Buys me something I've been talking about", "Buys me thoughtful gifts",
    "Celebrates my achievements with me", "Challenges me with thought-provoking questions",
    "Cheers on my personal achievements", "Cleans my car as a surprise", "Comforts me after a hard day",
    "Comforts me when I'm vulnerable", "Compliments my appearance",
    "Connects with me emotionally", "Cooks a meal for me", "Cooks a meal together with me", "Cooks my favourite meal",
    "Crafts a homemade gift for me", "Creates a playlist for me", "Cuddles with me while we watch a movie",
    "Dances with me", "Discusses a book we've read together", "Discusses future dreams together",
    "Discusses historical events with me", "Discusses the news and different perspectives",
    "Does the laundry without being asked", "Encourages curiosity and questioning",
    "Encourages me during tough times", "Encourages me to achieve my goals", "Encourages me to open up",
    "Encourages me to take on new challenges", "Encourages my self-care and mental health",
    "Encourages open communication", "Engages in intellectual debates with me",
    "Enjoys long walks with me", "Explores a museum with me", "Explores new places with me",
    "Expresses gratitude for the little things", "Expresses love through words daily",
    "Expresses their desire for me", "Finds reasons to laugh together often", "Fixes things around the house",
    "Gives me a back massage", "Gives me a foot massage", "Gives me a forehead kiss", "Gives me a framed photo of us",
    "Gives me a genuine compliment", "Gives me a handmade gift", "Gives me a hug", "Gives me physical affection",
    "Goes on dates with me", "Has heart-to-heart conversations with me", "Helps me achieve my goals",
    "Helps me learn from my mistakes", "Helps me outline steps to achieve goals", "Helps me overcome my fears",
    "Helps me practise a new skill", "Helps with house chores", "Holds my face lovingly", "Holds my hand in public",
    "Hugs me when I'm stressed", "Includes me in the conversation when we're out",
    "Initiates meaningful conversations about our dreams", "Introduces me to new ideas", "Is goofy and playful with me",
    "Joins me in a new activity I'm learning", "Joins me in my hobbies and interests",
    "Keeps promises and commitments", "Keeps me updated about their day", "Kisses me goodbye", "Kisses me passionately",
    "Leaves a cute note for me", "Lets me have the last piece of dessert", "Lets me vent when I'm stressed",
    "Listens and empathises with my feelings", "Makes me feel special", "Makes me laugh", "Makes me soup when I’m unwell",
    "Motivates me to achieve my goals", "Offers comfort when I'm down", "Organises a surprise date",
    "Pampers me when I'm ill", "Plans special dates for us", "Playfully teases me", "Plays board games with me",
    "Prepares a relaxing bath for me", "Provides career advice and guidance", "Puts together a fun date", "Regularly shares genuine compliments",
    "Remembers important dates and surprises me", "Runs errands for me", "Sends supportive messages during tough times",
    "Shares a blanket with me", "Shares a candlelit dinner with me", "Shares interesting facts they’ve learned",
    "Shares their deepest feelings with me", "Shares their thoughts and feelings openly", "Shows empathy when I'm upset", "Shows love through actions",
    "Sits quietly with me", "Solves riddles or brain teasers with me",
    "Spends quality time with me", "Supports my personal growth",
    "Surprises me with breakfast in bed", "Takes a bike ride with me",
    "Takes a walk with me", "Takes care of tasks I dislike",
    "Talks philosophy with me", "Tells me why they love me in detail",
    "Tries a new restaurant with me",
    "Uses kind words, even in disagreements", "Validates my feelings without judgement",
    "Watches the sunset or sunrise with me", "Waters my plants without being asked",
    "Wraps their arms around me", "Writes me a heartfelt letter"
]

# Título da aplicação
st.markdown("""
<div style='background-color:#f5f5f5; padding:20px;'>
    <h1 style='color: #003366; text-align: center;'>Relationship Questions</h1>
    <p style='text-align: center;'>Please rate the following questions on a scale of 1 to 10 (1: Strongly disagree, 10: Strongly agree)</p>
</div>
""", unsafe_allow_html=True)

# Processamento das respostas
scores = []
categories = []

for i, question in enumerate(questions):
    score = st.slider(f"{i+1}. {question}", 1, 10, 5)
    scores.append(score)
    categories.append(question)

# Identifica prioridades
if scores:
    st.markdown("""
    <div style='background-color:#e8f5e9; padding:15px;'>
        <h2 style='color: #003366;'>Priority Items</h2>
    </div>
    """, unsafe_allow_html=True)

    priorities = [(question, score) for question, score in zip(categories, scores) if score >= 7]
    if priorities:
        st.write("The following items have been classified as priorities:")
        for i, (priority, score) in enumerate(sorted(priorities, key=lambda x: -x[1]), start=1):
            st.write(f"{i}. {priority} (Score: {score})")

        # Geração do PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Priority Items", ln=True, align='C')
        pdf.ln(10)
        for i, (priority, score) in enumerate(sorted(priorities, key=lambda x: -x[1]), start=1):
            pdf.cell(0, 10, txt=f"{i}. {priority} (Score: {score})", ln=True)

        # Salvar em memória para download
        pdf_buffer = io.BytesIO()
        pdf.output(dest='S').encode('latin1')  # Especifica a saída do PDF como string binária
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
    st.write("Tool developed by Darliane Cunha")


