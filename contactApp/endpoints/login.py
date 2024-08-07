from flask import Blueprint, jsonify, request, session
from utils.connectionSetup import get_db_connection

loginBp = Blueprint('loginBP', __name__)

""""if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT id, password FROM users WHERE email=?", (email,))
                    user = cur.fetchone()
                    if user and check_password_hash(user[1], password):
                        session['user_id'] = user[0]
                        return jsonify({"message": "Logged in successfully"}), 200
                    else:
                        return jsonify({"message": "Wrong email or password"}), 401
        except Exception as e:
            logger.error(f"Error during login: {e}")
            return jsonify({"message": "Internal server error"}), 500
    else:
        return render_template('login.html')"""
#Added input validation for email and password.
#Used structured JSON responses with appropriate HTTP status codes.
#Included an example for rendering a login template for GET requests.




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
