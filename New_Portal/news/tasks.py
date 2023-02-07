from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import Post, Category, PostCategory
from datetime import datetime, timedelta
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from celery import shared_task


@shared_task
def my_job():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(dataCreation__gte=last_week)
    categories = set(posts.values_list('category__name', flat=True))
    subscribers = set(Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    html_content = render_to_string(
        'daily_news.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Еженедельные новости',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()


@shared_task
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


# @receiver(m2m_changed, sender=PostCategory)
# def notify_about_news(sender, instance, **kwargs):
#     if kwargs['action'] == 'post_add':
#         categories = instance.category.all()
#         subscribers: list[str] = []
#         for category in categories:
#             subscribers += category.subscribers.all()
#         subscribers = [s.email for s in subscribers]
#         send_notification(instance.preview, instance.pk, instance.title, subscribers)
