from django.urls import path
from .views import *

urlpatterns = [
    path('transaction/', process_transaction),
    path('convert/', convert),
    path('validate-number/', validate_number),
]