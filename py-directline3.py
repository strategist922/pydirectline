import json
import time
import requests

SECRET = "Bearer hDcYliwT7Uw.cwA.EhQ.uHC2fujOPSF2hwwqSpcVjlfLmCqFeY5qhJd2bm3dJ9U"

BASE_URL = "https://directline.botframework.com"
START_CONVERSATION = "/v3/directline/conversations" #start a new conversation
SEND_ACTIVITY = "/v3/directline/conversations/%s/activities"
GET_ACTIVITIES = "/v3/directline/conversations/%s/activities"

def start_conversation():
    """
    Starts a new conversation.
    """
    headers = {
        'Authorization': SECRET,
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', BASE_URL + START_CONVERSATION, headers=headers)
    return json.loads(response.text)

def send_activitiy(conversation, activity):
    """
    Send an activity.
    """
    headers = {
        'Authorization': ("Bearer %s" % conversation["token"]),
        'Content-Type': 'application/json'
    }
    response = requests.request('POST',
                                BASE_URL + (SEND_ACTIVITY % conversation["conversationId"]),
                                headers=headers,
                                json=activity)
    return json.loads(response.text)

def get_activities(conversation):
    """
    Get activities in this conversation.
    """
    headers = {
        'Authorization': ("Bearer %s" % conversation["token"]),
        'Content-Type': 'application/json'
    }
    response = requests.request('GET',
                                BASE_URL + (GET_ACTIVITIES % conversation['conversationId']),
                                headers=headers)
    return json.loads(response.text)

def main():
    """
    the main function
    """
    conversation = start_conversation()
    print json.dumps(conversation, indent=4)
    print "-" * 50

    activity = {"type":"message", "from": {"id":"user"}, "text":"all"}
    result = send_activitiy(conversation, activity)
    print result
    print "-" * 50

    time.sleep(10)

    activities = get_activities(conversation)
    print json.dumps(activities, indent=4)
    print "-" * 50

if __name__ == "__main__":
    main()
