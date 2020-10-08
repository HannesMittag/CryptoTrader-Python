#
# MODULE by @lyricsroot
# LICENSE: private; no external usage
#

""" 'CryptoTrader' KRAKEN_STATS module.

This module is responsible for plotting all data provided by the KRAKEN_API.


    functions:
        plotInterval: none, plots given set of data in given interval

"""

##imports
import matplotlib.pyplot as plt

##functions
def plotInterval(time = [1], data=[]):
    plt.ylabel('PRICE')
    plt.xlabel('TIME')
    plt.plot(time, data)
    plt.show()
