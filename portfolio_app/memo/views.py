from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Memo, Project
from .forms import MemoForm

def index(request):
    if request.method == 'POST':
        project_name = request.POST.get('project')
        project, created = Project.objects.get_or_create(name=project_name)

        Memo.objects.create(
            content=request.POST.get('content'),
            project=project,
        )
        return redirect('memo:index')
    
    memos = Memo.objects.all()
    projects = Project.objects.all()
    form = MemoForm()

    context = {
        'memos': memos,
        'projects': projects,
        'form': form,
    }

    return render(request, 'memo/index.html', context)

def project(request, pk):
    page_project = Project.objects.get(id=pk)

    if request.method == 'POST':
        Memo.objects.create(
            content=request.POST.get('content'),
            project=page_project,
        )
        return redirect('memo:project', pk=pk)

    memos = Memo.objects.filter(Q(project__name=page_project.name))
    projects = Project.objects.all()

    context = {
        'page_project': page_project,
        'memos': memos,
        'projects': projects,
    }

    return render(request, 'memo/project.html', context)

def update_memo(request, pk):
    memo = Memo.objects.get(id=pk)

    if request.method == 'POST':
        project_name = request.POST.get('project')
        project, created = Project.objects.get_or_create(name=project_name)
        memo.content = request.POST.get('content')
        memo.project = project
        memo.save()

        # 新しいプロジェクト名に更新を行った場合はトップページへリダイレクト
        if created == True:
            return redirect('memo:index')
        else:
            return redirect('memo:update-memo', pk=pk)
        
    projects = Project.objects.all()

    context = {
        'memo': memo,
        'projects': projects,
    }

    return render(request, 'memo/update_memo.html', context)

def delete_memo(request, pk):
    memo = Memo.objects.get(id=pk)

    if request.method == 'POST':
        memo.delete()
        return redirect('memo:index')
        
    projects = Project.objects.all()

    context = {
        'memo': memo,
        'projects': projects,
    }

    return render(request, 'memo/delete_memo.html', context)