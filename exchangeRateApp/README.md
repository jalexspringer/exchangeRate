# Exchange rate python API

## Tools:
- `pip install -r requirements.txt` to install dependencies.
- run `python setup.py install` in the pyopenex folder (package accompanies this app)
- Mongodb - simply run the mongod daemon on the localhost and leave the config as is. Or specify the URI to the running mongo instance in the config.py
- Exchange rates from free plan at openexchangerates.org API. Note that the free plan only updates every hour. Paid plans offer every minute.
- Ip info from ipinfo.io API. The free plan is limited to 1000 queries a month

I have included test API and app keys in the config.py. Please create accounts and update these with your own - the keys will expire in 2 weeks.

### To run the app:
- Install the dependencies, ensure mongodb is running, then run `python views.py` from the exchangeRate folder.
- This will create a new mongodb database and collection with the most recent exchange rates from openexchange.com. If the database exists it will update, and the updates will run hourly from there.

- Navigate to localhost:5000 to see the app. This will auto-detect your country using your IP (ipinfo.io API) and default to the country's primary currency. Select the desired currency from the drop down to change the view.

## Notes
- All rates outside of USD are derived from the USD exchange rate. The free API plan at openexchangerates.org does not allow the base currency to be changed. I spot checked the derived rates and they are quite accurate - but there may be small disrepancies here and there, especially in volatile currencies.
- The DB interaction tools are in the exchangedb.py file in the exchangeRateApp folder. These are the functions to call when anything is read to or from the DB
- The pyopenex package simply gets USD rates, converts them, and makes both a list of dictionaries (for mongo updating) and a full rate list dictionary available.
