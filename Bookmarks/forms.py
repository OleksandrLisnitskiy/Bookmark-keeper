from django import forms
from .models import Groups


class AddGroup(forms.Form):
    group_name = forms.CharField(max_length=15, label="",
                                 widget=forms.TextInput(attrs={'placeholder': 'Group Name',
                                                               'id': 'group_name'})
                                 )

