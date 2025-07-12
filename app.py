from flask import Flask
from flask_cors import CORS
from routes.simulate_routes import simulate_bp
import os

app = Flask(__name__)
CORS(app, origins=["https://ajcarr.net", "https://ajcarr.net/ai"])

app.register_blueprint(simulate_bp, url_prefix='/api/simulate')

@app.route('/api/test')
def test():
    return {"message": "Backend is running"}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)