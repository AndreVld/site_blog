from django import forms
from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter

from .models import Posts, Tags


class PostFilter(FilterSet):
    headline = CharFilter(field_name='headline', lookup_expr='icontains', label='')
    tags = ModelMultipleChoiceFilter(queryset=Tags.objects.all(),
                                     widget=forms.CheckboxSelectMultiple(attrs={'class': 'list_categories'})
                                     )

    class Meta:
        model = Posts
        fields = ('headline', 'tags')
