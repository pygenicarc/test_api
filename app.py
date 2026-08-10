import requests
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/posts')
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return jsonify({
        "data": response.json(),
        "status": "successfully",
        "status_code": 200
    })

@app.route('/comments')
def get_comments():
    url = "https://jsonplaceholder.typicode.com/comments"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return jsonify({
        "data": response.json(),
        "status": "successfully",
        "status_code": 200
    })

@app.route('/albums')
def get_albums():
    url = "https://jsonplaceholder.typicode.com/albums"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    return jsonify({
        "data": response.json(),
        "status": "success",
        "status_code": 200
    })

if __name__ == '__main__':
    app.run(debug=True)

