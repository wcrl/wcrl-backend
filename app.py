from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello WCRL!</p>"

@app.route("/api/teams")
def get_teams():
    return [
        {"id": 1, "teamName": "TeamName1", "totalPoints": 10},
        {"id": 2, "teamName": "TeamName2", "totalPoints": 20},
    ]

@app.post("/api/teams")
def create_team():
    data = request.get_json()
    return {
        "message": "Received team name",
        "teamName": data
    }