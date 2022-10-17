import json
import random
import requests




def HomeGetAppointment_Byid(id):
    try:
        URL = 'https://staging-api.vivifyhealthcare.com/UserAppointment/GetAppointmentByUserIdAppointmenttype/{}/Home'.format(id)
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer eyJ0 eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcxNDMyMjkxLCJqdGkiOiJjMjk0NDdlZDE4NDA0N2IxOTBhYzI2MGQ5MDgwZGNiOCIsInVzZXJfaWQiOjV9.TRVn5p3ddUEz0IH3x6ez9QsPQXIXyjPXUywBFUKTPLk'}
        r = requests.get(url = URL,headers=headers)
        data = r.json()['Result']
        total=[]
        output=""
        for i in data:
            a = {}
            # total.append("Dr. "+i['DoctorId']['Firstname']+ " "+"("+i['DoctorId']['Professional']['Specialization']+")"" \n")
            a["text"] = "Dr. "+i['DoctorId']['Firstname']+ " "+"("+i['DoctorId']['Professional']['Specialization']+")"
            a["value"] = i['DoctorId']['id']
            total.append(a)
        # another = {}
        # another["text"] = "Add Another Doctor"
        # another["value"] = "Add Another Doctor"
        # total.append(another)
       
            
        return total
    except:
        return " we would like to suggest you to book the appointment from the app for better coverage" 