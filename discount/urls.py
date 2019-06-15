from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required

from . import views

app_name = 'discount'

urlpatterns = [
    path('', views.Discount.as_view(), name='index'),

    path('use', views.UseDiscount.as_view(), name='use'),
    path('report', staff_member_required(views.AdminReport.as_view()), name='report'),

    path('percent/<code>/users', views.ListPercentDiscount.as_view(), name='percent_users'),
    path('amount/<code>/users', views.AdminReport.as_view(), name='amount_users'),
]
