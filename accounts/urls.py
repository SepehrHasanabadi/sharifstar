from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),

    path('info/<user_type>', views.Information.as_view(), name='info'),

]
