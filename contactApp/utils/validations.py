from phonenumbers import is_valid_number, NumberParseException, parse

from utils.connectionSetup import get_db_connection

#Connections and cursors should be closed after operations to avoid potential resource leaks.
def is_email_unique(email):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM contacts WHERE email=?", (email,))
    return cur.fetchone() is None

def validate_phone_number(phone_number):
    try:
        number = parse(phone_number, None)
        return is_valid_number(number)
    except NumberParseException:
        return False

def is_phone_number_unique(phone_number):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM contacts WHERE phone_number=?", (phone_number,))
    return cur.fetchone() is None
