from flask import Blueprint, session, request, jsonify
from utils.connectionSetup import get_db_connection
from utils.validations import is_email_unique, validate_phone_number, is_phone_number_unique

add_contactsBp = Blueprint('add_contactsBp', __name__)


@add_contactsBp.route('/contacts/add', methods=['GET', 'POST'])
def add_contact():
    if 'user_id' not in session:
        return jsonify("login again")
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        user_id = session['user_id']
        if email :
            if not is_email_unique(email):
                return jsonify("Email address is not unique")
        if not validate_phone_number(phone_number):
            return jsonify("Phone number is not valid")
        if not is_phone_number_unique(phone_number):
            return jsonify("Phone number is already registered for another contact")
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO contacts (user_id, name, email, phone) VALUES (?, ?, ?, ?)",
                    (user_id, full_name, email, phone_number))
        conn.commit()
        return jsonify("contact added successfully")
