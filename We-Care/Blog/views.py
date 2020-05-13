from django.shortcuts import render, redirect
from django.views import generic
from Blog.models import BlogPost, Images
from Blog.forms import PostForm, ImageForm
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.template import RequestContext


class BlogPostList(generic.ListView):
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blogs.html'

class BlogPostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blogpost_detail.html'

@login_required
def createBlogPost(request):

    ImageFormSet = modelformset_factory(Images, form = ImageForm, extra=3)

    if request.method == 'POST':      
        formset = ImageFormSet(request.POST, request.FILES, queryset=Images.objects.none())
        postForm = PostForm(request.POST)

        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.author = request.user
            post_form.status = 1
            post_form.save()

            for form in formset.cleaned_data:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
            
            messages.success(request,
                             "Posted!")
            return redirect("blogs")
        else:
            messages.error(request, "Some errors occured")
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Images.objects.none())
    return render(request, 'blog/create_blog_post.html',
                  {'postForm': postForm, 'formset': formset})