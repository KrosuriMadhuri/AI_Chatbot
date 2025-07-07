from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {settings.HF_API_KEY}"}

@login_required
def symptom_checker_view(request):
    response_text = None
    symptoms = None

    if request.method == 'POST':
        symptoms = request.POST.get("symptoms")
        try:
            prompt = f"Analyze the following symptoms and suggest possible causes and actions: {symptoms}"
            payload = {
                "inputs": f"<|user|>\n{prompt}\n<|assistant|>\n"
            }
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            data = response.json()

            if isinstance(data, list) and "generated_text" in data[0]:
                response_text = data[0]["generated_text"]
                if "<|assistant|>" in response_text:
                    response_text = response_text.split("<|assistant|>")[-1].strip()
                else:
                    response_text = response_text.strip()
            else:
                response_text = "Invalid response format"
        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "medical_tools/symptom_checker.html", {
        "response": response_text,
        "symptoms": symptoms
    })

@login_required
def drug_info_view(request):
    response_text = None
    condition = None

    if request.method == 'POST':
        condition = request.POST.get("condition")
        try:
            prompt = f"Suggest drugs and treatments for the condition: {condition}. Explain their use briefly."
            payload = {
                "inputs": f"<|user|>\n{prompt}\n<|assistant|>\n"
            }
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            data = response.json()

            print("API RESPONSE: ", data)  # 🐞 Add this to debug

            # 🧠 Fix handling
            if isinstance(data, list) and data and "generated_text" in data[0]:
                response_text = data[0]["generated_text"]
                if "<|assistant|>" in response_text:
                    response_text = response_text.split("<|assistant|>")[-1].strip()
                else:
                    response_text = response_text.strip()
            elif isinstance(data, dict) and "error" in data:
                response_text = f"API Error: {data['error']}"
            else:
                response_text = f"Unexpected response: {data}"

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "medical_tools/drug_info.html", {
        "response": response_text,
        "condition": condition
    })
