from django.contrib.auth.models import User

# Create superuser
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
    print("Superuser created: admin/admin123")

# Create test user
if not User.objects.filter(username='testuser').exists():
    User.objects.create_user('testuser', 'test@test.com', 'test123')
    print("Test user created: testuser/test123")

print("Users created successfully!")