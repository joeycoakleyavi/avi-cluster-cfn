from avi.sdk.avi_api import ApiSession
import logging
import os
import cfnresponse

def ready_check(nodes:dict, password:str, api_version:str):
    result = []
    for node, ip in nodes.items():
        try:
            api = ApiSession(ip['PrivateIp'], 'admin', password, tenant="admin", api_version=api_version)
            if api.get('cluster').status_code == 200:
                result.append(node)
        except:
            pass
    return True if len(result) == 3 else False

class NotReady(Exception):
    pass

def lambda_handler(event, context):
    print("Received Event:")
    print(event)
    avi_password = os.environ.get('AVIPASSWORD', '')
    api_version = os.environ.get('APIVERSION', '20.1.4')
    nodes = event['ResourceProperties']['Nodes']
    data = {
        "nodes": [
            {
                "name": "Ctl1",
                "ip": {
                    "addr": nodes['Ctl1']['PrivateIp'],
                    "type": "V4"
                },
                "password": avi_password
            },
            {
                "name": "Ctl2",
                "ip": {
                    "addr": nodes['Ctl2']['PrivateIp'],
                    "type": "V4"
                },
                "password": avi_password
            },
            {
                "name": "Ctl3",
                "ip": {
                    "addr": nodes['Ctl3']['PrivateIp'],
                    "type": "V4"
                },
                "password": avi_password
            }
        ]
    }

    try:
        print("Beginning Cluster Configuration")
        if ready_check(nodes, avi_password, api_version):
            print("Ready Check: Passed!")
            api = ApiSession(nodes['Ctl1']['PrivateIp'], 'admin', avi_password, tenant='admin', api_version=api_version)
            resp = api.put('cluster', data=data)
            if resp.status_code == 200:
                return(event)
            else:
                raise NotReady
        else:
            print("Ready Check Failed. Raising NotReady Exception")
            raise NotReady
        # cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
    except Exception:
        print("Caught an exception")
        # cfnresponse.send(event, context, cfnresponse.FAILED, responseData)
        raise NotReady