from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    # captcha = ReCaptchaField()
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['fullname'].label = 'Name'
        
    class Meta:
        model = Message

        fields = ['fullname','email','message']

        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'block w-full py-4 px-8 h-16 mb-6 bg-white border border-coolGray-400 rounded-full', 'required':True, 'placeholder':'Your name'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full py-4 px-8 h-16 mb-6 bg-white border border-coolGray-400 rounded-full', 'required':True, 'placeholder':'Your email address'}),
            'message': forms.Textarea(attrs={'class': 'w-full h-52 py-5 px-8 bg-white border border-coolGray-400 rounded-3xl resize-none mb-8', 'required':True, 'placeholder':'Your message'}),
        }