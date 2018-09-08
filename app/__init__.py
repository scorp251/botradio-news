from time import strftime
from flask import Flask, jsonify, request, redirect, url_for
from app.utils import log, setup_logger
from app.utils import ErrorGeneralOK
from app.model.database import setup_db
from app.api import article
from app.editor import news

log.info('Initializing application.')

app = Flask(__name__)

app.secret_key = 'zaguJooYeeph7uo3iezaew9ae'
app.config['SESSION_TYPE'] = 'filesystem'
app.config['JSON_AS_ASCII'] = False

setup_db(app)
setup_logger(app)

app.register_blueprint(article.bp)
app.register_blueprint(news.bp)

log.info('Application started')

@app.route('/')
def index():
    """Main page"""
    return ErrorGeneralOK("This is BotRadio News API")

@app.route('/help', methods = ['GET'])
def help():
    """Print available functions."""
    func_list = {}
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            func_list[rule.rule] = app.view_functions[rule.endpoint].__doc__
    return jsonify(func_list)

@app.after_request
def after_request(response):
    """ Logging after every request. """
    log.info('%s - %s %s "%s" %s "%s"',
          request.remote_addr,
          request.method,
          request.full_path,
          response.status,
          response.headers['Content-Length'],
          request.user_agent)
    return response
