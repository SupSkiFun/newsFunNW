import requests

def _getHeadLineNews(apiKey , country , topic):
    '''Get Headlines from specified Country, optionally by topic.
    Arguments:
    apiKey - valid key
    country - two letter country code.  e.g., fr = France
    topic - specific topic to query
    '''
    msg = "Problem Accessing the below URL for Headlines:\n"
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country' : country ,
        'apiKey' : apiKey ,
        'q' : topic ,
    }
    try:
        ret = requests.get(url , params = params)
        ret.raise_for_status()
    except requests.exceptions.HTTPError as err:
        try:
            # newsapi.org returns a JSON error; return it if available.
            jrd = ret.json()
            return msg + str(err) + "\n" + jrd['code'] + " - " +jrd['message']
        except:
            return msg + str(err)
    else:
        jrd = ret.json()
        return jrd

def _printNews(news , number):
    '''Print retrieved Headlines

    Arguments:
    news - unmarshalled JSON
    number - amount of articles to return.  All by default.
    '''
    for x in news['articles'][:number]:
        print(x['title'])
        print(x['content'])
        print(x['url'])
        print("\n")

def getNews(apiKey , country = "us" , topic = None , number = None):
    '''Get Headlines for specific Topic from specified Country

    Arguments:
    apiKey - valid key from https://newsapi.org/register
    country - optional; Example: "fr" for France.  Defaults to "us".
    topic - optional; Specific topic to query
    number - optional; Headlines to return.  Defaults to all.
    '''

    news = _getHeadLineNews(apiKey , country , topic)

    if "Problem" in news:
        print(news)
    else:
        _printNews(news , number)