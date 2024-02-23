import openai

# Set your OpenAI API key
api_key = '(api key)'
openai.api_key = api_key

def chat_with_gpt(prompt):
    # Make a request to the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can choose a different engine
        prompt=prompt,
        max_tokens=150  # You can adjust the response length
    )
    
    # Extract and return the model's reply
    return response['choices'][0]['text']

# Example usage
user_input = "Tell me a joke."
bot_reply = chat_with_gpt(user_input)
print(bot_reply)