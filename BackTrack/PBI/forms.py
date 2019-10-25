from django import forms

from .models import PB_item


class PB_itemForm(forms.ModelForm):
    class Meta:
        model=PB_item
        fields=[
            "feature","priority","story_point"
        ]

class PB_editForm(forms.ModelForm):
    class Meta:
        model=PB_item
        fields=[
            'feature','status','priority','story_point'
        ]
