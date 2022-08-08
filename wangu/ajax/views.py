from django.shortcuts import render

# Create your views here.

def ajax_contact_list(request):
    return render(request,'ajax/ajaxcontacts.html')

