# Импорт необходимых библиотек
import os
import json

from flask import Flask, render_template, url_for, request

from fixer_api_functions import get_latest_rates

# Инициализация Flask
app = Flask(__name__)

# Оъявление переменных
site_url = 'https://l1nt3x-currencyconverter.herokuapp.com/'
fcurrencies = open('.info/currencies.json', encoding='UTF-8')
currencies = json.load(fcurrencies)

# Root
@app.route('/en', methods=['POST', 'GET'])
def index():
    # Получаем пути к ресурсам
    site_icon_path = url_for('static', filename='img/icon-en.png')
    css_path = url_for('static', filename='css/main.css')
    icon_path = url_for('static', filename='img/icon.png')
    # Рендерим страницу
    if request.method == 'GET':
        return render_template('main-en.html', icon_path=icon_path, site_icon_path=site_icon_path,
                               site_url=site_url + 'en', css_path=css_path)
    elif request.method == 'POST':
        amount = float(request.form['amount'])
        currency1 = request.form['currencies1']
        if ' - ' in currency1:
            currency1_ABC, currency1_name = currency1.split(' - ')
        else:
            currency1_ABC = currency1
            currency1_name = currencies[currency1][0]
        currency2 = request.form['currencies2']
        if ' - ' in currency2:
            currency2_ABC, currency2_name = currency2.split(' - ')
        else:
            currency2_ABC = currency2
            currency2_name = currencies[currency2][0]
        rates = get_latest_rates(base=currency1_ABC, symbols=currency2_ABC)['rates']
        converted_value = float(rates[currency2_ABC]) * amount
        converted_text = f'{amount} {currency1_name} = {converted_value} {currency2_name}'
        return render_template('main-en-converted.html', icon_path=icon_path, site_icon_path=site_icon_path,
                               site_url=site_url + 'en', css_path=css_path, amount=amount, currency1=currency1,
                               currency2=currency2, converted_text=converted_text)


# Корень
@app.route('/ru', methods=['POST', 'GET'])
def index_ru():
    # Получаем пути к ресурсам
    site_icon_path = url_for('static', filename='img/icon-ua-ru.png')
    css_path = url_for('static', filename='css/main.css')
    icon_path = url_for('static', filename='img/icon.png')
    # Рендерим страницу
    if request.method == 'GET':
        return render_template('main-ru.html', icon_path=icon_path, site_icon_path=site_icon_path,
                               site_url=site_url + 'ru', css_path=css_path)
    elif request.method == 'POST':
        amount = float(request.form['amount'])
        currency1 = request.form['currencies1']
        if ' - ' in currency1:
            currency1_ABC, currency1_name = currency1.split(' - ')
        else:
            currency1_ABC = currency1
            currency1_name = currencies[currency1][0]
        currency2 = request.form['currencies2']
        if ' - ' in currency2:
            currency2_ABC, currency2_name = currency2.split(' - ')
        else:
            currency2_ABC = currency2
            currency2_name = currencies[currency2][0]
        rates = get_latest_rates(base=currency1_ABC, symbols=currency2_ABC)['rates']
        converted_value = float(rates[currency2_ABC]) * amount
        converted_text = f'{amount} {currency1_name} = {converted_value} {currency2_name}'
        return render_template('main-ru-converted.html', icon_path=icon_path, site_icon_path=site_icon_path,
                               site_url=site_url + 'ru', css_path=css_path, amount=amount, currency1=currency1,
                               currency2=currency2, converted_text=converted_text)


# Корінь
@app.route('/', methods=['POST', 'GET'])
def index_ua():
    # Получаем пути к ресурсам
    site_icon_path = url_for('static', filename='img/icon-ua-ru.png')
    css_path = url_for('static', filename='css/main.css')
    icon_path = url_for('static', filename='img/icon.png')
    # Рендерим страницу
    if request.method == 'GET':
        return render_template('main-ua.html', icon_path=icon_path, site_icon_path=site_icon_path,
                               site_url=site_url, css_path=css_path)
    elif request.method == 'POST':
        amount = float(request.form['amount'])
        currency1 = request.form['currencies1']
        if ' - ' in currency1:
            currency1_ABC, currency1_name = currency1.split(' - ')
        else:
            currency1_ABC = currency1
            currency1_name = currencies[currency1][0]
        currency2 = request.form['currencies2']
        if ' - ' in currency2:
            currency2_ABC, currency2_name = currency2.split(' - ')
        else:
            currency2_ABC = currency2
            currency2_name = currencies[currency2][0]
        rates = get_latest_rates(base=currency1_ABC, symbols=currency2_ABC)['rates']
        converted_value = float(rates[currency2_ABC]) * amount
        converted_text = f'{amount} {currency1_name} = {converted_value} {currency2_name}'
        return render_template('main-ua-converted.html', icon_path=icon_path, site_icon_path=site_icon_path,
                               site_url=site_url, css_path=css_path, amount=amount, currency1=currency1,
                               currency2=currency2, converted_text=converted_text)


# Стартуем сайт
def start_server():
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


# Стартуем процесс
if __name__ == '__main__':
    start_server()
