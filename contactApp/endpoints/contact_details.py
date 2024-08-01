from flask import session, redirect, url_for, request, Blueprint
from utils.connectionSetup import get_db_connection
from utils.validations import validate_phone_number


contact_detailsBp = Blueprint('contact_detailsBp', __name__)
#removed jsonify to test other ways


@contact_detailsBp.route('/contacts/<int:contact_id>', methods=['GET', 'POST'])
def contact_details(contact_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    cur = conn.cursor()

    if request.method == 'POST':
        name = request.form.get('full_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        if email:
            cur.execute("SELECT id FROM contacts WHERE email=? AND id!=?", (email, contact_id))
            if cur.fetchone():

                return redirect(url_for('contact_details', contact_id=contact_id))
        if phone_number:
            if not validate_phone_number(phone_number):

                return redirect(url_for('contact_details', contact_id=contact_id))
            cur.execute("SELECT id FROM contacts WHERE phone=? AND id!=?", (phone_number, contact_id))
            if cur.fetchone():

                return redirect(url_for('contact_details', contact_id=contact_id))
        cur.execute("UPDATE contacts SET email=?, phone=?, name=? WHERE id=?",
                    (email, phone_number, name, contact_id))
        conn.commit()
        return
