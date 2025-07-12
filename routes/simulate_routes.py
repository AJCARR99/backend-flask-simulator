from flask import Blueprint, request, jsonify
import numpy as np
import matplotlib.pyplot as plt
import io
import base64

simulate_bp = Blueprint('simulate', __name__)

@simulate_bp.route('/neuron', methods=['POST'])
def simulate_neuron():
    data = request.get_json()
    inputs = np.array(data.get("inputs", [0.0, 0.0]))
    weights = np.array(data.get("weights", [1.0, 1.0]))
    bias = data.get("bias", 0.0)

    output = np.dot(inputs, weights) + bias

    fig, ax = plt.subplots()
    ax.bar(["Input 1", "Input 2"], inputs)
    ax.set_title("Neuron Inputs")

    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    return jsonify({
        "output": float(output),
        "image": image_base64
    })