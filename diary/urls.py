from django.urls import path

from diary import views
from diary.views import DiaryPostListView, DiaryPostDetailView, DiaryPostCreateView, DiaryPostUpdateView, \
    DiaryPostDeleteView, contacts

app_name = 'diary'

urlpatterns = [
    path('', DiaryPostListView.as_view(), name='diary_list'),
    path('diary/<int:pk>/', DiaryPostDetailView.as_view(), name='diary_detail'),
    path('diary/create/', DiaryPostCreateView.as_view(), name='diary_create'),
    path('diary/<int:pk>/update/', DiaryPostUpdateView.as_view(), name='diary_update'),
    path('diary/<int:pk>/delete/', DiaryPostDeleteView.as_view(), name='diary_delete'),
    path('contacts/', contacts, name='contacts'),
    path('search/', views.search_view, name='search'),
]