from django.db import models

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class User(models.Model):
    user_name = models.CharField(max_length=200, null=True)
    user_mobile = models.CharField(max_length=200, null=True)
    user_email = models.CharField(max_length=200, null=True)
    user_address = models.CharField(max_length=200, null=True)
    user_password = models.CharField(max_length=200, null=False, default="password")
    profile_photo = models.ImageField(upload_to='images/', blank=True, null=True)
    public_id = models.CharField(max_length=200, unique=True, default="password")

    def __str__(self):
        return self.user_name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comm_title = models.CharField(max_length=200, null=True)
    comm_type = models.CharField(max_length=200, null=True)
    comm_desc = models.TextField(blank=True)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.commentor


class Followers(models.Model):
    follower = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # users_followed = models.ManyToManyField(User, related_name='user_followers', null=True)

    blog_followed = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
