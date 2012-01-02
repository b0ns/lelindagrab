'''
Created on Jan 2, 2012

@author: bons
'''


#!/usr/bin/python
import urllib
import time
from datetime import datetime,timedelta



def retrieveImages( period,hour, path):
    
    thisdate = time.strftime("%Y/%m/%d", period.timetuple())
    url = "http://www.webcam-ski.com/archives/" + thisdate +"/"+ hour + "/lindarets/lindarets_MEGA.jpg"
    print url
    name = time.strftime("%Y_%m_%d", period.timetuple())+hour
    print name
    urllib.urlretrieve( url, path+name)
  

def daterange(start_date, end_date):
    for n in range((end_date - start_date).days):
        yield start_date + timedelta(n)

if __name__ == '__main__':
    h_list = ["1000","1400","1600"]
    start_date = datetime(2011,12,01)
    end_date = datetime(2011,12,31)
    path = "./pics/" #The path where you want to store the downloaded images
    day_count = (end_date - start_date).days + 1
    for date in daterange(start_date, end_date):
        for hour in h_list:
            retrieveImages( date, hour, path )
     


