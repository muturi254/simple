from django import forms
from boards.models import Topic

# froms
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
