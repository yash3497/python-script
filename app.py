from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/authentication', methods=['GET'])
def authentication():
    # You can implement any logic here to determine the boolean value
    result = False  # Change this value based on your requirement
    
    # Response in JSON format
    response = {'status': result}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
