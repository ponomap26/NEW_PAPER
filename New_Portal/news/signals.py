from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string
from .models import PostCategory
from .tasks import send_notification


def send_notification(preview, pk, title, subscribers):
    html_contect = render_to_string(
        'news_create_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_contect, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=PostCategory)
def notify_about_news(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        print(f'{categories= }')
        subscribers: list[str] = []

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]
        send_notification.delay(instance.preview, instance.pk, instance.title, subscribers)
