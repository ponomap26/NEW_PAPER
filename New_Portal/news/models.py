from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.authorUser}'

    def updata_reting(self):
        postRat = self.post.ser.aggregate(postRating=Sum('ratinfromg'))
        pRyt = 0
        pRyt += postRat.get('postRating')

        commentRat = self.authorUser.comment.set.aggregate(commentRating=Sum('rating'))
        cRet = 0
        cRet += commentRat.get('commentRating')
        self.retingAuthor = pRyt * 3 + cRet
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор")
    NEWS = "NW"
    ARTICLE = "AT"
    CATEGORY_CHOICES = (
        (NEWS, 'НОВОСТЬ'),
        (ARTICLE, 'СТАТЬЯ'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE, verbose_name="Категория Публикации")
    dataCreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    postCategory = models.ManyToManyField(Category, through='PostCategory', verbose_name="Тип Поста")
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    text = models.TextField(verbose_name=' ТЕКСТ')
    rating = models.SmallIntegerField(default=0, verbose_name="Рейтинг")



    def get_absolute_url(self):
        return reverse('new', args=[str(self.id)])

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[0:123] + '...'


class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.categoryThrough}'


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dataCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
