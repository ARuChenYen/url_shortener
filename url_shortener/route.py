from flask import Blueprint, render_template, request, redirect
from .extensions import db
from .model import *

short = Blueprint('short', __name__)

@short.route('/<short_url>')
def redirect_to_url(short_url):
    original = Url.query.filter_by(short_url=short_url).first_or_404()
    return redirect(original.original_url)

@short.route('/add_url', methods=['POST'])
def add_url():
    original_url = request.form['original_url']
    url = Url(original_url=original_url)
    db.session.add(url)
    db.session.commit()

    return render_template('url_added.html',
        new_url=url.short_url, original_url=url.original_url)

@short.route('/')
def index():
    return render_template('index.html')

@short.errorhandler(404)
def page_not_found(e):
    return '<h1>Short Link is not valid</h1>', 404