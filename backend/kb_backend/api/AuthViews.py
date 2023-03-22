import uuid
from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django_expiring_token.models import ExpiringToken
from django_expiring_token.authentication import ExpiringTokenAuthentication
from rest_framework import status
from django.contrib.auth.models import User
import string

from ..models import ResetPasswordId

class AuthView(APIView):
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        response = {}
        token = False
        if user is not None:
            try:
                token = ExpiringToken.objects.get(user=user)
            except:
                pass
            if token:
                token.delete()
            token = ExpiringToken.objects.create(user=user)
            response["response"] = token.key
            response["expires"] = token.expires
        else:
            response["error"] = "Incorrect username or password"
        return JsonResponse(response)
    # No backend authenticated the credentials

    def delete(self, request):
        request.user.auth_token.delete()
        return JsonResponse({"message":"logged out"})

class CheckAuth(APIView):
    authentication_classes = [ExpiringTokenAuthentication]

    def get(self, request, format=None):
        content = {
            'response':'Not authed',  # None
            }
        if (request.user.is_authenticated):
            content["response"] = "Authed"
        return JsonResponse(content)

class ChangePassword(APIView):

    authentication_classes = [ExpiringTokenAuthentication]

    def post(self, request):

        response = {
            "message":[],
            "errors":[]
        }

        passwordRequirements = {
            "oldPassAndNewPassNotSame": False,
            "oldPasswordOK": False,
            "passwordsMatch": False,
            "passwordLengthOK": False,
            "passwordHasCapitalChar": False,
            "passwordHasSpecialChar": False,
        }


        #check if old password is valid
        if request.user.check_password(request.data["oldPassword"]):
            passwordRequirements["oldPasswordOK"] = True
        else:
            response["errors"].append("Old password invalid")


        #check if passwords match
        if request.data["newPassword"] == request.data["newPasswordConfirm"]:
            passwordRequirements["passwordsMatch"] = True
        else:
            response["errors"].append("Passwords do not match")

        #check if old password is the same with the new password
        if request.data["newPassword"] == request.data["oldPassword"]:
            response["errors"].append("New password cannot be the same as the new password")
        else:
            passwordRequirements["oldPassAndNewPassNotSame"] = True

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

        if any(c in string.punctuation for c in request.data["newPassword"]) and any(c in string.punctuation for c in request.data["newPasswordConfirm"]):
            passwordRequirements["passwordHasSpecialChar"] = True
        else:
           response["errors"].append("Password must contain at least 1 special character") 


        #check all password requirements
        #if some fails, return an error response
        for policy in passwordRequirements:
            if passwordRequirements[policy] == False:
                response["message"] = "Please verify the password requirements"
                return JsonResponse(response,status = status.HTTP_400_BAD_REQUEST)

        #change the users password
        response["message"] = "Password changed successfuly!"

        u = User.objects.get(username=request.user)
        u.set_password(request.data["newPassword"])
        u.save()

        return JsonResponse(response,status=status.HTTP_200_OK)


class RequestResetPasswordId(APIView):
    def post(self, request):
        response = {
            "message":[],
            "errors":[]
        }

        if "username" not in request.data:
            response.errors.append("Invalid request")
            return JsonResponse(response,status = status.HTTP_400_BAD_REQUEST) 

        try:
            user = User.objects.get(username=request.data["username"])
            #return JsonResponse(response,status = status.HTTP_200_OK)
        except:
            pass
        
        if not user:
            return JsonResponse(response,status = status.HTTP_200_OK)

        #create reset password id
        resetPasswordId = ResetPasswordId()
        resetPasswordId.username = request.data["username"]
        resetPasswordId.link = str(uuid.uuid4())
        resetPasswordId.is_used = False
        resetPasswordId.save()

        print(resetPasswordId.username,resetPasswordId.link,resetPasswordId.is_used)

        #send it to user via email

        return JsonResponse(response,status = status.HTTP_200_OK)
        
class ResetPassword(APIView):
    def post(self,request):

        response = {
            "message":[],
            "errors":[]
        }

        passwordRequirements = {
            "passwordsMatch": False,
            "passwordLengthOK": False,
            "passwordHasCapitalChar": False,
            "passwordHasSpecialChar": False,
        }

        if "newPassword" not in request.data:
            response.errors.append("Password missing")
        
        if "newPasswordConfirm" not in request.data:
            response.errors.append("Password confirmation missing")
        
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

        if any(c in string.punctuation for c in request.data["newPassword"]) and any(c in string.punctuation for c in request.data["newPasswordConfirm"]):
            passwordRequirements["passwordHasSpecialChar"] = True
        else:
           response["errors"].append("Password must contain at least 1 special character") 

        for policy in passwordRequirements:
            if passwordRequirements[policy] == False:
                response["message"] = "Please verify the password requirements"
                return JsonResponse(response,status = status.HTTP_400_BAD_REQUEST)
        
        #password policy ok.

        #check the reset link

        link = request.data["resetPasswordId"]
        try:
            resetPasswordId = ResetPasswordId.objects.get(link=link,is_used=False)
        except:
            return JsonResponse(response,status = status.HTTP_400_BAD_REQUEST)



        #change the user password to the new one
        try:
            u = User.objects.get(username=resetPasswordId.username)
            u.set_password(request.data["newPassword"])
            u.save()
            resetPasswordId.delete()
        except:
           return JsonResponse(response,status = status.HTTP_400_BAD_REQUEST) 

        return JsonResponse(response,status=status.HTTP_200_OK)