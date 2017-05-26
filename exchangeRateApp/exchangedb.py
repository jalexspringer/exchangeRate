import pymongo

def dbUpdate(mongo_dict, rates_list):
    import datetime
    # Create/update the database with the most recent rates
    coll = exchangeDBConnect(mongo_dict)
    try:
        coll.insert_many(rates_list)
    except:
        for c in rates_list:
            coll.replace_one({'_id': c['_id']}, c, True)
    try:
        coll.insert_one({'_id': 'lastupdated'}, {'timestamp': datetime.datetime.utcnow()})
    except:
        coll.replace_one({'_id': 'lastupdated'}, {'timestamp': datetime.datetime.utcnow()})

    print('DB Updated {}'.format(datetime.datetime.now()))


def exchangeDBConnect(mongo_dict):
    client = pymongo.MongoClient(mongo_dict['uri'])
    db = client[mongo_dict['db']]
    coll = db[mongo_dict['coll']]
    return coll


def getRatesDB(currency, mongo_dict):
    # Returns a dictionary of conversion rates for the given currency code
    coll = exchangeDBConnect(mongo_dict)
    return(coll.find_one({'_id': currency}))


def lastUpdated(mongo_dict):
    # Returns a dictionary of conversion rates for the given currency code
    coll = exchangeDBConnect(mongo_dict)
    time = coll.find_one({'_id': 'lastupdated'})
    try:
        return time['timestamp']
    except KeyError:
        return str(datetime.datetime.utcnow())


def test_ips(ipinfo_key, mongo_dict):
    # Requires ipinfo.io api key and uri to the running mongodb
    test_ip_nigeria = '105.112.43.249'
    test_ip_zimbabwe = '41.57.79.249'
    test_ip_china = '1.0.63.1'
    test_ips = [test_ip_nigeria, test_ip_zimbabwe, test_ip_china]
    for ip in test_ips:
        uv = userVisit(ipinfo_key, ip)
        print(uv.ip)
        print(getRates(uv.currency, mongo_uri)['_id'])
