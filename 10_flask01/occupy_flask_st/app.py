#!/usr/bin/env python3
from flask import Flask
from standard import get_random_occupations
app = Flask(__name__)

occupations = []
@app.route("/")
def index():
    return_html = ''
    jobs = ''
    return_html += "<h1>Team AutoKAD: Andrew Jiang, Dean Carey"
    return_html += ", Carlos 'Karl' Hernandez</h1><br>"
    occupations.append(get_random_occupations()[1])
    return_html += "<ul><li><h4>" + "</h4></li><li><h4>".join(occupations)
    return_html += "</h4></li></ul><br>List of Occupations:<br>"
    for job in get_random_occupations()[0]:
        jobs += job + "<br>"
    return_html += jobs
    return return_html


if __name__ == '__main__':
    app.run(debug=True)
