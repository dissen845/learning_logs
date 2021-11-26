from django import forms
from .models import Topic, Titles, Discussion

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class TitlesForm(forms.ModelForm):
    class Meta:
        model = Titles
        fields = ['text']
        labels = {'text': ''}

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['text']
        labels = {'text': ''}