from .app import app
from flask import render_template, request
from app.forms import DanifyForm
from app.core import danify


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DanifyForm(request.data)
    form.validate_on_submit()

    if request.method == 'POST':
        return render_template('result.html', result=danify(form.text))

    return render_template('form.html', form=form)
