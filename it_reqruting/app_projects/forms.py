from django.forms import ModelForm
from .models import Project, Review


class ProjectForm(ModelForm):
    """form for Project model"""
    class Meta:
        model = Project
        fields = ['title', 'slug', 'tags', 'description', 'demo_link', 'source_link']


class ReviewForm(ModelForm):
    """Form for reviews"""
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Review the project',
            'body': 'Add comments'
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})