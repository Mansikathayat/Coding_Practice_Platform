from django.contrib.auth.models import User

# Reset testuser password
try:
    user = User.objects.get(username='testuser')
    user.set_password('test123')
    user.save()
    print("testuser password reset to: test123")
except User.DoesNotExist:
    user = User.objects.create_user('testuser', 'test@test.com', 'test123')
    print("testuser created with password: test123")

# Reset admin password
try:
    admin = User.objects.get(username='admin')
    admin.set_password('admin123')
    admin.save()
    print("admin password reset to: admin123")
except User.DoesNotExist:
    admin = User.objects.create_superuser('admin', 'admin@test.com', 'admin123')
    print("admin created with password: admin123")

print("All passwords reset successfully!")