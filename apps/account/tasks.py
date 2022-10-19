from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

def send_activation_code(email, activation_code):
    activation_link = f'http://localhost:8000/account/activate/{activation_code}/'
    html_message = render_to_string(
        'account/code_mail.html', 
        {'activation_code': activation_link}   # двойные {} в html
        )
    send_mail(
        'Activate your account!',
        '',
        settings.EMAIL_HOST_USER,
        {email},
        html_message=html_message,
        fail_silently=False
    )