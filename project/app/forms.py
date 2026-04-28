from django import forms
from django.db.models.fields import CharField

from .models import Vacancies, Category, Comment
from django.core.validators import ValidationError

class VacanciesForm(forms.ModelForm):
    class Meta:
        model = Vacancies
        fields = "__all__"

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary <= 0:
            raise ValidationError('salary must be greater than 0 !!!')
        return salary

    def clean_contacts(self):
        contacts = self.cleaned_data.get('contacts')
        if (not contacts[0] == "+" and not contacts[1::12].isdigit()
                or contacts[0] == "@"):
            raise ValidationError('please enter your contacts correctly')
        return contacts

    # def clean(self):
    #     cleaned_data = super().clean()
    #     salary = cleaned_data.get('salary')
    #
    #
    #     if salary <= 0:
    #         raise ValidationError('salary must be greater than 0 !!!')
    #
    #
    #     contacts = cleaned_data.get('contacts')
    #     if not contacts[0] == "+" and not contacts[1::12].isdigit() or contacts[0] == "@":
    #         raise ValidationError('please enter your contacts correctly')
    #     return cleaned_data

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    widgets = {
        'direction': forms.TextInput(attrs={
            'class': 'form-control'
        })
    }

from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'write comment'
        })
    )

