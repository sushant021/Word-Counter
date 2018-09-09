from django import forms

class mainForm(forms.Form):
	maintext= forms.CharField(label='',widget= forms.Textarea(attrs={'placeholder':'Paste your text here','rows':'13','cols':'100'}))
	searchword = forms.CharField(label='Do you want to search a specific word?',widget=forms.TextInput(attrs={'placeholder':'Search Word'}))