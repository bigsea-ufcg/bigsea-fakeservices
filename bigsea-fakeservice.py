import random

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/authorization/run_application/', methods=['POST'])
def authorize_application_execution():
    return '{"success":true}', 200

@app.route('/optimizer/initial_cluster_size/', methods=['POST'])
def initial_cluster_size():
    data = request.get_json()

    if data['flavor'] != '' and data['application_type'] != '' and data['cluster_size'] > 0:
        return jsonify({'initial_size': data['cluster_size']}), 200
    else:
        return 'Access denied for the application %.', 401


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
