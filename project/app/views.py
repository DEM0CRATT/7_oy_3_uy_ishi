from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


from .models import Vacancies, Category, Comment
from .forms import VacanciesForm, CategoryForm, CommentForm

def get_started(request: HttpRequest):
    vacancies = Vacancies.objects.all()
    categories = Category.objects.all()

    context = {
        'vacancies': vacancies,
        'categories': categories,
        'title': 'main menu'
    }

    return render(request, 'main/index.html', context)

def get_job_detail(request: HttpRequest, job_id: int):

    vacancy = get_object_or_404(Vacancies, pk=job_id)
    title = vacancy.title
    comments = Comment.objects.filter(vacancy=vacancy).order_by('-created_at')

    context = {
        'vacancy': vacancy,
        'title': title,
        'form': CommentForm(),
        'comments': comments
    }
    return render(request, 'main/job_detail.html', context)

def get_job_by_category(request: HttpRequest, category_id: int):
    vacancies = Vacancies.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    title = category.direction
    context = {
        'vacancies': vacancies,
        'categories': categories,
        'title': title
    }

    return render(request, 'main/index.html', context)

def add_vacancy(request: HttpRequest):
    if request.user.is_staff:
        if request.method == 'POST':
            form = VacanciesForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                vacancy = form.save()
                return redirect('job_detail', vacancy.pk)
        else:
            form = VacanciesForm()
        categories = Category.objects.all()
        context = {
            'form': form,
            'categories': categories,
            'title': 'add vacancy',
            'request': request
        }
        return render(request, "main/add_vacancy.html", context)

def add_category(request: HttpRequest):
    if request.user.is_staff:
        if request.method == "POST":
            form = CategoryForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                category = form.save()
                return redirect('get_started')
        form = CategoryForm()
        context = {
            'form': form,
            'title': 'add category'
        }
        return render(request, "main/add_category.html", context)

def update_vacancy(request: HttpRequest, vacancy_id: int):
    if request.user.is_staff:
        vacancy = Vacancies.objects.get(pk=vacancy_id)
        categories = Category.objects.all()
        if request.method == "POST":
            form = VacanciesForm(data=request.POST, files=request.FILES, instance=vacancy)
            if form.is_valid():
                form.save()
                return redirect('job_detail', job_id=vacancy.id)
        else:
            form = VacanciesForm(instance=vacancy)
        context = {
            'form': form,
            'vacancy': vacancy,
            'categories': categories,
            'request': request
        }
        return render(request, "main/update_vacancy.html", context)

def delete_vacancy(request: HttpRequest, vacancy_id: int):
    if request.user.is_staff:
        vacancy = Vacancies.objects.get(pk=vacancy_id)
        if request.method == "POST":
            vacancy.delete()
            return redirect('get_started')
        context = {
            'vacancy': vacancy
        }
        return render(request, 'main/confirm_delete_job.html', context)

def write_comment(request: HttpRequest, vacancy_id: int):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(data=request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.vacancy = Vacancies.objects.get(pk=vacancy_id)
                comment.save()
        return redirect('job_detail', vacancy_id)

@login_required(login_url='get_started')
def update_comment(request: HttpRequest, comment_id: int):
    comment = Comment.objects.get(pk=comment_id)
    if request.user == comment.user:

        if request.method == "POST":
            form = CommentForm(data=request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('job_detail', comment.vacancy.id)

        else:
            form = CommentForm(instance=comment)
            context = {
                'form': form
            }
            return render(request, 'main/update_comment.html', context)

@login_required(login_url='get_started')
def delete_comment(request: HttpRequest, comment_id: int):
    if request.user.is_staff:
        comment = Comment.objects.get(pk=comment_id)
        vacancy_id = comment.vacancy.id
        comment.delete()
        return redirect('job_detail', job_id=vacancy_id)






















