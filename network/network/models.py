from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass



class Post(models.Model):
    reporter = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_posts")
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    like= models.IntegerField()
    
   
    def serialize(self):
        return {
            "id": self.id,
            "reporter": self.reporter,
            "text": self.text,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "like": self.like,
         }

class Read_Post(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_r")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_r")
    read = models.BooleanField(default=False)


class like_Post(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="post_l")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_l")
    like_user = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.post} {self.user} {self.like_user}"

class Follower(models.Model):
    user_p = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_p")
    user_f = models.ForeignKey("User", on_delete=models.CASCADE, related_name="user_f")

    def __str__(self):
        return f"{self.user_p} {self.user_f}"

