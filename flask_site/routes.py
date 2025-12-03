from flask import Blueprint

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
@main_blueprint.route('/home')
def home():
    return 'This is the Home Page!'

@main_blueprint.route('/about')
def about():
    return 'This is the About Page!'