from flask import Blueprint, jsonify, request, current_app
from app.model.article import Article
from app.model.tag import Tag
from app.model.article_tag import ArticleTag
from app.model.database import db
from app.validator.schemas import add_schema
from app.validator.validator import validate_schema
from app.utils import log

bp = Blueprint("api", __name__, url_prefix="/api/v1")

DEFAULT_ARTICLE_LIMIT  = 5
DEFAULT_TAG_LIMIT      = 50
DEFAULT_ARTICLE_OFFSET = 0

'''
GET tag_articles
'''
@bp.route('/articles/tag/<string:tag_name>')
def show_tag_articles(tag_name):

    limit  = _get_article_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))
    current_app.logger.debug(tag_name)

    query = db.session.query(Article) \
        .join(ArticleTag, Tag) \
        .filter(Tag.name == tag_name) \

    articles = query.limit(limit).offset(offset)
    articles_count = query.count()

    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit,
        offset=offset
    )


'''
GET articles
'''
@bp.route('/articles')
def show_articles():
    """List articles in database. You may pass two arguments: limit - Number fo items to fetch, offset - Skip <offset> items from database result"""

    limit  = _get_article_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))

    articles = Article.query \
        .order_by(Article.created_at.desc(), Article.id.desc())\
        .offset(offset)\
        .limit(limit)
    current_app.logger.debug(articles)

    articles_count = Article.query.count()
    next_offset = min(limit + offset, articles_count)
    is_next = next_offset != articles_count

    return jsonify(
        articles=[a.serialize() for a in articles],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit,
        offset=offset
    )


'''
Get tags
'''
@bp.route('/tags')
def show_tags():
    limit  = _get_tag_limit(request.args.get('limit'))
    offset = _get_offset(request.args.get('offset'))

    tags = Tag.query \
        .order_by(Tag.id) \
        .offset(offset)\
        .limit(limit)

    tag_count = Article.query.count()
    next_offset = min(limit + offset, tag_count)
    is_next = next_offset != tag_count

    return jsonify(
        tags=[a.serialize() for a in tags],
        nextOffset=next_offset,
        isNext=is_next,
        limit=limit,
        offset=offset
    )


'''
Post add
'''
@bp.route('/articles/add', methods=['POST'])
@validate_schema(add_schema)
def add():
    log.debug(request)
    current_app.logger.debug(request.json)
    article_id = request.json['article_id']
    tag_names  = request.json['tag_names']

    article = Article.query\
        .filter(Article.id == article_id)\
        .first()

    current_app.logger.debug(article)

    return jsonify(
        article.serialize()
    )

'''
Methods
'''

def _get_article_limit(l):
    return int(l) if l is not None else DEFAULT_ARTICLE_LIMIT

def _get_tag_limit(l):
    return int(l) if l is not None else DEFAULT_TAG_LIMIT

def _get_offset(o):
    return int(o) if o is not None else DEFAULT_ARTICLE_OFFSET
