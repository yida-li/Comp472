import os
import openai
import pyautogui


openai.api_key = "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"


while(True):
    yida=pyautogui.prompt('Ask a Question to openai ;)')
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content":""+yida+""}
    ]
    )
    reply=completion.choices[0].message['content']
    pyautogui.alert(reply)

