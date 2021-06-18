from django.urls import path
from .views import HomePageView, DriverCreateView, DriverDetailView,  work_form_view, DriverList, DriverDetail, DriverUpdateView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('work/', work_form_view),
    path('<int:pk>/', DriverDetailView.as_view(), name='details'),
    path('new/', DriverCreateView.as_view(), name='create'),
    path('<int:pk>/edit', DriverUpdateView.as_view(), name='update'),
    path('api/', DriverList.as_view(), name='api'),
    path('api/<int:pk>/', DriverDetail.as_view(), name='apidetail')
    # path('<int:pk>/delete', DriverDeleteView.as_view(), name='delete')
]