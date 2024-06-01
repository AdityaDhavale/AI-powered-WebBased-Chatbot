import gradio as gr
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
from huggingface_hub import login

# Logging in to Hugging Face using API token
api_token = "Hugging Face API token"
login(api_token)

# Loading the Blenderbot-3B model and tokenizer from Hugging Face
model_name = "facebook/blenderbot-3B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Using a pipeline as a high-level helper
pipe = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

messages = [{"role": "system", "content": "AI Chatbot"}]

def CustomChatbot(user_input):
    messages.append({"role": "user", "content": user_input})
    
    # Preparing the input for the model
    input_string = " ".join([f"{message['role']}: {message['content']}" for message in messages])
    
    # Generating a response using the pipeline
    response = pipe(input_string, max_length=500, pad_token_id=tokenizer.eos_token_id)
    Chatbot_reply = response[0]['generated_text']
    
    messages.append({"role": "assistant", "content": Chatbot_reply})
    return Chatbot_reply

# Setting up the Gradio interface
demo = gr.Interface(fn=CustomChatbot, inputs="text", outputs="text", title="AI Powered Web-based ChatBot")

demo.launch(share=True)
