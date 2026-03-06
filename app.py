import os
from datetime import datetime, timezone

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template(
        'index.html',
        app_name='Flask Starter',
        server_time=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
    )


@app.route('/health')
def health():
    return {'status': 'ok'}, 200

@app.route('/api/hello', methods=['GET'])
def api_hello():
    return jsonify({'message': 'Hello from API!'})


if __name__ == '__main__':
    debug_mode = os.getenv('FLASK_DEBUG', '1') == '1'
    port = int(os.getenv('PORT', '5000'))
    app.run(host='127.0.0.1', port=port, debug=debug_mode)
