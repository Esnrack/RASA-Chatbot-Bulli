# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import json
from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionCardapio(Action):

    def name(self) -> Text:
        return "action_cardapio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open(".\info\dados.json", encoding="utf-8")
        x = json.load(file)
        y = x["menu"]

        opcao = int(tracker.get_slot("name"))

        for item in y:
            print(item["id"], item["nome"])
            if item["id"] == opcao:
                print(item["descricao"])
                dispatcher.utter_message(text=item["descricao"])
        #dispatcher.utter_message(text="Hello World!")

        return []

class ActionSubcardapio(Action):

    def name(self) -> Text:
        return "action_subcardapio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open(".\info\dados.json", encoding="utf-8")
        x = json.load(file)
        y = x["menu"]
        opcaoMenu = int(tracker.get_slot("name"))

        for item in y:
            if item["id"] == opcaoMenu:
                submenu = item

        opcao = int(tracker.get_slot("submenu"))

        for item in submenu:
            print(item["id"], item["nome"])
            if item["id"] == opcao:
                print(item["descricao"])
                dispatcher.utter_message(text=item["descricao"])
        #dispatcher.utter_message(text="Hello World!")

        return []

class ActionMenu(Action):

    def name(self) -> Text:
        return "action_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open(".\info\dados.json", encoding="utf-8")
        x = json.load(file)
        itens = x["menu"]

        mensagem = ""
        for item in itens:
            mensagem += "{}. {}\n".format(item['id'], item['nome'])
        dispatcher.utter_message(text=mensagem)            

        return []

class ActionSubmenu(Action):

    def name(self) -> Text:
        return "action_submenu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        file = open(".\info\dados.json", encoding="utf-8")
        x = json.load(file)
        menu = x["menu"]
        opcao = int(tracker.get_slot("name"))
        itens = None
        for i in menu:
             if type(i) == list and i["id"] == opcao:
                itens = i
        if itens == None:
            mensagem = menu["descricao"]
        else:
            mensagem = ""        
        
        for item in itens:
            mensagem += "{}. {}\n".format(item['id'], item['nome'])
        dispatcher.utter_message(text=mensagem)            

        return []

class ActionInput(Action):

    def name(self) -> Text:
        return "action_input"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.latest_message['text']
        print(value)

        return [SlotSet('name', value)]

class ActionInputSubmenu(Action):

    def name(self) -> Text:
        return "action_input_submenu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        value = tracker.latest_message['text']
        print(value)

        return [SlotSet('submenu', value)]
