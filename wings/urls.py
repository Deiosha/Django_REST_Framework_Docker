from django.urls import path
from .views import WingList, WingDetail

urlpatterns = [
    path('', WingList.as_view(), name='wing_list'),
    path('<int:pk>/', WingDetail.as_view(), name='wing_detail'),
]