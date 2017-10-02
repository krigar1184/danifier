import os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash


app = Flask(__name__)
app.config.from_object(__name__)
# app.config.from_envvar('DANIFIER_SETTINGS', silent=False)
app.config.update({
    'SECRET_KEY': 'sdfgHOI*99jioplk80&y'
})


from app import views
