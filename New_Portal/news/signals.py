from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .tasks import send_notification


@receiver(m2m_changed, sender=PostCategory)
def notify_about_news(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.category.all()
        print(f'{categories= }')
        subscribers: list[str] = []

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]
        send_notification.delay(instance.preview(), instance.pk, instance.title, subscribers)
