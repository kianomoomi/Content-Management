from django.contrib import admin
from django.urls import path

from core.views.user import *
from core.views.content import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # User API
    path('user/register/', RegisterView.as_view()),
    path('user/login/', LoginView.as_view()),

    # Content API
    path('content/create/', CreateView.as_view()),
    path('content/retrieve/', RetrieveView.as_view()),
]
