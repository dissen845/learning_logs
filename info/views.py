from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from .models import Topic, Titles, Discussion
from .forms import TopicForm, TitlesForm, DiscussionForm

def index(request):
    """Домашняя страница приложения info"""
    return render(request, 'info/index.html')

def topics(request):
    """Выводит список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'info/topics.html', context)

def titles(request,topic_id):
    """Выводит раздел и всё, что в нём есть"""
    topic = Topic.objects.get(id=topic_id)
    titles = topic.titles_set.order_by()
    context = {'topic': topic, 'titles': titles}
    return render(request, 'info/titles.html', context)

def discussion(request, titles_id):
    """Выводит все записи по объекту titles"""
    title = Titles.objects.get(id=titles_id)
    discussions = title.discussion_set.order_by('-date_added')
    context = {'titles': title, 'discussions': discussions}
    return render(request, 'info/discussions.html', context)

@login_required
def new_topic(request):
    """Определяет новый раздел"""

    if Topic.owner != request.user.username != 'dissen':
        raise Http404

    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('info:topics')

    context = {'form': form}
    return render(request, 'info/new_topic.html', context)

@login_required
def new_titles(request, topic_id):
    """Определяет новый объект раздела(название фильма, сериала и т.д.)"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = TitlesForm()
    else:
        form = TitlesForm(data=request.POST)
        if form.is_valid():
            new_titles = form.save(commit=False)
            new_titles.topic = topic
            new_titles.owner = request.user
            new_titles.save()
            return redirect('info:titles', topic_id=topic_id)

    context = {'topic': topic, 'form': form}
    return render(request, 'info/new_titles.html', context)

@login_required
def new_discussion(request, titles_id):
    """Определяет новый отзыв"""
    titles = Titles.objects.get(id=titles_id)
    topic = titles.topic
    if request.method != 'POST':
        form = DiscussionForm()
    else:
        form = DiscussionForm(data=request.POST)
        if form.is_valid():
            new_discussion = form.save(commit=False)
            new_discussion.titles = titles
            new_discussion.topic = titles
            new_discussion.owner = request.user
            new_discussion.save()
            return redirect('info:discussion', titles_id=titles_id)

    context = {'topic': topic, 'titles': titles, 'form': form}
    return render(request, 'info/new_discussion.html', context)

@login_required
def edit_titles(request, titles_id):
    """Редактирует существующую запись"""
    titles = Titles.objects.get(id=titles_id)
    topic = titles.topic
    if titles.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = TitlesForm(instance=titles)
    else:
        form = TitlesForm(instance=titles, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:titles', topic_id=topic.id)

    context = {'topic': topic, 'titles': titles, 'form': form}
    return render(request, 'info/edit_titles.html', context)

@login_required
def edit_discussion(request, discussion_id):
    """Редактирует существующий отзыв"""
    discussion = Discussion.objects.get(id=discussion_id)
    titles = discussion.topic
    topic = titles.topic
    if discussion.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = DiscussionForm(instance=discussion)
    else:
        form = DiscussionForm(instance=discussion, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('info:discussion', titles_id=titles.id)

    context = {'titles': titles, 'discussion': discussion, 'form': form}
    return render(request, 'info/edit_discussion.html', context)

# def delite_discussion(request, discussion_id):
#     """Удалить существующий отзыв"""
#     discussion = Discussion.objects.get(id=discussion_id)
#     if discussion.owner != request.user:
#         raise Http404
#     discussion.delete()
#     titles = discussion.topic
#     return redirect('info:discussion', titles_id=titles.id)

class Delite(DeleteView):
    """Удалить существующий отзыв"""
    model = Discussion
    success_url = '/topics/'
    template_name = 'info/delite_discussion.html'
    pk_url_kwarg = 'discussion_id'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(Delite, self).get_object()
        if obj.owner != self.request.user:
            raise Http404
        return obj