import requests
from rpcclient import jira_options
from rpcclient import jira
from rpcclient import issues_in_project
from rpcclient import Testflourl
from rpcclient import xmlrpchost
from rpcclient import rpcserver

def WhenPass(PassTcStep,retval):
    r = requests.put(Testflourl, json=PassTcStep, auth=('admin', 'admin'))
    print(retval, r)

def WhenFail(FailTcStep,retval):
    r = requests.put(Testflourl, json=FailTcStep, auth=('admin', 'admin'))
    print(retval, r)

def Sikulifunction(step,PassTcStep,FailTcStep,functiontype):
    if functiontype == 'find':
        try:
            retval = rpcserver.myfindfunction(str(step['cells'][1]))
            if retval in "OK":
                WhenPass(PassTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)
    if functiontype == 'wait':
        try:
            retval = rpcserver.mywaitfunction(str(step['cells'][1]))
            if retval in "OK":
                WhenPass(PassTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)
    if functiontype == 'click':
        try:
            retval = rpcserver.myclickfunction(str(step['cells'][1]))
            if retval in "OK":
                WhenPass(PassTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)
    if functiontype == 'typecustom':
        try:
            retval = rpcserver.mytypecustomfunction(str(step['cells'][1]))
            if retval in "OK":
                WhenPass(PassTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)
    if functiontype == 'SearchBarRegionfunction':
        try:
            retval = rpcserver.mySearchBarRegionfunction()
            if retval != None:
                WhenPass(PassTcStep,retval)
            else:
                WhenFail(FailTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)
    if functiontype == 'validatetext':
        try:
            retval = rpcserver.validatetext(str(step['cells'][1]))
            if retval in "OK":
                WhenPass(PassTcStep,retval)
            else:
                WhenFail(FailTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)
    if functiontype == 'Key.ENTER':
        try:
            retval = rpcserver.enter()
            if retval in "OK":
                WhenPass(PassTcStep,retval)
        except:
            WhenFail(FailTcStep,retval)