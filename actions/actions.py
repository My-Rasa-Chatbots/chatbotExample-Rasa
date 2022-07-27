# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import pymongo
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from rasa_sdk.events import EventType, AllSlotsReset
import re

from sqlalchemy import null

# MongoDB connection


def connectDB():
    conn_str = "mongodb+srv://kesu:keshab123@cluster0.bqo0o.mongodb.net/?retryWrites=true&w=majority"
    try:
        client = pymongo.MongoClient(conn_str)
        db_name = "mChat"
        col_name = "responses_test"
        my_db = client[db_name]
        my_coll = my_db[col_name]
        # print("DB Connected successfully:")
        return my_coll
    except pymongo.errors.ConnectionFailure as e:
        print("Database connection problem: ", str(e))
#################################################
####  query DB and send response
def getResponse(response_name):
    my_coll = connectDB()
    try:
        res = my_coll.find_one({"response_name": response_name})

        response = res["response_payload"]
        
        return response
    except pymongo.errors.OperationFailure as e:
        print("MongoDB Operational Failure: ",e.details)
        return []
################################################
# general chitchat topics


class ActionUtterGreet(Action):
    def name(self) -> Text:
        return "action_utter_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_greet"
        response=getResponse(resp_name)
        dispatcher.utter_message(json_message=response)
        return []
        


class ActionUtterCheerUp(Action):
    def name(self) -> Text:
        return "action_utter_cheer_up"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_cheer_up"
        response=getResponse(resp_name)
        dispatcher.utter_message(json_message=response)
        return []
##############################################
# contact form


class ValidateContactForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_contact_form"

    def validate_user_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        return {"user_name": slot_value}

    def validate_user_phone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        phone_regex = "^(\+\d{1,3}[- ]?)?\d{10}$"
        if(re.search(phone_regex, slot_value) != None):
            # print("Phone number matched")
            return {"user_phone": slot_value}
        else:
            print("Phone number not matched")
            return {"user_phone": None}

    def validate_user_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if(re.search(email_regex, slot_value) != None):
            return {"user_email": slot_value}
        print("Email mismatch")

        return {"user_email": None}

    def validate_user_query(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        return {"user_query": slot_value}


class SubmitContactForm(Action):
    def name(self) -> Text:
        return "submit_contact_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        print("form submitted")
        name = tracker.get_slot("user_name")
        email = tracker.get_slot("user_email")
        phone = tracker.get_slot("user_phone")
        query = tracker.get_slot("user_query")
        print(name, email, phone, query)
        dispatcher.utter_message(response="utter_we_will_contact_you")
        return [AllSlotsReset()]

##############################################
# Divergence topic


class ActionHowMarlabsRecognition(Action):
    def name(self) -> Text:
        return "action_utter_Marlabs_Recognition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp_name = "action_utter_Marlabs_Recognition"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)
        return []


class ActionHowMarlabsExpert(Action):
    def name(self) -> Text:
        return "action_utter_How_Marlabs_Expert"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp_name = "action_utter_How_Marlabs_Expert"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)
        return []


class ActionHowMarlabsBestProducts(Action):
    def name(self) -> Text:
        return "action_utter_Marlabs_Best_Products"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp_name = "action_utter_Marlabs_Best_Products"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)
        return []


class ActionHowMarlabsSolutionArea(Action):
    def name(self) -> Text:
        return "action_utter_Marlabs_Solution_Area"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp_name = "action_utter_Marlabs_Solution_Area"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)
        return []


class ActionHowMarlabsIndustryLeading(Action):
    def name(self) -> Text:
        return "action_utter_How_Industry_Leading"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        resp_name = "action_utter_How_Industry_Leading"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)
        return []


############# Chetan ###################

# Computer Vision

class ActionUtterCvDefinition(Action):

    def name(self) -> Text:
        return "action_utter_CV_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_CV_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterCvUsage(Action):

    def name(self) -> Text:
        return "action_utter_CV_Usage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_CV_Usage"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterCvWorkings(Action):

    def name(self) -> Text:
        return "action_utter_CV_Workings"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_CV_Workings"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# NLP


