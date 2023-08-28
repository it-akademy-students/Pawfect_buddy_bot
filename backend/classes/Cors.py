from flask_cors import CORS


class Cors:
    def __init__(self, app) -> None:
        CORS(app, resources={r'/*': {'origins': [
            'http://localhost:3000', # React
            'http://127.0.0.1:3000', # React
            '*'
        ]}}, supports_credentials=True)
