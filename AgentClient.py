import requests
from rpcclient import jira_options
from rpcclient import jira
from rpcclient import issues_in_project
from rpcclient import Testflourl
from rpcclient import xmlrpchost
from rpcclient import rpcserver
from sikulifunction import Sikulifunction
def JIRA_Connection():
    for issue in issues_in_project:
        if(issue.raw['fields']['customfield_11000'] == None):
          print(issue)
          print("No Test Step")
        else:
         print(rpcserver.system.listMethods())
         for index , step in enumerate(issue.raw['fields']['customfield_11000']['stepsRows']):
          PassTcStep = {
              "issueId": issue.id,
              "rowIndex": index,
              "status": "Pass"
          }
          FailTcStep = {
              "issueId": issue.id,
              "rowIndex": index,
              "status": "Fail"
          }
          print(index)
          if "find" in step['cells'][0] :
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          elif "wait" in step['cells'][0]:
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          elif "click" in step['cells'][0] :
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          elif "typecustom" in step['cells'][0] :
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          elif "SearchBarRegionfunction" in step['cells'][0]:
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          elif "Key.ENTER" in step['cells'][0]:
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          elif "validatetext" in step['cells'][0]:
             Sikulifunction(step,PassTcStep,FailTcStep,step['cells'][0])
          else:
              print("there are no function in sikuli")

def main():
    JIRA_Connection()

if __name__ == "__main__":
    main()







