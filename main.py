from routes.router import app

from dotenv import load_dotenv

load_dotenv(".env")

app.run(debug=True)
