from django.shortcuts import render
from models import MyCustomProfile
from django.conf import settings 

def home(request):

	if request.user and not request.user.is_anonymous():
		profile = MyCustomProfile.objects.get( user = request.user )
		image = settings.STATIC_URL + profile.image.url
	else:
		image = False
	
	return render( request,'index.html', { 'image' : image } )