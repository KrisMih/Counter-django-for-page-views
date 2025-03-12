from django.shortcuts import render
from .models import VisitCount

def count_visits(request):
    visit, created = VisitCount.objects.get_or_create(id=1)
    visit.count += 1
    visit.save()
    return render(request, 'counts.html', {'count': visit.count})


