from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests

class ActionCoronaTracker(Action):

     def name(self) -> Text:
         return "action_corona_tracker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get("https://api.covid19india.org/data.json").json()

        entities = tracker.latest_message['entities']
        print(entities)
        state = None

        for e in entities:
            if e['entity'] == "state":
                state = e['value']
        
        if state == "india":
            state = "Total"

        message = "please enter correct state name"

        for data in response["statewise"]:
            if data["state"] == state.title():
                print(data)
                message = "Active : "+data["active"] +" Confirmed : " +data["confirmed"] +" Recovered : "+data["recovered"] +" On " +data["lastupdatedtime"]
        print(message)
        dispatcher.utter_message(message)

        return []
