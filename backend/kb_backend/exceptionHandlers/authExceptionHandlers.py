from rest_framework.views import exception_handler
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response


def unauthenticated(exc, context):
    if isinstance(exc, AuthenticationFailed):
        return Response({"auth_error": str(exc)}, status=401)

    # else
    # default case
    return exception_handler(exc, context)