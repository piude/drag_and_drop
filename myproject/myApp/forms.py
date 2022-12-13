from .models import FileUploader
from django import forms

class FileUploaderForm(forms.ModelForm):
	class Meta:
		model = FileUploader
		fields = '__all__'