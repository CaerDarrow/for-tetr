__author__ = 'Ruslan Akhmetshin'

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('test.html')


@app.route('/appearance', methods=['POST'])
def appearance():
    total_str = request.form['lesson'] + ',' + request.form['tutor'] + ',' + request.form['pupil']
    list1 = total_str.split(',')
    events = []
    for i in range(len(list1)):
        events.append((int(list1[i]), 1 - 2*(i%2))) 
    events.sort()
    counter = 0
    start = -1
    answer = 0
    for t in events:
        counter += t[1]
        if counter == 3: 
            start = t[0]
        if counter == 2 and start > 0: 
            answer += t[0] - start
            start = -1
    return 'Total time is %s seconds <br/> <a href="/">Back Home</a>' % (answer)


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 3500)