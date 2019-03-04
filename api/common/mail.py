"""
Mail module implements simple way to send email
Uses sendgrid's WEP api
"""
import http
import os
import sendgrid
import urllib.request as urllib

# from django.conf import settings
from django.http import HttpResponse

import sendgrid.helpers.mail
from api.config import local_settings as settings


def send_mail(subject, content, from_email, to_email, subs, template):
    sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
    substitutions = {}

    # If there are substitutions add them
    # to the personalization substitutions item
    if subs:
        for substitution in subs:
            substitutions['%' + substitution + '%'] = subs[substitution]

    data = {
        'personalizations': [
            {
                'to': to_email,
                'subject': subject,
                'substitutions': substitutions
            },
        ],
        'from': from_email,
        'content': [
            {
                'type': 'text/html',
                'value': content
            }
        ]
    }

    # If template is passed set the template Id
    # This will prompt sending of email via template
    if template:
        data['template_id'] = template

    try:
        response = sg.client.mail.send.post(request_body=data)
    except urllib.HTTPError as e:
        return HttpResponse(e)
    return response

