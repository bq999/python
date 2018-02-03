#JSON data ---

import urllib.request # instead of urllib2 like in Python 2.7
import json


def printResults(data):

  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  


# now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print (theJSON["metadata"]["title"])

def main():
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1/0summary/2..5_day.geojson"


  

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print (webUrl.getcode())
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    data = data.decode("utf-8") # in Python 3.x we need to explicitly decode the response to a string
    # print out our customized results
    printResults(data)
  else:
    print ("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))


if __name__ == "__main__":
    printResults()