class ActiontterNlpStands(Action):

    def name(self) -> Text:
        return "action_utter_NLP_Stands"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_NLP_Stands"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterNlpDefinition(Action):

    def name(self) -> Text:
        return "action_utter_NLP_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_NLP_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterNlpRpa(Action):

    def name(self) -> Text:
        return "action_utter_NLP_RPA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_NLP_RPA"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterNlpApllication(Action):

    def name(self) -> Text:
        return "action_utter_NLP_Apllication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_NLP_Apllication"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterNlpDocumentsStructure(Action):

    def name(self) -> Text:
        return "action_utter_NLP_Documents_Structure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_NLP_Documents_Structure"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterNlpDocumentsUnstructured(Action):

    def name(self) -> Text:
        return "action_utter_NLP_Documents_Unstructured"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_NLP_Documents_Unstructured"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# Fuzzy_Logic


class ActionUtterFlDefinition(Action):

    def name(self) -> Text:
        return "action_utter_FL_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_FL_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterFlAi(Action):

    def name(self) -> Text:
        return "action_utter_FL_AI"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_FL_AI"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# Digital_Assistant


class ActionUtterDaDefinition(Action):

    def name(self) -> Text:
        return "action_utter_DA_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_DA_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterDaRpa(Action):

    def name(self) -> Text:
        return "action_utter_DA_RPA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_DA_RPA"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterDaExamples(Action):

    def name(self) -> Text:
        return "action_utter_DA_Examples"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_DA_Examples"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# Chatbot


class ActionUtterChatbotDefinition(Action):

    def name(self) -> Text:
        return "action_utter_Chatbot_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_Chatbot_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterChatbotRpa(Action):

    def name(self) -> Text:
        return "action_utter_Chatbot_RPA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_Chatbot_RPA"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterChatbotBenefits(Action):

    def name(self) -> Text:
        return "action_utter_Chatbot_Benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_Chatbot_Benefits"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# Process_Discovery


class ActionUtterPdDefinition(Action):

    def name(self) -> Text:
        return "action_utter_PD_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PD_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPdWorking(Action):

    def name(self) -> Text:
        return "action_utter_PD_Working"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PD_Working"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPdBenefits(Action):

    def name(self) -> Text:
        return "action_utter_PD_Benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PD_Benefits"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# Process_Mining


class ActionUtterPmDefinition(Action):

    def name(self) -> Text:
        return "action_utter_PM_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PM_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPmUsage(Action):

    def name(self) -> Text:
        return "action_utter_PM_Usage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PM_Usage"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPmBenefits(Action):

    def name(self) -> Text:
        return "action_utter_PM_Benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PM_Benefits"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# Kannan ####################################################

# AI


class ActionutterAIbotservice(Action):

    def name(self) -> Text:

        return "action_utter_AI_bot_service"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_bot_service"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIBaas(Action):

    def name(self) -> Text:

        return "action_utter_AI_Baas"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Baas"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIRaas(Action):

    def name(self) -> Text:

        return "action_utter_AI_Raas"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Raas"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIRPAbot(Action):

    def name(self) -> Text:

        return "action_utter_AI_RPA_bot"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_RPA_bot"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIRPAaas(Action):

    def name(self) -> Text:

        return "action_utter_AI_RPAaas"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_RPAaas"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIIA(Action):

    def name(self) -> Text:

        return "action_utter_AI_IA"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_IA"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIIAFull(Action):

    def name(self) -> Text:

        return "action_utter_AI_IA_Full"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_IA_Full"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIAI(Action):

    def name(self) -> Text:

        return "action_utter_AI_AI"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_AI"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIAboutAI(Action):

    def name(self) -> Text:

        return "action_utter_AI_AboutAI"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_AboutAI"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIAIAutomation(Action):

    def name(self) -> Text:

        return "action_utter_AI_AI_Automation"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_AI_Automation"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIAIaas(Action):

    def name(self) -> Text:

        return "action_utter_AI_AIaas"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_AIaas"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIAdvantages(Action):

    def name(self) -> Text:

        return "action_utter_AI_Advantages"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Advantages"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIDisAdvantages(Action):

    def name(self) -> Text:

        return "action_utter_AI_DisAdvantages"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_DisAdvantages"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAITechnology(Action):

    def name(self) -> Text:

        return "action_utter_AI_Technology"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Technology"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIDetails(Action):

    def name(self) -> Text:

        return "action_utter_AI_Details"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Details"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIIntent(Action):

    def name(self) -> Text:

        return "action_utter_AI_Intent"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Intent"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAIBenefits(Action):

    def name(self) -> Text:

        return "action_utter_AI_Benefits"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_AI_Benefits"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# API


