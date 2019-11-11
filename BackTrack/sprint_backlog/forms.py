from django import forms

from .models import sprint_backlog_item

class sprint_backlog_item_form(forms.ModelForm):
    class Meta:
        model=sprint_backlog_item
        fields=[
            "PBI",
            "title",
            "status",
            "owner",
            "estimation"
        ]
        widgets = {
            'PBI': forms.HiddenInput(),
            'status': forms.HiddenInput(),
            }