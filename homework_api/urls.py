from django.urls import path
from .views import HomePageView, DriverCreateView, DriverDetailView, DriverUpdateView, work_form_view

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('work/', work_form_view),
    path('<int:pk>/', DriverDetailView.as_view(), name='details'),
    path('new/', DriverCreateView.as_view(), name='create'),
    path('<int:pk>/edit', DriverUpdateView.as_view(), name='update')
    # path('<int:pk>/delete', DriverDeleteView.as_view(), name='delete')
]