class ActionutterAPI(Action):

    def name(self) -> Text:

        return "action_utter_API"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIFull(Action):

    def name(self) -> Text:

        return "action_utter_API_Full"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Full"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIEnable(Action):

    def name(self) -> Text:

        return "action_utter_API_Enable"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Enable"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIDriven(Action):

    def name(self) -> Text:

        return "action_utter_API_Driven"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Driven"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIWorking(Action):

    def name(self) -> Text:

        return "action_utter_API_Working"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Working"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIEndPoint(Action):

    def name(self) -> Text:

        return "action_utter_API_EndPoint"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_EndPoint"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIEPImportance(Action):

    def name(self) -> Text:

        return "action_utter_API_EP_Importance"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_EP_Importance"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIBenefits(Action):

    def name(self) -> Text:

        return "action_utter_API_Benefits"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Benefits"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIMainreasons(Action):

    def name(self) -> Text:

        return "action_utter_API_Main_reasons"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Main_reasons"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPISecurity(Action):

    def name(self) -> Text:

        return "action_utter_API_Security"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Security"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionutterAPIPerformance(Action):

    def name(self) -> Text:

        return "action_utter_API_Performance"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_API_Performance"
        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []

# ############## Nagendra #############################
# Process Analytics


class ActionUtterPaDefination(Action):

    def name(self) -> Text:
        return "action_utter_PA_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PA_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPaBenefits(Action):

    def name(self) -> Text:
        return "action_utter_PA_Benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PA_Benefits"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterMlPurposeInPa(Action):

    def name(self) -> Text:
        return "action_utter_ML_Purpose_In_PA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_ML_Purpose_In_PA"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterHowMlUsedInPa(Action):

    def name(self) -> Text:
        return "action_utter_How_ML_Used_In_PA"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_How_ML_Used_In_PA"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterMlDefinition(Action):

    def name(self) -> Text:
        return "action_utter_ML_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_ML_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPaTypes(Action):

    def name(self) -> Text:
        return "action_utter_PA_Types"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PA_Types"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterDescriptivePaDefinition(Action):

    def name(self) -> Text:
        return "action_utter_Descriptive_PA_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_Descriptive_PA_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPredictivePaDefinition(Action):

    def name(self) -> Text:
        return "action_utter_Predictive_PA_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_Predictive_PA_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPresciptivePaDefinition(Action):

    def name(self) -> Text:
        return "action_utter_Prescriptive_PA_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_Prescriptive_PA_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterPaUsedAreas(Action):

    def name(self) -> Text:
        return "action_utter_PA_Used_Areas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PA_Used_Areas"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


# Process Re-Engineering

class ActionUtterProcessReEngineeringDefinition(Action):

    def name(self) -> Text:
        return "action_utter_PRE_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PRE_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterProcessReEngineerngSteps(Action):

    def name(self) -> Text:
        return "action_utter_PRE_Stages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PRE_Stages"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterProcessReEngineerngBenefits(Action):

    def name(self) -> Text:
        return "action_utter_PRE_Benefits"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PRE_Benefits"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterProcessReEngineerngDisadvantages(Action):

    def name(self) -> Text:
        return "action_utter_PRE_Disadvantages"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PRE_Disadvantages"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterProcessReEngineerngChallenges(Action):

    def name(self) -> Text:
        return "action_utter_PRE_Challenges"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_PRE_Challenges"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterRPADefinition(Action):

    def name(self) -> Text:
        return "action_utter_RPA_Definition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_RPA_Definition"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []


class ActionUtterRPAUsedAreas(Action):

    def name(self) -> Text:
        return "action_utter_RPA_Using_Areas"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        resp_name = "action_utter_RPA_Using_Areas"

        response=getResponse(resp_name)

        dispatcher.utter_message(json_message=response)

        return []
