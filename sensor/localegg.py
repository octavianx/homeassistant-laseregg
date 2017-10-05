# This Python file uses the following encoding: utf-8
#######################################################################
# localegg.py
# A native executable py version of laseregg fetch
#  USAGE:   localegg.py  [eggid]
#  And it returns all values which stored in  the laseregg server.
#
# author: octavianx, 2017-09-01
#

import requests
import yaml


DEFAULT_NAME = 'LaserEgg'
DEFAULT_POLL_INTERVAL = 5
DEFAULT_TIMEOUT = 5
DEFAULT_RETRY = 3


REQDOMAIN = "http://api-ios.origins-china.cn:8080"
REQPATH = "topdata"
REQAPI_GETNAME = "getTopByTimeId"
REQARGV = "timeId"

REQAPI_GETDETAIL = "getTopDetail"
REQARGVDETAIL= "id"


YAML_DEF_PLATFORM = 'platform'

def getAQI(eggID):
    print ("Probing devid : %s" % eggID)
    timeID = eggID
    reqbase = REQDOMAIN + '/' + REQPATH + '/' + REQAPI_GETNAME
    parameters = {  REQARGV : timeID }
    response  = requests.get(url=reqbase, params= parameters ,
                                timeout = DEFAULT_TIMEOUT )
    print (">>%s" % response.url)
    answer = response.json()
    response.raise_for_status()
    devid = answer['data']['id']
    reqbase2 = REQDOMAIN + '/' + REQPATH + '/' + REQAPI_GETDETAIL
    parameters2 = { REQARGVDETAIL : devid}
    res2 = requests.get(url=reqbase2, params= parameters2, 
                            timeout = DEFAULT_TIMEOUT)
    print (">:%s"  % res2.url)
    res2.raise_for_status()
    if ( res2.status_code == requests.codes.ok ) :
        answer2 = res2.json()
        list_up_dic_keyvalue(answer2) 
    else :
        print("Failed in get URL[%s]" % res2.url)

def search_all_dict(dict_a, targetkey, targetvalue) :
    if isinstance(dict_a,dict) : # #使用isinstance检测数据类型
        if  (targetkey in dict_a) & (dict_a[targetkey] == targetvalue) :
            getAQI( dict_a['devtimeid'])
#           for x in range(len(dict_a)) :
#                temp_key = list(dict_a.keys())[x]
#                temp_value = dict_a[temp_key]
#                print("%s : %s" %(temp_key,temp_value))
#                list_all_dict(temp_value, targetkey,targetvalue) #自我调用实现无限遍历

def list_up_dic_keyvalue(dict_a):
    if isinstance(dict_a, dict):
        for x in range(len(dict_a)):
            temp_key = list(dict_a.keys())[x]
            temp_value = dict_a[temp_key]
            print("%s : %s" %(temp_key,temp_value))


f = open('./laseregg.yaml')
content = yaml.load(f)
print ("1.Yaml file loaded")
for  x in range(len(content)):
    temp_dict  = content[x]
    search_all_dict(temp_dict, 'platform', 'laseregggen1')

