from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.template.loader import render_to_string

from .models import PostCategory


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
def notify_about_news_post(sender, instance, **kwargs):
    print(" Первый!")
    if kwargs['action'] == 'post_add':
        print('signal')
        categories = instance.category.all()
        print(f'{categories= }')
        subscribers: list[str] = []

        for category in categories:
            subscribers += category.subscribers.all()

        subscribers = [s.email for s in subscribers]
        print(f'{subscribers= }')
        send_notification(instance.preview, instance.pk, instance.title, subscribers)

    # emails = User.objects.filter(
    #     subscriptions__category=instance.category
    #
    # subject = f'Новый Пост в категории {instance.category}'
    #
    # ).values_list('email', flat=True)
    # text_content = (
    #     f'Заголовок: {instance.title}\n'
    #     f'Категория поста: {instance.category}\n\n'
    #     f'Ссылка на пост: http://127.0.0.1{instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Заголовок: {instance.title}<br>'
    #     f'категория: {instance.category}<br><br>'
    #     f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
    #     f'Ссылка на пост</a>'
    # )
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()
