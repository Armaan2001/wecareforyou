from django.shortcuts import render, redirect
from django.views import generic
from Confession.models import ConfessionPost
from Confession.forms import ConfessionForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required


class ConfessionPostList(generic.ListView):
    queryset = ConfessionPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'confession/confessions.html'

class ConfessionPostDetail(generic.DetailView):
    model = ConfessionPost
    template_name = 'confession/confessionpost_detail.html'

@login_required
def createConfessionPost(request):
    if request.method == 'POST':      
        form = ConfessionForm(request.POST)
        if form.is_valid():
            post_form = form.save(commit=False)
            post_form.author = request.user
            post_form.status = 1
            post_form.save(request)
            messages.success(request,
                             "Posted!")
            return redirect("confessions")
        else:
            messages.error(request, "Some errors occured")
    else:
        form = ConfessionForm()
    context = {
        'form':form
    }
    return render(request, 'confession/create_confession_post.html', context)
