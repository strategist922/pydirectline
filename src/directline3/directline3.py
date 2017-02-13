"""
A python client for talking to Direct Line API v3.0.

https://docs.botframework.com/en-us/restapi/directline3/#/
"""

import json
import requests

AUTH_PATTERN = "Bearer %s"

BASE_URL = "https://directline.botframework.com"
START_CONVERSATION = "/v3/directline/conversations" #Start a new conversation
SEND_ACTIVITY = "/v3/directline/conversations/%s/activities" #Send an activity
GET_ACTIVITIES = "/v3/directline/conversations/%s/activities" #Get activities in this conversation.

def start_conversation(secret):
    """
    Starts a new conversation.
    """
    headers = {
        'Authorization': (AUTH_PATTERN % secret),
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', BASE_URL + START_CONVERSATION, headers=headers)
    return json.loads(response.text)

def send_activitiy(conversation, activity):
    """
    Send an activity.
    """
    headers = {
        'Authorization': (AUTH_PATTERN % conversation["token"]),
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
        'Authorization': (AUTH_PATTERN % conversation["token"]),
        'Content-Type': 'application/json'
    }

    params = {}
    if watermark is not None:
        params["watermark"] = watermark

    response = requests.request('GET',
                                BASE_URL + (GET_ACTIVITIES % conversation['conversationId']),
                                headers=headers, params=params)
    return json.loads(response.text)
