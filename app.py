import asyncio
import os

from flask import Flask, jsonify
from wcrl_db import Database

app = Flask(__name__)
DATABASE_PATH = os.environ["WCRL_DATABASE_PATH"]

def fetch_teams():
    async def fetch():
        db = Database(DATABASE_PATH, readonly=True)
        await db.connect()

        try:
            return await db.teams.list_with_member_counts()
        finally:
            await db.close()
    return asyncio.run(fetch())

@app.route("/api/teams", methods = ["GET"])
def get_teams():
    teams = fetch_teams()
    return jsonify(teams)

# Run Flask backend
if __name__ == "__main__":
    app.run(debug = True)