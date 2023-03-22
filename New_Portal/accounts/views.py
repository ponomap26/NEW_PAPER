from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group

from django.views.generic.edit import CreateView

from news.models import Author
from .forms import SignUpForm


class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login'
    template_name = 'registration/signup.html'


class AuthorCreate(LoginRequiredMixin, CreateView):
    model = Author
    fields = ['authorUser']
    success_url = '/news/author'
    template_name = 'author.html'

    def form_valid(self, form):
        form.instance.authorUser = self.request.user
        return super().form_valid(form)


def add_author(pk, request):
    user = super().save(request)
    author_group = Group.objects.get(name="author")
    user.groups.add(author_group)
    Author.objects.create(authorUser=User.objects.get(pk=user.id))
    return user
