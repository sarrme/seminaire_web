from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

FIELD_NAME_MAPPING = {
    'first_name': 'prénom',
    'ggg': 'nom'
}
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optionnel.')
    email = forms.EmailField(max_length=254, help_text='Requis. entrer une adresse email valide.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Prénom"
        self.fields['last_name'].label = "Nom"