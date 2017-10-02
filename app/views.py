from .app import app
from flask import render_template, request
from app.forms import DanifyForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DanifyForm(request.data)

    if request.method == 'POST':
        return render_template('result.html', result=form.text)

    return render_template('form.html', form=form)
