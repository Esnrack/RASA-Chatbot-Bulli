# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open(".\info\dados.json", encoding="utf-8")
        x = json.load(file)
        y = x["menu"]

        for item in y:
            print(item["id"], item["nome"])
            if item["id"] == 4:
                print(item["descricao"])

        #dispatcher.utter_message(text="Hello World!")

        return []
