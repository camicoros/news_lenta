from django.utils import timezone
from django.views.generic import DetailView, ListView

from news.models import Post


class PostListView(ListView):
    """Отображение списка постов.
    пагинация по 10 постов
    неопубликованные посты скрыты
    сортировка по дате публикации
    """
    template_name = 'news/index.html'
    model = Post
    paginate_by = 10
    queryset = Post.objects.filter(
        is_published=True, pub_date__lte=timezone.now()
    )
    ordering = ('-pub_date',)
    extra_context = {'header': 'Все новости'}


class PostDetailView(DetailView):
    """Страница отдельного поста.
    неопубликованные посты скрыты
    """
    template_name = 'news/detail.html'
    model = Post
    slug_url_kwarg = 'slug'
    context_object_name = 'post'
    queryset = Post.objects.filter(
        is_published=True, pub_date__lte=timezone.now()
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = self.object.name
        return context
