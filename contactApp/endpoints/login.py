from flask import Blueprint, jsonify, request, session
from utils.connectionSetup import get_db_connection

loginBp = Blueprint('loginBP', __name__)


@loginBp.route('/base/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id FROM users WHERE email=? AND password=?", (email, password))
        user = cur.fetchone()
        if user:
            session['user_id'] = user[0]
            return jsonify("Logged in successfully")
        else:
            return jsonify("Wrong email or password")
    else:
        return jsonify("Welcome")
