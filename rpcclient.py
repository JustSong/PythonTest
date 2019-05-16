from jira.client import JIRA
import xmlrpc.client
jira_options = {'server': 'http://localhost:8080/jira'}
jira = JIRA(options=jira_options, basic_auth=("admin", "admin"))
issues_in_project = jira.search_issues('labels = sikuli')
Testflourl = 'http://localhost:8080/jira/rest/tms/1.0/steps/status'
xmlrpchost = "http://127.0.0.1:1337"
rpcserver = xmlrpc.client.ServerProxy(xmlrpchost)

