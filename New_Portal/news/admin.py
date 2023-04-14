from django.contrib import admin
from .models import Post, Author, Category, PostCategory, Comment
from modeltranslation.admin import TranslationAdmin  # импортируем модель амдинки (вспоминаем модуль про переопределение стандартных админ-инструментов)


class CategoryAdmin(TranslationAdmin):
    model = Category


class PostAdmin(TranslationAdmin):
    model = Post


class AuthorAdmin(TranslationAdmin):
    model = Author


class PostCategoryAdmin(TranslationAdmin):
    model = PostCategory


admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(PostCategory)
admin.site.register(Comment)
