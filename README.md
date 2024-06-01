# AI-powered-WebBased-Chatbot
This project aims to develop an AI-powered chatbot using the Blenderbot-3B model from Hugging Face, known for generating human-like responses. By integrating this advanced conversational agent with a user-friendly web interface created with Gradio, the project ensures a seamless and engaging interaction experience for users.

1.Importing Libraries:

'gradio' is used to create a web interface.
transformers from Hugging Face is used to load and work with transformer models.
login from 'huggingface_hub' is used to authenticate with the Hugging Face Hub.

2.Logging into Hugging Face:

Here, the 'api_token' is used to log in to the Hugging Face platform, enabling access to models.

3.Loading the Blenderbot-3B Model and Tokenizer:

'model_name' specifies the Blenderbot-3B model.
'AutoTokenizer.from_pretrained(model_name)' loads the tokenizer associated with the model.
'AutoModelForSeq2SeqLM.from_pretrained(model_name)' loads the model itself.

4.Creating a Pipeline:

A pipeline is created for text-to-text generation using the loaded model and tokenizer, making it easier to generate responses.

5.Initializing the Conversation:

messages is a list to store the conversation history, starting with a system message indicating that it's an AI Chatbot.

6.Defining the Custom Chatbot Function:

This function takes the user_input, appends it to the messages list as a user message.
input_string is prepared by concatenating all messages in the format "role: content".
response is generated using the pipe, specifying a max_length for the response and padding tokens.
The model's reply (Chatbot_reply) is extracted and appended to messages as the assistant's response.
The function returns the chatbot's reply.

7.Setting Up the Gradio Interface:

gr.Interface is used to create a web interface for the chatbot.
fn specifies the function to be called (CustomChatbot).
inputs and outputs specify the types of input and output (both text in this case).
title sets the title of the web interface.

8.Launching the Interface:

launch starts the Gradio interface, with share=True allowing the interface to be accessible via a public link.
