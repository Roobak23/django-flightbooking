from django.shortcuts import render, redirect, get_object_or_404
from .models import Flight, Booking
from .forms import SearchForm, BookingForm
from django.contrib.auth.decorators import login_required


def home(request):
    form = SearchForm()
    context = {'form': form}

    return render(request, 'flights/home.html', context)

def search_flights(request):
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            flights = Flight.objects.filter(
                source__icontains=form.cleaned_data['source'],
                destination__icontains=form.cleaned_data['destination'],
                date=form.cleaned_data['date']
            )
            return render(request, 'flights/search.html', {'flights': flights})

    return redirect('/')



@login_required

def book_flight(request, id):
    flight = get_object_or_404(Flight, id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        seats = request.POST.get("seats")

        Booking.objects.create(
            flight=flight,
            name=name,
            email=email,
            seats=seats
        )
        
        return render(request, 'flights/success.html', {"flight": flight})

    return render(request, 'flights/book.html', {"flight": flight})


