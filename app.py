from flask import Flask
from flask_cors import CORS
from routes.user_routes import user_bp
from routes.record_routes import record_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(record_bp)

@app.route("/")
def home():
    return {"message": "Finance Dashboard API Running"}

if __name__ == "__main__":
    app.run(debug=True)