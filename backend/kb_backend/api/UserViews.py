import string
from django.http import JsonResponse
from rest_framework import generics, status
from ..models import Invitation
from django.contrib.auth.models import User
import re

class UserCreateEndpoint(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        
        #check if invitation exists
        #invitationId = request.GET.get('id', '')
        try:
            invitation = Invitation.objects.get(link=request.data["invitationId"])
        except Invitation.DoesNotExist:
            return JsonResponse({
                "message":"",
                "errors":"Invitation does not exist"
                }, 
                status=status.HTTP_404_NOT_FOUND)
    
        #so if it exists we have to checked if is used
        if invitation.is_used:
            return JsonResponse({
                "message":"",
                "errors":"Invitation is already used"
                }, 
                status=status.HTTP_400_BAD_REQUEST)


        response = {
            "message":[],
            "errors":[]
        }

        #check if password meets the password policy
        passwordRequirements = {
            "passwordsMatch": False,
            "passwordLengthOK": False,
            "passwordHasCapitalChar": False,
            "passwordHasSpecialChar": False,
        }

        #check if passwords match
        if request.data["newPassword"] == request.data["newPasswordConfirm"]:
            passwordRequirements["passwordsMatch"] = True
        else:
            response["errors"].append("Passwords do not match")

        #check if password length is over 7 characters
        if len(request.data["newPassword"]) > 7 and len(request.data["newPasswordConfirm"]) > 7:
            passwordRequirements["passwordLengthOK"] = True
        else:
            response["errors"].append("Password length must be over 7 characters")

        #check if password has capital character
        if any(c.isupper() for c in request.data["newPassword"]) and any(c.isupper() for c in request.data["newPasswordConfirm"]):
            passwordRequirements["passwordHasCapitalChar"] = True
        else:
            response["errors"].append("Password must contain at least 1 capital character")

        #check if password has special character
        if any(c in string.punctuation for c in request.data["newPassword"]) and any(c in string.punctuation for c in request.data["newPasswordConfirm"]):
            passwordRequirements["passwordHasSpecialChar"] = True
        else:
           response["errors"].append("Password must contain at least 1 special character")

        for policy in passwordRequirements:
            if passwordRequirements[policy] == False:
                return JsonResponse(response,status = status.HTTP_400_BAD_REQUEST)

        #check if username is an email
        if "username" not in request.data:
            response["errors"].append("Username not found")
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)

        if not is_email(request.data["username"]):
            response["errors"].append("Username must be an email")
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User(username = request.data["username"])
            user.set_password(request.data["newPassword"])
            user.save()
            invitation.is_used = True
            invitation.save()
        except:
            response.errors.append("An error occured")

        response["message"] = "User created"
        return JsonResponse(response, status=status.HTTP_200_OK)
        

def is_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(pattern, email)