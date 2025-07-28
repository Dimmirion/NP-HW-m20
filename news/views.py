from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

from .models import Post
from .filters import PostFilter

# Список новостей с пагинацией
class NewsList(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    ordering = ['-date_created']
    paginate_by = 10  # 10 новостей на страницу

# Поиск новостей
class NewsSearch(ListView):
    model = Post
    template_name = 'news/news_search.html'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

# Создание новости
class NewsCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'news/news_create.html'

    def form_valid(self, form):
        form.instance.post_type = Post.NEWS  # Автоматически ставим тип "Новость"
        return super().form_valid(form)

# Создание статьи
class ArticleCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'news/article_create.html'

    def form_valid(self, form):
        form.instance.post_type = Post.ARTICLE  # Автоматически ставим тип "Статья"
        return super().form_valid(form)

# Редактирование (общее для новостей и статей)
class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'news/post_edit.html'

# Удаление (общее для новостей и статей)
class PostDelete(DeleteView):
    model = Post
    template_name = 'news/post_delete.html'
    success_url = '/news/'


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from .models import Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # Укажите нужные поля
    template_name = 'post_edit.html'  # Шаблон для редактирования
    success_url = '/'  # Куда перенаправлять после успешного редактирования