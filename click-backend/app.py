from flask import Flask, logging
from flask_cors import CORS
from redis import Redis
from redis.exceptions import ConnectionError

app = Flask(__name__)
CORS(app)
cache = Redis(host='redis', port=6379)

log = logging.create_logger(app)


def get_clicks_from_redis():
    try:
        clicks = cache.get('clicks')
        return 0 if clicks is None else int(clicks)
    except ConnectionError as err:
        log.error(err)
        return 'Redis connection failed :('


def send_click_to_redis():
    try:
        cache.incr('clicks')
    except ConnectionError as err:
        log.error(err)
        return


@app.route('/clicks', methods=['GET'])
def get_clicks():
    clicks = get_clicks_from_redis()
    return str(clicks)


@app.route('/clicks', methods=['POST'])
def add_click():
    send_click_to_redis()
    return ''


if __name__ == '__main__':
    app.run()
