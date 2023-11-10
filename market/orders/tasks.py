from celery import shared_task
from django.core.mail import EmailMessage
from configuration import EMAIL_USER
from .models import Orders
from django.template.loader import render_to_string, get_template

@shared_task
def send_email(order_id): 
    subject = "You have order"
    send_to = []
    from_email = EMAIL_USER
    # user_email = Orders.objects.filter(order_id).select_related('user')
    # print(user_email.user.email)
    # if user_email:
    data = Orders.objects.filter(id=order_id).select_related('user').values('user__username', 'user__email', 'address', 'city', 'total_price').first()
    send_to.append(data['user__email'])
    

    
    message = get_template('orders/order-email-signal.html').render(data)
    msg = EmailMessage(subject, message, to=send_to, from_email=from_email)
    msg.content_subtype = 'html'
    msg.send()