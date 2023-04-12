import uuid
from django.http import JsonResponse
from rest_framework import status
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from ..models.Invitation import Invitation
from ..mailService import mailer
from ..models import PaypalEvent

@csrf_exempt
def IPNListener(request):
    # check if request method is POST
    
    data = json.loads(request.body)
    email_address = data["resource"]["subscriber"]["email_address"]

    #check what event came
    if data["event_type"] == "BILLING.SUBSCRIPTION.ACTIVATED":
        event = PaypalEvent.objects.create(email=email_address, event_type='BILLING.SUBSCRIPTION.ACTIVATED')
        #onboard a new user
        link = str(uuid.uuid4())
        # Create a new InvitationLink object
        invitation_link = Invitation(link=link)
        invitation_link.save()
        mailer.sendMail(email_address,mailer.SUBSCRIPTION_ACTIVATED,link)
        
    if data["event_type"] == "BILLING.SUBSCRIPTION.CANCELLED":
        #user has cancelled his subscription
        #send a sad to see you go email
        #also deactivate the account
        event = PaypalEvent.objects.create(email=email_address, event_type='BILLING.SUBSCRIPTION.CANCELLED')
        try:
            user = User.objects.get(username = email_address)
            user.is_active = False
            user.save()
            mailer.sendMail(email_address,mailer.SUBSCRIPTION_CANCELLED)
        except:
            pass
        
    # if data["event_type"] == "BILLING.SUBSCRIPTION.EXPIRED":
    #     #user subscription has expired (???)
    #     #when does a subscription expire?
    #     event = PaypalEvent.objects.create(email=email_address, event_type='BILLING.SUBSCRIPTION.EXPIRED')
    #     try:
    #         mailer.sendMail(email_address,mailer.SUBSCRIPTION_EXPIRED)
    #         user = User.objects.get(username = email_address)
    #         user.is_active = False
    #         user.save()
    #     except:
    #         pass

    if data["event_type"] == "BILLING.SUBSCRIPTION.PAYMENT.FAILED":
        event = PaypalEvent.objects.create(email=email_address, event_type='BILLING.SUBSCRIPTION.PAYMENT.FAILED')
        #payment of a subscription has failed.
        #disable the user
        try:
            mailer.sendMail(email_address,mailer.SUBSCRIPTION_PAYMENT_FAILED)
            user = User.objects.get(username = email_address)
            user.is_active = False
            user.save()
        except:
            pass

    if data["event_type"] == "BILLING.SUBSCRIPTION.RE-ACTIVATED":
        event = PaypalEvent.objects.create(email=email_address, event_type='BILLING.SUBSCRIPTION.RE-ACTIVATED')
        #user has reactivated his subscription
        #enable the user
        try:
            mailer.sendMail(email_address,mailer.SUBSCRIPTION_RE_ACTIVATED)
            user = User.objects.get(username = email_address)
            user.is_active = True
            user.save()
        except:
            pass

    return JsonResponse({
            "message":"",
            "error":""
            },status=status.HTTP_200_OK)
    if request.method == 'POST':
        # get user input from request
        print(request)
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