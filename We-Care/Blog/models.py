from django.db import models
import os
from django.conf import settings
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

def get_unique_slug(sender, instance, **kwargs):
    num = 1
    slug = slugify(instance.title)
    unique_slug = slug
    while BlogPost.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    instance.slug=unique_slug

pre_save.connect(get_unique_slug,sender=BlogPost)


def user_directory_path(instance,filename):
    base_name = os.path.basename(filename)
    name,ext = os.path.splitext(base_name)

    return "blog/user/"+ str(instance.post.author.id) + "/"+ str(instance.post.id)+ "/"+"IMG_"

class Images(models.Model):
    post = models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, null=True, blank=True)

    def __str__(self):
        return self.post.title + " Img"



