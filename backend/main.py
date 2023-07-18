from flask import Flask, request, jsonify
import openai
import os
import psycopg2


app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')  # obtenemos la API KEY del entorno

@app.route('/api/compose', methods=['POST'])
def compose():
    text = request.get_json()['text']
    response = openai.Completion.create(engine="text-davinci-002", prompt=text, max_tokens=100)
    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(port=5000)


conn = psycopg2.connect(
    dbname="your-db-name",
    user="your-username",
    password="your-password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    message = data['message']
    response = openai.Completion.create(engine="text-davinci-004", prompt=message, max_tokens=60)
    response_text = response.choices[0].text.strip()
    cur.execute("INSERT INTO logs (user_input, gpt_response) VALUES (%s, %s)", (message, response_text))
    conn.commit()
    return response_text
