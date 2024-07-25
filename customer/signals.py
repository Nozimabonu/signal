import json
import os

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from config.settings import BASE_DIR
from customer.models import User
from django.contrib import messages
from django.core.mail import EmailMessage

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import FormView, CreateView

from customer.forms import LoginForm, RegisterModelForm
from django.contrib.auth.decorators import permission_required
from config import settings
from customer.models import User
from customer.views.tokens import account_activation_token


@receiver(post_save, sender=User)
def user_save(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.email} is created!')
        print(kwargs)
    else:
        print('User Updated')


@receiver(pre_delete, sender=User)
def user_delete(sender, instance, **kwargs):
    file_path = os.path.join(BASE_DIR, 'customer/delete_users/', f'user_{instance.id}.json')

    user_data = {
        'id': instance.id,
        'email': instance.email,
        'username': instance.username,
        'birth_of_date': instance.birth_of_date
    }

    with open(file_path, mode='w') as file_json:
        json.dump(user_data, file_json, indent=4)

    print(f'{instance.email} is deleted')










# @receiver(post_save, sender=User)
# def sending_link(sender, instance, created, **kwargs):
#     if created:
#         requests = sender.request_class
#         print('User Created')
#         print(requests)

# current_site = get_current_site(self.request)
# subject = "Verify Email"
# message = render_to_string('email/verify_email_message.html', {
#     'request': self.request,
#     'user': user,
#     'domain': current_site.domain,
#     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#     'token': account_activation_token.make_token(user),
# })
# email = EmailMessage(subject, message, to=[user.email])
# email.content_subtype = 'html'
#
# email.send()
# else:
#     print('User Updated ! ')
