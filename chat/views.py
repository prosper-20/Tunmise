from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

def home(request):
    return render(request, "chat/home.html")


# def contact_us(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Thanks for contacting us!!")
#             return redirect("https://gigm.com/select-bus")
#         else:
#             messages.error(request, "Something went wrong!!")
#             return redirect("contact")
        
#     else:
#         form = ContactForm()

#     context = {"form": form}
#     return render(request, "chat/contact.html", context)

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return redirect("contact")
    else:
        form = ContactForm()
    context = {"form": form}
    return render(request, "chat/contact.html", context)
