from flask import Flask
import random

app = Flask(__name__)
rando = random.randint(1, 9)


def text_decorator(function):
    def wrapper(**kwargs):
        number = kwargs["number"]
        text = function(number)
        if number == rando:
            return f"<h1 style='color:green;'>{text}</h1> <img src='https://media.giphy.com/media/Px4VZw6PYCZFKcps0U" \
                   f"/giphy.gif' width='200'> "
        elif number < rando:
            return f"<h2 style='color:green;'>{text}</h2>"
        else:
            return f"<h2 style='color:red;'>{text}</h2>"

    return wrapper


@app.route("/")
def hello():
    return "Type number between 1-9 in URL for higher/lower game"


@app.route("/<int:number>")
@text_decorator
def higher_lower_game(number):
    if number == rando:
        return f"correct"
    elif number < rando:
        return f"too low"
    else:
        return f"too high"


if __name__ == "__main__":
    app.run(debug=True)
