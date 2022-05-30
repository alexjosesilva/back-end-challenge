from flask import Flask
import json
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    mensagem = "Back-end Challenge 2021 🏅 - Space Flight News"
    return (mensagem)

@app.route("/articles/", methods=['GET'])
def articles():
    response = requests.get("https://api.spaceflightnewsapi.net/v3/articles")
    data = response.json()

    if (response.status_code == 200):
        print("The request was a success! 200: ")
        return 
    else:
        print("The request was a error!")
        return 

if __name__ == "__main__":
    app.run(debug=True)