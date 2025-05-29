from flask import Flask, request, jsonify
import ast
import operator
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.USub: operator.neg
}

def eval_expr(expr):
    def _eval(node):
        if isinstance(node, ast.Constant):
            return node.n
        elif isinstance(node, ast.BinOp):
            return ALLOWED_OPERATORS[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):
            return ALLOWED_OPERATORS[type(node.op)](_eval(node.operand))
        else:
            raise ValueError("Invalid expression")
        
    parsed = ast.parse(expr.strip(), mode='eval')
    return _eval(parsed.body)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json()
    expr = data.get("expression", "")
    try:
        result = eval_expr(expr)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
