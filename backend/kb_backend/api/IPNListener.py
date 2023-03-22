import uuid
from django.http import JsonResponse
from rest_framework import status

from django.views.decorators.csrf import csrf_exempt

from ..models.Invitation import Invitation
from ..mailService import mailer

@csrf_exempt
def IPNListener(request):
    # check if request method is POST
    if request.method == 'POST':
        # get user input from request
        

        #transaction is valid
        #create invitation link and send email

        link = str(uuid.uuid4())
        # Create a new InvitationLink object
        invitation_link = Invitation(link=link)
        invitation_link.save()

        mail = "razgriz9@gmail.com" #MOCK!
        subject = "Welcome to QRExp.pro!"
        body = '''Hello and welcome to QRExp.pro!
        Thank you for choosing us, as your QR generator tool. We promise we won't fail you!
        Click <a href="http://localhost:4200/newUser?id='''+invitation_link.link+'''">here to register your account.

        Sincerely,
        The QRExp.pro team
        '''

        mailer.sendMail(
            mail,
            subject,
            body
        )

        # return response with user input
        return JsonResponse({
            "message":invitation_link.link,
            "error":""
            },status=status.HTTP_200_OK)
    else:
        # return error response for other methods
        return JsonResponse({
            "message":"",
            "error":"This endpoint only accepts POST requests"
            },status=status.HTTP_400_BAD_REQUEST)

def is_valid_invitation_link(link):
    try:
        invitation_link = Invitation.objects.get(link=link)
        if invitation_link.is_used:
            # The invitation link has already been used
            return False
        else:
            # The invitation link is still valid
            return True
    except Invitation.DoesNotExist:
        # The invitation link does not exist in the database
        return False