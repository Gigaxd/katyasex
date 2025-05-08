from flask import Flask, render_template
import random
import os  # импортируем os для доступа к переменным окружения

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
    # Получаем порт из переменной окружения, если он не задан, используем 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
