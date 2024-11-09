# app.py
from flask import Flask, request, jsonify
from Smain import generate_stock_graph

app = Flask(__name__)

@app.route('/get_stock_graph', methods=['GET'])
def get_stock_graph():
    stock_name = request.args.get('stock_name')

    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400

    try:
        # Generate the graph JSON
        graph_json = generate_stock_graph(stock_name)
        return jsonify(graph_json)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
