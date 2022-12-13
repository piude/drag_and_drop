from django.shortcuts import render
from .models import FileUploader
from .forms import FileUploaderForm

# Create your views here.
def add(request):
	form = FileUploaderForm(request.POST)
	context = {}
	if request.method == "POST":
		if form.is_valid():
			form.save()
			return redirect('list/')
	context['form'] = form
	return render(request, 'add.html', context)


def list(request):
	context = {}
	context['files'] = FileUploader.objects.all()
	return render(request, 'list.html', context)


def detail(request, id):
	context = {}
	context['file'] = FileUploader.objects.get(id=id)
	return render(request, 'detail.html', context)
