from .add_contacts import add_contactsBp
from .contact_details import contact_detailsBp
from .contacts import contactsBp, contactRemoveBp
from .login import loginBp
from flask import Flask


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(loginBp)
    app.register_blueprint(contactsBp)
    app.register_blueprint(contactRemoveBp)
    app.register_blueprint(add_contactsBp)
    app.register_blueprint(contact_detailsBp)
    app.config['EXPLAIN_TEMPLATE_LOADING'] = True

    return app
