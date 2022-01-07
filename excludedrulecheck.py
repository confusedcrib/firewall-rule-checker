import boto3
import json

fms_client = boto3.client("fms")

class color:
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def listpolicies():
    policylist = []
    policyname = []
    policydict = fms_client.list_policies()
    policies = policydict['PolicyList']
    for x in policies:
        policylist.append(x['PolicyId'])
        policyname.append(x['PolicyName'])
    policydict = {}
    for key in policylist:
        for value in policyname:
            policydict[key] = value
            policyname.remove(value)
    return policydict
    
def getpolicydetails(policydict):
    for key, value in policydict.items():
        print('\n' + color.BOLD + color.UNDERLINE + color.GREEN + value + color.END + "\n")
        response = json.dumps(fms_client.get_policy(
        PolicyId = key
        ))
        format_response = json.loads(response)
        RuleGroups = format_response['Policy']['SecurityServicePolicyData']['ManagedServiceData']
        format_RuleGroup = json.loads(RuleGroups)
        details = format_RuleGroup["preProcessRuleGroups"]
        for x in details:
            if x['managedRuleGroupIdentifier'] is not None:
                RuleGroupName = x['managedRuleGroupIdentifier']['managedRuleGroupName']
                RuleGroupExclusions = x['excludeRules']
                print('\n' + color.YELLOW + RuleGroupName + color.END + " has the below exceptions:")
                if bool(RuleGroupExclusions):
                    for x in RuleGroupExclusions:
                        print(color.RED + x['name'] + color.END)
                else:
                    print('No Exceptions')

policydict = listpolicies()

getpolicydetails(policydict)
