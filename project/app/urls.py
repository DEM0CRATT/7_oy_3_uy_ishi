from django.urls import path
from .views import get_started, get_job_detail, get_job_by_category, add_category, add_vacancy, update_vacancy, delete_vacancy

urlpatterns = [
    path('', get_started, name='get_started'),
    path('job_detail/<int:job_id>/', get_job_detail, name='job_detail'),
    path('get_job_by_category/<int:category_id>/', get_job_by_category, name="get_job_by_category"),
    path('add/vacancy/', add_vacancy, name='add_vacancy'),
    path('add/category/', add_category, name='add_category'),
    path('update/<int:vacancy_id>/vacancy/', update_vacancy, name='update-vacancy'),
    path('delete/<int:vacancy_id>/vacancy/', delete_vacancy, name='job-delete')
]
