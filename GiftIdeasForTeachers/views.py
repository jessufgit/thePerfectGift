from django.shortcuts import render
from .forms import PriceForm
from .forms import NewGiftForm
from GiftIdeasForTeachers.models import Gift
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
def price_range(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populates it with data from the request:
        form = PriceForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect the user entered data to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PriceForm()

    # this is the line that actually returns the form where the user inputs the data on the page where you want the form to exist.
    return render(request, 'index.html', {'form': form})

def giftsFiltered(request): ## When thanks loads as a result of the form being submitted, it saves the user entered info from the PriceForm and renders it to the html indicated. 
##		giftImage, comment, price, webAddress, giftTitle
	spendingInfo=request.POST.get('price_cap', False)
	teacherLikes=request.POST.get('likes', False)
	subjectTaught=request.POST.get('subject', False)
	likesCoffee=request.POST.get('coffee', False)
	isFunny=request.POST.get('hasASenseOfHumor', False)
	hasKids=request.POST.get('hasChildren', False)
	likesSports=request.POST.get('sportsFan', False)

	gifts = Gift.objects.all()
	allgifts = Gift.objects.all()
	kidgifts = Gift.objects.none()
	sportsgifts = Gift.objects.none()

	if (likesCoffee == "notcoffee"):
		gifts = gifts.exclude(comment__contains="mug").exclude(comment__contains="coffee").exclude(comment__contains="Starbucks")
	if (isFunny == "notfunny"):
		gifts = gifts.exclude(comment__contains="laugh").exclude(giftTitle__contains="funny").exclude(comment__contains="kick").exclude(comment__contains="humor")
	if (subjectTaught != ""):
		gifts = gifts.filter(comment__contains=subjectTaught).filter(giftTitle__contains=subjectTaught)

	if (hasKids == "kids"):
		kidgifts = allgifts.filter(comment__contains="family")
	if (likesSports == "sports"):
		sportsgifts = allgifts.filter(comment__contains="sports")

	gifts = gifts.union(kidgifts, sportsgifts)
	gifts = gifts.order_by('price')

#	if (spendingInfo >= 'price'):
#		gifts = gifts.exclude(price__isexact=spendingInfo)
#	if (teacherLikes != ""):
#		gifts = gifts.filter(comment__contains=teacherLikes)
#		if not gifts:
#			gifts = Gift.objects.all()
	return render(request, 'thanks.html', {'spendingInfo':spendingInfo, 'teacherLikes':teacherLikes, 'subjectTaught':subjectTaught, 'likesCoffee':likesCoffee, 'isFunny':isFunny, 'hasKids':hasKids, 'likesSports':likesSports, 'gifts':gifts})

def newForm(request):
	if request.method == 'POST':
		form = NewGiftForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/thanksagain/')
	else:
		form = NewGiftForm()

	return render(request, 'addYourGift.html', {'form': form})

def userCreatedGift(request):
	title=request.POST['giftTitle']
	price=request.POST['price']
	image=request.POST['image']
	address=request.POST['webAddress']
	comment=request.POST['comment']

	newGift = Gift.objects.create(giftTitle=title, price=price, image=image, webAddress=address, comment=comment)

	return render(request, 'thanksagain.html', {'title':title})



	


