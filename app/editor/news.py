import json
from flask import Blueprint, request, render_template
from app.model.article import Article
from app.model.tag import Tag
from app.model.article_tag import ArticleTag
from app.model.database import db
from app.utils import log
from app import log

import requests

bp = Blueprint('news', __name__, url_prefix='/editor', template_folder='templates', static_folder='static')

@bp.route('/news')
def show_news():
    response = requests.get('http://127.0.0.1:5000/api/v1/articles?limit=60')
    articles = response.json()
    for article in articles['articles']:
        log.debug(article['title'])
    return render_template('index.html')
