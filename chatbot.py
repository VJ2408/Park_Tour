import openai

# Set your OpenAI API key here
api_key = '(provide API) '
openai.api_key = api_key

def ask_question(question, chat_log=None):
    if chat_log is None:
        chat_log = "The chatbot is turned off. You can turn it on by typing 'Turn on chatbot.'\n"
    
    response = openai.ChatCompletion.create(
        model="text-davinci-003",
        messages=[
            {"role": "system", "content": chat_log},
            {"role": "user", "content": question}
        ]
    )
    
    answer = response.choices[0].message['content']
    
    return answer

# Initialize the chat log
chat_log = "The chatbot is turned off. You can turn it on by typing 'Turn on chatbot.'\n"

while True:
    user_input = input("User: ")
    
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    if user_input.lower() == 'turn on chatbot':
        chat_log = ""
        print("Chatbot is turned on.")
        continue
    
    # Add user input to the chat log
    chat_log += f"User: {user_input}\nAI:"
    
    # Call the ask_question function with the updated chat log
    bot_response = ask_question(user_input, chat_log)
    
    # Add bot response to the chat log
    chat_log += f"{bot_response}\n"
    
    print("AI:", bot_response)

