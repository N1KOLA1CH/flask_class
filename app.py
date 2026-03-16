from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def training(prof):
    param = {}
    if any(i in prof for i in ('инженер', 'строитель')):
        param["title"] = 'Инженерные тренажеры'
        param["img"] = "ing.png"
    else:
        param["title"] = 'Научные симуляторы'
        param["img"] = "sci.png"
    return render_template('training.html', **param)


@app.route('/index')
def odd_even():
    param = {}
    param["title"] = 'Заготовка'
    return render_template('base.html', **param)


@app.route('/list_prof/<lst>')
def list_prof(lst):
    param = {}

    param["lst"] = lst
    param["title"] = 'Список профессий'
    param['professions'] = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                            'инженер по терраформированию', 'климатолог',
                            'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                            'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                            'штурман', 'пилот дронов']
    return render_template('list_prof.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
