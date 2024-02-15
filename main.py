import openai
import gradio

openai.api_key = 'Your OpenAI API KEY'

messages = [{"role": "system", "content": "You are a helpful assistant"}]

def customChat(user_input):
    messages.append({"role": "system", "content": user_input})
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages= messages)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return reply

demo = gradio.Interface(fn=customChat, inputs="text", outputs="text", title="Your Title")

demo.launch()
