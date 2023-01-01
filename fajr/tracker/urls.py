from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'tracker', views.TrackerViewSet)

urlpatterns = [
    path('', views.read_data, name = 'read-data'),
    path('create/', views.create_data, name = 'create-record'),
    path('edit/<int:pk>', views.edit_data, name = 'edit-record'),
    path('delete/<int:pk>', views.delete_data, name = 'delete-record'),

    # path('api/', include(router.urls)),
    # path('api/<int:pk>', include(router.urls))

    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    # path('read/', views.read_data, name = 'view-records'),

    path('api/', views.TrackerAPIView.as_view()),
    path('api/<int:id>/', views.TrackerDetailAPIView.as_view())

    
]