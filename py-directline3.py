import requests
import json
import time

SECRET = "Bearer hDcYliwT7Uw.cwA.EhQ.uHC2fujOPSF2hwwqSpcVjlfLmCqFeY5qhJd2bm3dJ9U"
START_CONVERSATIONS_URL = "https://directline.botframework.com/v3/directline/conversations"
ACTIVITIES_URL = "https://directline.botframework.com//v3/directline/conversations/%s/activities"


#r = requests.Request('POST', url, headers)
#prepared = r.prepare()
#pretty_print_POST(prepared)

#s = requests.Session()
#response = s.send(prepared)

#print response
#print response.text

def pretty_print_POST(req):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".

    However pay attention at the formatting used in 
    this function because it is programmed to be pretty 
    printed and may differ from the actual request.
    """
    print('{}\n{}\n{}\n\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))

def start_conversation():
    headers = {
        'Authorization': SECRET, 
        'Content-Type': 'application/json'
    }
    r = requests.request('POST', START_CONVERSATIONS_URL, headers=headers)
    return json.loads(r.text)


auth = start_conversation()
print json.dumps(auth,indent=4)
print "-" * 50

headers = {
    'Authorization': ("Bearer %s" % auth["token"]),
    'Content-Type': 'application/json'
}

r = requests.request('POST', (ACTIVITIES_URL % auth["conversationId"]), headers=headers, json={"type":"message", "from": {"id":"user"}, "text":"all"})
print json.loads(r.text)
print "-" * 50

time.sleep(10)

r = requests.request('GET', (ACTIVITIES_URL % auth['conversationId']), headers=headers)
print json.dumps(json.loads(r.text), indent=4)
print "-" * 50