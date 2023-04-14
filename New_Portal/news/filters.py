from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dataCreation',
        lookup_expr='gt',
        label="Дата публикации не позднее",
        widget=DateTimeInput(
            format='%Y-%m-%d',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            'author': ['exact'],
            'title': ['icontains'],
            'category': ['exact'],
            'categoryType': ['exact'],

        }
