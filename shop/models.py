from django.db import models


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=155, choices=[('active', 'Active'), ('deleted', 'Deleted')], default="Active")

    def __str__(self):
        return self.name


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="contacts")
    enum_type = models.CharField(max_length=50,
                                 choices=[('telegram', 'Telegram'), ('phone', 'Phone'), ('instagram', 'instagram')])
    string_value = models.CharField(max_length=100)

    def __str__(self):
        return self.enum_type


class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.name


class Ad(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_agreeable = models.BooleanField(default=False)
    price = models.FloatField(max_length=155)
    currency = models.CharField(max_length=3, choices=[('som', 'SOM'), ('usd', 'USD'), ('rub', 'RUB')], default='som')
    vip_type = models.CharField(max_length=10, choices=[('normal', 'Normal'), ('vip', 'VIP')], default='normal')
    state = models.CharField(max_length=10,
                             choices=[('active', 'Active'), ('inactive', 'Inactive'), ('moderation', 'Moderation')],
                             default='active')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="ads")
    images = models.BinaryField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    is_liked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
