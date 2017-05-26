'''
Copyright (C) 2017 Alex Springer

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''


import os
import atexit

import webbrowser
from flask import Flask, render_template, flash, redirect, request, url_for
from werkzeug import secure_filename
from flask_apscheduler import APScheduler

import exchangedb
import pyopenex


def exchange_job(access_key, mongo_dict):
    ex = pyopenex.exchanger(access_key)
    exchangedb.dbUpdate(app.config['MONGO_DICT'], ex.all_rates_list)


app = Flask(__name__)
app.config.from_object('config')


@app.route("/", methods=['GET', 'POST'])
def index():
    uv = pyopenex.userVisit(app.config['OPENEX_KEY'])
    last_updated = exchangedb.lastUpdated(app.config['MONGO_DICT'])
    if request.method == 'POST':
        rate_list = exchangedb.getRatesDB(request.form['option'], app.config['MONGO_DICT'])
        currency_code=request.form['option']
        currency=uv.currency_dict[currency_code]
    else:
        rate_list = exchangedb.getRatesDB(uv.currency, app.config['MONGO_DICT'])
        currency_code=uv.currency,
        currency=uv.currency_long,

    return render_template("index.html",
                           currency_code=currency_code,
                           currency=currency,
                           pick_list=uv.currency_dict.keys(),
                           rate_list=rate_list,
                           updated=last_updated)


if __name__ == "__main__":
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    exchange_job(app.config['OPENEX_KEY'], app.config['MONGO_DICT'])
    app.run()
