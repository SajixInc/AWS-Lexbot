import json
import random
import requests
from immunization import immunization_Byid
from GetAppointment import GetAppointment_Byid
from HealthSummary import HealthSummary_Byid
from teleconsulatationGetAppointment import teleconsulatationGetAppointment_Byid
from HomeGetAppointment import HomeGetAppointment_Byid
        


""" --- Main handler --- """
def lambda_handler(event, context):
    intent_name = event['interpretations'][0]['intent']['name']
    if intent_name == 'inclinic':
        slots = event['interpretations'][0]['intent']['slots']
        category = slots['CategoryName']['value']['interpretedValue']
        print(category)
        # but ={}
        # but["text"] = "Add Another Doctor"
        # but["value"] = "Add Another Doctor"
        message = GetAppointment_Byid(category)
        # message.append(but)
        response = {
           'sessionState' : {
                'dialogAction' : {
                    'type' : 'Close'
                },
                'intent' : {
                    'name' : intent_name,
                    'state' : 'Fulfilled'
                }
           },
            'messages': [
                 {
       "contentType": "ImageResponseCard",
       "imageResponseCard": {
        "title": "Recently Booked Doctors",
        "subtitle": "Recently Booked Doctors",
        "buttons":message
         
        
         
       }
      }
            ]
        }
        return response
        
    if intent_name == 'teleconsulatation':
        slots = event['interpretations'][0]['intent']['slots']
        category = slots['CategoryName']['value']['interpretedValue']
        print(category)
        # but ={}
        # but["text"] = "Add Another Doctor"
        # but["value"] = "Add Another Doctor"
        message = teleconsulatationGetAppointment_Byid(category)
        # message.append(but)
        response = {
           'sessionState' : {
                'dialogAction' : {
                    'type' : 'Close'
                },
                'intent' : {
                    'name' : intent_name,
                    'state' : 'Fulfilled'
                }
           },
            'messages': [
                 {
       "contentType": "ImageResponseCard",
       "imageResponseCard": {
        "title": "Recently Booked Doctors",
        "subtitle": "Recently Booked Doctors",
        "buttons":message
         
        
         
       }
      }
            ]
        }
        return response
        
    if intent_name == 'Home':
        slots = event['interpretations'][0]['intent']['slots']
        category = slots['CategoryName']['value']['interpretedValue']
        print(category)
        # but ={}
        # but["text"] = "Add Another Doctor"
        # but["value"] = "Add Another Doctor"
        message = teleconsulatationGetAppointment_Byid(category)
        # message.append(but)
        response = {
           'sessionState' : {
                'dialogAction' : {
                    'type' : 'Close'
                },
                'intent' : {
                    'name' : intent_name,
                    'state' : 'Fulfilled'
                }
           },
            'messages': [
                 {
       "contentType": "ImageResponseCard",
       "imageResponseCard": {
        "title": "Recently Booked Doctors",
        "subtitle": "Recently Booked Doctors",
        "buttons":message
         
        
         
       }
      }
            ]
        }
        return response
    elif intent_name == 'VHSmyself':
        slots = event['interpretations'][0]['intent']['slots']
        category = slots['CategoryName']['value']['interpretedValue']
        print(category)
        # but ={}
        # but["text"] = "Add Another Doctor"
        # but["value"] = "Add Another Doctor"
        message = HealthSummary_Byid(category)
        # message.append(but)
        response = {
           'sessionState' : {
                'dialogAction' : {
                    'type' : 'Close'
                },
                'intent' : {
                    'name' : intent_name,
                    'state' : 'Fulfilled'
                }
           },
            'messages': [
             {
                'contentType' : 'PlainText',
                'content' : message
             }
        ]
        }
        return response
    elif intent_name == 'immunizationmyself':
        slots = event['interpretations'][0]['intent']['slots']
        category = slots['CategoryName']['value']['interpretedValue']
        print(category)
        # but ={}
        # but["text"] = "Add Another Doctor"
        # but["value"] = "Add Another Doctor"
        message = immunization_Byid(category)
        # message.append(but)
        response = {
           'sessionState' : {
                'dialogAction' : {
                    'type' : 'Close'
                },
                'intent' : {
                    'name' : intent_name,
                    'state' : 'Fulfilled'
                }
           },
            'messages': [
             {
                'contentType' : 'PlainText',
                'content' : message
             }
        ]
        }
        return response