from faker import Faker

from posts.models import Post


fake = Faker()

for i in range(8000):
    models.Post.objects.create(content = fake.text())