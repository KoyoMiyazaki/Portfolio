from django.forms import ModelForm
from .models import Memo

class MemoForm(ModelForm):
    class Meta:
        model = Memo
        fields = '__all__'