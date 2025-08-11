from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')

def hello():
    return jsonify({
        'message' : 'hello_world - GitHub Action'
    }) 


if __name__ == "__main__":

    app.run(host="0.0.0.0")


# '/api/v1/details'
# '/api/v1/healthz'