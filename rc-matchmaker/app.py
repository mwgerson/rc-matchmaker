# user endpoint
# database

from flask import Flask, render_template

import matching
from users import fetch_users

app = Flask(__name__)

@app.route('/')
def index():
    # TODO: redirect to /coffee

    # Backend: Create list of "users"
    # Frontend: # List all users
    users = fetch_users()

    # Backend: stub out a pairing algorithm
    # Frontend: List current pairings
    matched_users, unmatched_users = matching.match_users(users)

    # Backend: create algorithm + create tests

    return render_template('test_coffee.html',
                           users=users,
                           matched_users=matched_users,
                           unmatched_users=unmatched_users)

@app.route('/coffee')
def coffee():
    return "Welcome to the Coffee Matchmaker!"

if __name__=='__main__':
    app.run(debug=True)