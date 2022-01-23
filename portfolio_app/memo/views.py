from django.shortcuts import render
from .models import Memo

def index(request):
    memos = Memo.objects.all()

    return render(request, 'memo/index.html', {'memos': memos})