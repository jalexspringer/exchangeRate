# Configuration pyexchange, mongodb and api keys

# Time in seconds between refreshes of the exchange rates.
REFRESH_RATE = 3600

# https://openexchangerates.org/signup/free
OPENEX_KEY = ''

# https://ipinfo.io/pricing``
IPINFO_KEY = ''

# Mongodb Information
MONGO_URI = 'mongodb://localhost:27017/'
DB_NAME = 'exchange_rates'
COLLECTION_NAME = 'exchange_rates'

# Do not change these settings. Use above variables.
MONGO_DICT = {
    'uri': MONGO_URI,
    'db': DB_NAME,
    'coll': COLLECTION_NAME}
JOBS = [
    {
        'id': 'exchange_job',
        'func': 'views:exchange_job',
        'args': (OPENEX_KEY, MONGO_DICT),
        'trigger': 'interval',
        'seconds': REFRESH_RATE
    }
]
SCHEDULER_API_ENABLED = True
