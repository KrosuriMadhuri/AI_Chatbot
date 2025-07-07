import requests
from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import ChatLog

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": f"Bearer {settings.HF_API_KEY}"}

@login_required
def chat_view(request):
    response_text = None
    user_prompt = None

    if request.method == 'POST':
        user_prompt = request.POST.get("prompt")
        try:
            payload = {
                "inputs": f"<|user|>\n{user_prompt}\n<|assistant|>\n"
            }
            response = requests.post(API_URL, headers=HEADERS, json=payload)
            data = response.json()

            if isinstance(data, list) and "generated_text" in data[0]:
                response_text = data[0]["generated_text"]
                # Clean assistant response
                if "<|assistant|>" in response_text:
                    response_text = response_text.split("<|assistant|>")[-1].strip()
                else:
                    response_text = response_text.strip()
            else:
                response_text = "Invalid response format"

            # ✅ Save to database inside POST block
            if user_prompt and response_text:
                ChatLog.objects.create(
                    user=request.user,
                    prompt=user_prompt,
                    response=response_text
                )

        except Exception as e:
            response_text = f"Error: {str(e)}"

    return render(request, "ai_assistant/chat.html", {
        "response": response_text,
        "user_prompt": user_prompt
    })
