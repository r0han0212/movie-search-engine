from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, template_folder='template')

OMDB_API_KEY = "d1549122"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search_movie", methods=["GET"])
def search_movie():
    title = request.args.get("title")
    if not title:
        return jsonify({"error": "Title is required"}), 400

    url = f"http://www.omdbapi.com/?i=tt3896198&apikey=d1549122&t={title}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get("Response") == "True":
            return jsonify(data)
        else:
            return jsonify({"error": data.get("Error")}), 404
    else:
        return jsonify({"error": "Failed to connect to OMDb API"}), 500

if __name__ == "__main__":
    app.run(debug=True)
