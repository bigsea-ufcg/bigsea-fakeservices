import ConfigParser

from flask import Flask, request, jsonify

app = Flask(__name__)

conf = ConfigParser.RawConfigParser()
conf.read("fakeservices.cfg")
cluster_size = conf.getint("defaults", "cluster_size")

@app.route('/authorization/run_application/', methods=['POST'])
def authorize_application_execution():
    return '{"success":true}', 200

@app.route('/optimizer/get_cluster_size', methods=['GET'])
def initial_cluster_size():
    result = {"cluster_size":cluster_size}
    return jsonify(result), 200

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
