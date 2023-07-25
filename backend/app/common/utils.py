import requests

def generate_response_from_gpt(input_text):
    # URL del API de ChatGPT
    api_url = 'https://api.openai.com/v1/chat/completions'

    # Parámetros de la solicitud
    headers = {
        'Authorization': 'Bearer KEY',
        'Content-Type': 'application/json'
    }
    data = {
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': input_text}]
    }

    try:
        # Realizar la solicitud POST al API de ChatGPT
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        
        # Obtener la respuesta generada del API
        response_json = response.json()
        response_text = response_json['choices'][0]['message']['content']

        return response_text
    except requests.exceptions.RequestException as e:
        print('Error en la solicitud al API de ChatGPT:', e)
        return None
