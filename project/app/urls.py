from django.urls import path
from .views import (get_started, get_job_detail,
                    get_job_by_category, add_category,
                    add_vacancy, update_vacancy,
                    delete_vacancy, write_comment,
                    update_comment, delete_comment,
                    add_favorite_vacancy, get_to_the_favorites)

urlpatterns = [
    path('', get_started, name='get_started'),
    path('job_detail/<int:job_id>/', get_job_detail, name='job_detail'),
    path('get_job_by_category/<int:category_id>/', get_job_by_category, name="get_job_by_category"),
    path('add/vacancy/', add_vacancy, name='add_vacancy'),
    path('add/category/', add_category, name='add_category'),
    path('update/<int:vacancy_id>/vacancy/', update_vacancy, name='update-vacancy'),
    path('delete/<int:vacancy_id>/vacancy/', delete_vacancy, name='job-delete'),
    path('write/comments/<int:vacancy_id>/', write_comment, name='write_comment'),
    path('update/comments/<int:comment_id>/', update_comment, name='update_comment'),
    path('delete/comments/<int:comment_id>/', delete_comment, name='delete_comment'),
    path('add/favorite/vacancy/<int:vacancy_id>/', add_favorite_vacancy, name='add_favorite_vacancy'),
    path('get_to_the/my_favorites/', get_to_the_favorites, name='get_to_the_favorites')
]


