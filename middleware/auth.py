from . import login_manager
from models.Admin import admin
from flask_login import AnonymousUserMixin
login_manager.login_view = 'login.logins'
class Anonymous(AnonymousUserMixin):
    def __init__(self):
        self.username = 'Guest'
@login_manager.user_loader
def load_user(user_id):
    return admin.query.get(int(user_id))