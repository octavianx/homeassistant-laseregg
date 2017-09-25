
import requests





DEFAULT_NAME = 'LaserEgg'
DEFAULT_POLL_INTERVAL = 5
DEFAULT_TIMEOUT = 0
DEFAULT_RETRY = 3


REQDOMAIN = "http://api-ios.origins-china.cn:8080"
REQPATH = "topdata"

REQAPI_GETNAME = "getTopByTimeId"
REQARGV = "timeId"

REQAPI_GETDETAIL = "getTopDetail"
REQARGVDETAIL= "id"



def getAQI(eggID):

    timeID = eggID
    reqbase = REQDOMAIN + '/' + REQPATH + '/' + REQAPI_GETNAME


    parameters = {  REQARGV : timeID }
    response  = requests.get(url=reqbase, params= parameters )
    print ("requesting following base:" , response.url)
    answer = response.json()
    

    prints =     

    devid = answer['data']['id']


    reqbase2 = REQDOMAIN + '/' + REQPATH + '/' + REQAPI_GETDETAIL
    parameters2 = { REQARGVDETAIL : devid}

    res2 = requests.get(url=reqbase2, params= parameters2)
    print ("requesting following base:" , res2.url)
    answer2 = res2.json()

    print("PM2.5 count ", answer2['pm2_5_count'])
    print("PM2.5 Idx ",   answer2['pm2_5'])
    print("Location: ", answer2['cityname'])


getAQI(DCONFIG_LASEREGG_ID)
