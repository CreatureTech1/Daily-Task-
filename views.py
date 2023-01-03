from django.shortcuts import render
from django.contrib.auth.models import User
from .models import FacebookResponse

# Create your views here.
import facebook

def get_user_profile(request):
    # Get the user's access token
    #access_token = request.GET.get('access_token')
    access_token = 'EAAGlTazvDuoBALYLXgsdGT50LXxAXAFc1r4t7mSHd27lbk3ZAVVjCaO88XD0o64WHFn3C16rYKIn5BZBTZBigY065M3ma4Tyy0hYW14KzvnzQFXA1zpSL2eInPZBdKTuDbZBjeoPSEpZB7e41yx8tkBS8GTgnfrh2dNPajJvFqQBw5aYKyDaRsLf2DdmalirtmDYf5PYw2evcJQZAHQcY7e9CjDWpZBwZCyBLMQtcOKDbLQKU0ROjCihZCANd4ZBUxQCP8ZD'
    # Initialize the Facebook Graph API client
    graph = facebook.GraphAPI(access_token=access_token, version='3.1')
    
    # Get the user's profile information
    #profile = graph.get_object(id='me', fields='id,name,email')

    response = graph.get_object(id='me', fields='id,name,email')
    
    # Create a new FacebookResponse object and save it to the database
    responses = FacebookResponse(
        facebook_id=response['id'],
        name=response['name'],
        email=response['email']
    )
    responses.save()

    responses = FacebookResponse.objects.all()

    for responsee in responses:
        print(responsee.name)
        print(responsee.email)
        print(responsee.facebook_id)

    
    
    return render(request, 'response.html', {'response': response})
    
    
    #return render(request, 'profile.html', {'profile': profile})




'''
if request.method == "GET":
        #username = request.POST.get('username',False)
        userid = request.GET.get("id")
        username = request.GET.get('name')
        #lname = request.POST['lname']
        email = request.GET.get('email')
        #pass1 = request.POST['pass1']
        #pass2 = request.POST['pass2']

        myuser = User.objects.create_user[userid,username,email]
        #myuser.first_name = fname
        #myuser.last_name = lname

        myuser.save()
'''