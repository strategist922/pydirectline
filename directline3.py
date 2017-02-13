"""
A python client for talking to Direct Line API v3.0.
"""

import json
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

def get_activities(conversation, watermark=None):
    """
    Get activities in this conversation.
    """
    headers = {
        'Authorization': ("Bearer %s" % conversation["token"]),
        'Content-Type': 'application/json'
    }

    params = {}
    if watermark is not None:
        params["watermark"] = watermark

    response = requests.request('GET',
                                BASE_URL + (GET_ACTIVITIES % conversation['conversationId']),
                                headers=headers, params=params)
    return json.loads(response.text)