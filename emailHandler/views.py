
# download excel package
from django.http import HttpResponse

# rest framework package
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from rest_framework import status



def post_email(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'pigeg46259@toracw.com',
        ['gibocop445@box4mls.com'],
        fail_silently=False,
    )
    return HttpResponse('sent successfully.')
    # subject = request.data.get('subject')
    # if subject:
    #     try:
    #         send_mail(subject, message, from_email, ['admin@example.com'])
    #     except BadHeaderError:
    #         return Response({'success': 'True', 'message': 'data saved successfully'}, status=status.HTTP_201_CREATED)
