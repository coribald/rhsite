from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recordings/', views.RecordingListView.as_view(), name='recordings'),
    path('shows/', views.ShowListView.as_view(), name='shows'),
    path('recording/<int:pk>', views.RecordingDetailView.as_view(), name='recording-detail'),
    path('show/<int:pk>', views.ShowDetailView.as_view(), name='show-detail')
]