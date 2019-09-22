from django.contrib.auth import get_user_model

User = get_user_model()

if User.objects.filter(email='admin@example.com').count() == 0:
    user_data = {'username': 'admin', 'email': 'admin@example.com', 'password': 'admin'}
    user = User.objects.create_superuser(**user_data)
