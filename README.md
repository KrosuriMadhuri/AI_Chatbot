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
│   ├── SymptomsOutput.json
│   ├── DiseasesOutput.json
│   ├── symptomsDisease246k.json
│
├── app/
│   ├── __init__.py
│   ├── qna_engine.py
│   ├── priority_controller.py
│   ├── disease_scoring.py
│   ├── recommendation_engine.py
│   ├── response_formatter.py
│
├── main.py
├── requirements.txt
└── README.md
