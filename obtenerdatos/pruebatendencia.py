import requests

from pytrends.request import TrendReq
import pandas as pd

pytrend = TrendReq(hl='en-US', tz=360)
kw_list = ["pizza"]
pytrend.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
iot = pytrend.interest_over_time()
iot.plot()