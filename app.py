from flask import Flask, render_template
app = Flask(__name__)

HOST = '0.0.0.0'
HTTP_PORT = 80

# Index route
@app.route("/")
def index():
	data = {}
	return render_template('index.html', **data)

if __name__ == "__main__":
	app.run(debug=True, host=HOST, port=HTTP_PORT)
