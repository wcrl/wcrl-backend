from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello WCRL!</p>"

@app.route("/api/teams")
def get_teams():
    return [
        # (team_id, teamName, totalPoints)
        {"team_id": 1, "teamName": "TeamName1", "totalPoints": 10},
        {"team_id": 2, "teamName": "TeamName2", "totalPoints": 20},
    ]

@app.post("/api/teams")
def create_team():
    data = request.get_json()
    return {
        "message": "Received team name",
        "teamName": data
    }

@app.route("/api/members")
def get_member():
    return [
        # (discord_id, name, email)
        {"discord_id": 1, "users_name": "Watson", "email": "Watson123@gmail.com"},
        {"discord_id": 2, "users_name": "Bot", "email": "Bot321@gmail.com"},
    ]