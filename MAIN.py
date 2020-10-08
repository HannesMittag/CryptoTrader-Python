#
# MODULE by @lyricsroot
# LICENSE: private; no external usage
#

""" 'CryptoTrader' MAIN module.

This module is the main script of the Trader Bot, managing the whole core procedure
of the program.

    Objects:
        caller: KRAKEN_API_CALLER instance, managing all API calls and responding with json

"""

##imports
from KRAKEN_API_CALLER import KRAKEN_API_CALLER
import KRAKEN_STATS
import json

##variables
caller = KRAKEN_API_CALLER()

##script
#testing connection
if caller.test():
    #fetching OHLC-data from server
    json_res = caller.getOHLC('XXBTZEUR')
    #transforming data- dict to list
    data = json_res['result']['XXBTZEUR']
    time = []
    average_data = []
    for x in data:
        average_data.append((float(x[2])+float(x[3]))/float(2))
        time.append(x[0])
    #create plot
    KRAKEN_STATS.plotInterval(time=time, data=average_data)
