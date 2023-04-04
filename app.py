from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

model_api_key = os.environ.get('OPENAI_API_KEY')

openai.api_key = model_api_key
model_engine = "davinci"

@app.route('/', methods=['POST'])
def chat():
    content = request.json['content']

    response = openai.Completion.create(
        engine=model_engine,
        prompt=content,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return jsonify({'content': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run()
