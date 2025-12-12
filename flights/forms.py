from django import forms

class SearchForm(forms.Form):
    source = forms.CharField(max_length=50)
    destination = forms.CharField(max_length=50)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    seats = forms.IntegerField(min_value=1)
