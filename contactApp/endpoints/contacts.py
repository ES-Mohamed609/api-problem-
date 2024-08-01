from flask import Blueprint, jsonify, session
from utils.connectionSetup import get_db_connection

contactsBp = Blueprint('contactsBp', __name__)
contactRemoveBp = Blueprint('contactRemoveBp', __name__)

@contactsBp.route('/base/contacts')
def contact_list():
    if 'user_id' not in session:
        return jsonify("login again")

    user_id = session['user_id']
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id , name FROM contacts WHERE user_id=?", (user_id,))
    contacts = cur.fetchall()
    return jsonify(contacts)

@contactRemoveBp.route('/base/contacts/remove/<int:contact_id>', methods=['POST'])
def remove_contact(contact_id):
    if 'user_id' not in session:
        return jsonify("login again")

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    conn.close()

    return jsonify("contact removed successfully")
