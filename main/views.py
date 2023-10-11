from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Post
from .forms import ReviewForm



class PostDetialView(DetailView):
    model=Post
    slug_field='url'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] =ReviewForm()
        
        return context

class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST, request.FILES)
        post=Post.objects.get(id=pk)
        if form.is_valid:
            form=form.save(commit=False)
            # print("Photo path: ", form.cleaned_data['photo'].path)
            if request.POST.get("parent", None):
                form.parent_id=int(request.POST.get("parent"))
            form.post=post
            form.save()
        return redirect(post.get_absolute_url())






