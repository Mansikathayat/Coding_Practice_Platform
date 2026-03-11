from django.contrib.auth.models import User
from users.models import UserProfile

# Create test user
user = User.objects.create_user(
    username='testuser',
    password='testpass123',
    email='test@example.com'
)

# Create profile
UserProfile.objects.create(user=user)

print("Test user created: username=testuser, password=testpass123")