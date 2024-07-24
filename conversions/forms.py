from django import forms
from .models import Conversion

# from django_recaptcha.fields import ReCaptchaField
# from django_countries.widgets import CountrySelectWidget


# CONSULTATION_METHOD_CHOICES = (
#     ('chat', 'Whatsapp Chat (RECOMMENDED)'),
#     ('phone', 'Whatsapp Phone Call'),
# )

class ConversionForm(forms.ModelForm):
    # captcha = ReCaptchaField()
    def __init__(self, *args, **kwargs):
        super(ConversionForm, self).__init__(*args, **kwargs)
        self.fields['fullname'].label = 'Name'

    class Meta:
        model = Conversion

        fields = ['fullname', 'email','phone_number','service', 'description',]

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'block w-full py-4 px-8 h-16 mb-6 bg-white border border-coolGray-400 rounded-full', 'required':True, 'placeholder':'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full py-4 px-8 h-16 mb-6 bg-white border border-coolGray-400 rounded-full', 'required':True, 'placeholder':'Email Address'}),
            'phone_number': forms.TextInput(attrs={'class': 'block w-full py-4 px-8 h-16 mb-6 bg-white border border-coolGray-400 rounded-full', 'required':True, 'placeholder':'Your Phone Number'}),
            'service': forms.Select(attrs={'class': 'relative block w-full py-4 px-8 h-16 mb-6  bg-transparent border border-coolGray-400 rounded-full appearance-none outline-none', 'required':True}),
            'description': forms.Textarea(attrs={'class': 'w-full h-52 py-5 px-8 bg-white border border-coolGray-400 rounded-3xl resize-none mb-8', 'required':True, 'placeholder':'Describe Your Project'}),
        }

# class MessageForm(forms.ModelForm):
#     captcha = ReCaptchaField()
#     class Meta:
#         model = Message

#         fields = ['name', 'subject', 'email', 'message']
#         captcha = ReCaptchaField()

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'bordered-box', 'style': 'color: #000000 ; background-color: #ffffff;', 'required':True, 'placeholder':'Your name'}),
#             'subject': forms.TextInput(attrs={'class': 'bordered-box', 'style': 'color: #000000 ; background-color: #ffffff;','required':True, 'placeholder':'Subject'}),
#             'email': forms.EmailInput(attrs={'class': 'bordered-box', 'style': 'color: #000000 ; background-color: #ffffff;', 'required':True, 'placeholder':'Email address'}),
#             'message': forms.Textarea(attrs={'class': 'bordered-box', 'style': 'color: #000000 ; background-color: #ffffff;', 'required':True, 'placeholder':'Your message'}),
#         }


