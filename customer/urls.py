from django.urls import path
from customer import views

app_name = 'customer'

urlpatterns = [
    path('signup/', views.signup, name='customer_signup'),
]
