from flask import Flask
import os

app = Flask(__name__)

VERSION = os.getenv("VERSION", "v1")

@app.route("/")
def home():
    return f"Hello, Working on a task related to ArgoCD to automate application deployments by integrating it into the CI/CD pipeline | Version: {VERSION}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)