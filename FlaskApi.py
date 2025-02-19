from flask import Flask, request, jsonify
from Smain import generate_graph  
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_stock_graph', methods=['GET'])
def get_stock_graph():
    stock_name = request.args.get('stock_name')

    if not stock_name:
        return jsonify({"error": "Stock name is required"}), 400

    try:
        graph_json = generate_graph(stock_name)  
        return jsonify(graph_json)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return jsonify({"error": str(ve)}), 404
    except Exception as e:
        print(f"Internal server error: {e}")
        return jsonify({"error": "An internal error occurred. Please try again later."}), 500
    
if __name__ == "__main__":
    app.run(debug=True)
