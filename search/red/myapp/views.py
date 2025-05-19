from django.shortcuts import render,redirect
from myapp.models import Record

def index(request):
    records = Record.objects.all()
    start_date = request.GET.get('start')
    end_date = request.GET.get('end')
    if start_date and end_date:
        records = records.filter(date__range=[start_date, end_date])
    return render(request, 'index.html', {'records': records})

def new(request):
	if request.method == "POST":
		name = request.POST.get("name")
		date = request.POST.get("date")
		record = Record(name=name,date=date)
		record.save()
		return redirect('/')
 	