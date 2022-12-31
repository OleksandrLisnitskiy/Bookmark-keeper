from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone


class AddGroup(forms.Form):
    group_name = forms.CharField(max_length=15, label="",
                                 widget=forms.TextInput(attrs={'placeholder': 'Group Name',
                                                               'id': 'group_name'})
                                 )


class AddTask(forms.Form):
    task_name = forms.CharField(max_length=60, label="",
                                widget=forms.Textarea(attrs={'placeholder': 'Task',
                                                             'id': 'task'}))
    deadline = forms.DateTimeField(label="", required=False, input_formats=['%d/%m/%Y %H:%M'],
                                   widget=forms.TextInput(attrs={'placeholder': 'Deadline',
                                                                 "autocomplete": "off"})
                                   )


class EditTask(forms.Form):
    task = forms.CharField(max_length=60, label="",
                           widget=forms.Textarea(attrs={'placeholder': 'Task',
                                                        'id': 'edit_task'}))

    edit_deadline = forms.DateTimeField(label='', required=False, input_formats=['%d/%m/%Y %H:%M'],
                                        widget=forms.TextInput(attrs={'placeholder': 'Deadline',
                                                                      "autocomplete": "off"})
                                        )

    def clean(self):
        super(EditTask, self).clean()

        deadline = self.cleaned_data["edit_deadline"]

        if deadline < timezone.now():

            self.add_error("edit_deadline", "You've entered past date!")
            self._errors["edit_deadline"] = self.error_class(["You've entered past date!"])
            raise ValidationError("You've entered past date!")
        return self.cleaned_data


class EditGroup(forms.Form):
    group_name = forms.CharField(max_length=15, label="",
                                 widget=forms.TextInput(attrs={'placeholder': 'Group Name',
                                                               'id': 'edit_group_name'})
                                 )
