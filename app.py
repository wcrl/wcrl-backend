from flask import Flask, request
import database

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello WCRL!</p>"

@app.route("/api/teams")
def get_teams():
    return database.get_team_data

@app.route("/api/members")
def get_member():
    return database.get_member_data