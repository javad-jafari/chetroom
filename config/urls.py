from django.contrib import admin
from django.urls import path, include
from schema_graph.views import Schema
from chat import views
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path("schema/", Schema.as_view()),
    path('new/', include("new.urls")),
    path('chat/', include('chat.urls')), 
    path('logout/', views.Logout.as_view(), name='out'),
    path('login/', views.Login.as_view(), name='in'),
    path('token/', ObtainAuthToken.as_view(), name='token'),
    
]
