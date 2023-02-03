from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PostCategory


@receiver(post_save, sender=PostCategory)
def news_create(instance, created, **kwargs):
    if not created:
        return

    emails = User.objects.filter(
        subscriptions__category=instance.category
    ).values_list('email', flat=True)

    subject = f'Новый Пост в категории {instance.category}'

    text_content = (
        f'Заголовок: {instance.title}\n'
        f'Категория поста: {instance.category}\n\n'
        f'Ссылка на пост: http://127.0.0.1{instance.get_absolute_url()}'
    )
    html_content = (
        f'Заголовок: {instance.title}<br>'
        f'категория: {instance.category}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на пост</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()