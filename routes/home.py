from router import app


@app.route("/")
def home():
    return "Now I am become Death, the Destroyer of Worlds"
