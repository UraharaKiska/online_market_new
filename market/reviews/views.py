from django.shortcuts import render


from django.http import HttpResponse
from django.shortcuts import render


def show_all_reviews(request):
    return render(request, 'reviews/show_all.html')


def leave_review(request):
    return render(request, 'reviews/leave_reviews.html')
    


