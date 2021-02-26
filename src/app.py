from flask import Flask
from flask import request
app = Flask(__name__)


from flask import jsonify
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]
@app.route('/todos')
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(original_string)
    print("Incoming request with the following body", request_body)
    return 'Response for the POST todo'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
