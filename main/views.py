from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from django.core.exceptions import ValidationError
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
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                if photo.size > 1024 * 1024:  # 1MB limit
                    return HttpResponse("Photo size should not exceed 1MB.", status=400)
            form=form.save(commit=False)
            
            if request.POST.get("parent", None):
                form.parent_id=int(request.POST.get("parent"))
            form.post=post
            form.save()
            return redirect(post.get_absolute_url())
        else:
            try:
                photo_error = form.errors['photo']
                print("NOTHING")
            except KeyError:
                photo_error = None
            return render(
                request,
                'main/post_detail.html',  
                {'form': form, 'photo_error': photo_error}
            )





