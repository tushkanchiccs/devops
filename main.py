from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['POST'])
def register():
    team_name = request.form['team_name']
    captain = request.form['captain']
    teammate1 = request.form['teammate1']
    teammate2 = request.form['teammate2']

    db.insert_user(team_name, captain, teammate1, teammate2)

    return redirect(url_for('teams'))

@app.route('/teams')
def teams():
    teams = db.get_teams()
    return render_template('teams.html', teams=teams)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
