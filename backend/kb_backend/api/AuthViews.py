from django.contrib.auth import authenticate
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django_expiring_token.models import ExpiringToken
from django_expiring_token.authentication import ExpiringTokenAuthentication
from rest_framework.permissions import IsAuthenticated


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
        content = content = {
            'response':'Not authed',  # None
            }
        if (request.user.is_authenticated):
            content["response"] = "Authed"
        return JsonResponse(content)