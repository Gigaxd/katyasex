<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Выбор фразы</title>
    <style>
        /* Основной стиль для страницы */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            color: #333;
            text-align: center;
            transition: background-color 0.5s ease;
        }

        h1 {
            font-size: 36px;
            color: #333;
            margin-bottom: 20px;
            animation: fadeIn 2s ease-out;
        }

        /* Стиль кнопки */
        button {
            font-size: 20px;
            padding: 15px 40px;
            cursor: pointer;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 8px;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        /* Эффект при наведении на кнопку */
        button:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 25px rgba(0, 0, 0, 0.2);
        }

        button:active {
            transform: translateY(2px);
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
        }

        /* Эффект появления фразы */
        #phrase {
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            padding: 10px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
            transition: opacity 1s ease;
            opacity: 0;
        }

        /* Анимация появления */
        .show {
            opacity: 1;
        }

        /* Анимация для заголовка */
        @keyframes fadeIn {
            0% {
                opacity: 0;
                transform: translateY(-50px);
            }
            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>
<body>
    <div>
        <h1>Надо срочно выбрать что-то одно</h1>

        <button onclick="getRandomPhrase()">Выбрать</button>

        <p id="phrase" class="fade"></p>
    </div>

    <script>
        function getRandomPhrase() {
            fetch('/random')
                .then(response => response.text())
                .then(phrase => {
                    const phraseElement = document.getElementById('phrase');
                    phraseElement.innerText = phrase;
                    phraseElement.classList.add('show');  // Анимация появления фразы
                });
        }
    </script>
</body>
</html>
