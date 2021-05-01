from flask import Flask, jsonify, request
import service1
import service2
import service3
import service4
import service5
import service6

app = Flask(__name__) #se crea el obj


@app.route('/api/characterization/', methods=['POST'])
def execCharacterization():
    request_data = request.get_json()
    return jsonify(service1.exec(request_data['sequences'], request_data['time']))

@app.route('/api/classification/', methods=['POST'])
def execClassification():
    request_data = request.get_json()
    return jsonify(service2.exec(request_data['sequences'], request_data['time']))

@app.route('/api/alignment/', methods=['POST'])
def execAlignment():
    request_data = request.get_json()
    return jsonify(service3.exec(request_data['sequences'], request_data['time']))

@app.route('/api/frequency/', methods=['POST'])
def execFrequency():    
    request_data = request.get_json()
    return jsonify(service4.exec(request_data['sequences'], request_data['time'], request_data['option']))

@app.route('/api/encoding/', methods=['POST'])
def execEncoding():    
    request_data = request.get_json()
    return jsonify(service5.exec(request_data['sequences'], request_data['time'], request_data['option']))

@app.route('/api/training/', methods=['POST'])
def execTraining():
    request_data = request.get_json()
    return jsonify(service6.exec(request_data['time']))


if (__name__ == "__main__"):#si se esta ejecutando como archivo principal
    app.run(debug=True, port='4000') #con debug el servidor se reiniciar al hacer cambios

