# netlify/functions/api/main.py
import json
from flask import Flask, request
from werkzeug.wrappers import Response

# Importe sua aplicação Flask original (assumindo que ela esteja em app.py)
from app import app as flask_app

def handler(event, context):
    """Handler para a função Netlify."""
    with flask_app.test_client() as client:
        path = event.get('path', '/')
        method = event.get('httpMethod', 'GET').upper()
        headers = event.get('headers', {})
        body = event.get('body', None)

        # Converte os headers para o formato esperado pelo Flask
        flask_headers = [(k, v) for k, v in headers.items()]

        response = client.open(
            path=path,
            method=method,
            headers=flask_headers,
            data=body,
            content_type=headers.get('content-type')
        )

        return {
            "statusCode": response.status_code,
            "headers": dict(response.headers),
            "body": response.get_data(as_text=True),
        }

if __name__ == "__main__":
    # Para testes locais (opcional)
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Flask app running locally for Netlify Function test!"

    if __name__ == '__main__':
        app.run(debug=True)