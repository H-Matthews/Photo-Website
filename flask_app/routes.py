from flask import Blueprint, render_template

main_blueprint = Blueprint('main', __name__)
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@main_blueprint.route('/')
@main_blueprint.route('/home')
def home():
    return render_template('index.html')

@main_blueprint.route('/about')
def about():
    return 'This is the About Page!'
    
@auth_blueprint.route('/login')
def login():
    return 'This is the LOGIN page'