"""
A simple test module
"""

import json
import time

from .. import directline as dl3

def main():
    """
    the main function
    """
    conversation = dl3.start_conversation(
        "hDcYliwT7Uw.cwA.EhQ.uHC2fujOPSF2hwwqSpcVjlfLmCqFeY5qhJd2bm3dJ9U")

    print json.dumps(conversation, indent=4)
    print "-" * 50

    activity = {"type":"message", "from": {"id":"user"}, "text":"all"}
    result = dl3.send_activitiy(conversation, activity)
    print result
    print "-" * 50

    time.sleep(10)

    activities = dl3.get_activities(conversation)
    print json.dumps(activities, indent=4)
    print "-" * 50

    for activity in activities["activities"]:
        if activity["from"]["id"] == "cat-lunch-bot":
            print json.dumps(activity["text"])


if __name__ == "__main__":
    main()
