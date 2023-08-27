import openai

def query_chatgpt(query, api_key):
    openai.api_key = api_key
    res = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {"role": "user", "content": f"{query}"},
        ]
    )
    return res['choices'][0]['message']['content']
