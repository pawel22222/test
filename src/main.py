from sanic import Sanic
from sanic.response import json

app = Sanic("MyApp")


@app.route("/")
async def root(request):
    return json({"message": "Witaj w Sanic!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
