from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route('/', methods=['GET','POST'])
def index():
    name = request.form.get('name') if request.method == 'POST' else ''
    return render_template('index.html', name=name)

