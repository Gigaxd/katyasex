from flask import Flask, render_template
import random
import os

app = Flask(__name__)

phrases = [
    "Скинь фоточки с бутиками",
    "Покажи попочку",
    "Дай засунуть носик в пупочек",
    "Сядь на личико",
    "Срочно нужно лизнуть подмышечку",
    "Отправь поцелуйчик в голосовом"
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_phrase():
    return random.choice(phrases)

if __name__ == "__main__":
    # Убедитесь, что приложение слушает нужный порт
    port = int(os.environ.get("PORT", 5000))  # Render передает переменную окружения PORT
    app.run(debug=True, host="0.0.0.0", port=port)
