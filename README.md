# AI Medical Chatbot for Disease Prediction and Personalized Recommendations

---

## Project Description

The goal is to design and implement an **AI-powered medical chatbot** that:

Guides users through a **structured Q&A flow**  
Predicts **possible diseases** based on symptoms  
Provides **personalized recommendations**, including:  
- Over-the-counter (OTC) medications  
- Home remedies  
- Physician referral  
- Emergency care instructions  

Uses **dynamic question prioritization**  
Focuses on **safety-first and explainability**  

---

## Project Structure

```text
/medical_chatbot_project
├── data/
│   ├── SymptomsOutput.json                <-- original
│   ├── SymptomsOutput_updated.json        <-- with user_question (simple)
│   ├── DiseasesOutput.json
│   ├── DiseasesOutput_updated.json
│   ├── symptomsDisease246k.json           <-- used for Embedding Matcher / Classifier
│
├── app/
│   ├── __init__.py
│   ├── qna_engine.py
│   ├── priority_controller.py
│   ├── disease_scoring.py
│   ├── recommendation_engine.py
│   ├── response_formatter.py
│   ├── embedding_matcher.py               <-- Phase 2.2
│
├── generate_user_questions.py             <-- Phase 2.1
├── main.py                                <-- Phase 2 READY
├── requirements.txt
└── README.md
