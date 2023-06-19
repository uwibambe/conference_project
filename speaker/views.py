from django.shortcuts import render

speakers = [
        {
            "id": 'A',
            "name": "INFORMATION TECHNOLOGY",
            "date": "2005-01-01",
            "location": "HUYE"
        },
        {
            "id": 'B',
            "name": "COMPUTER SCIENCE",
            "date": "2019-06-07",
            "location": "NYAGATARE"
        },
        {
            "id": 'C',
            "name": "COMPUTER ENGINNER",
            "date": "2022-04-12",
            "location": "BUTARE"
        },

        {
            "id": 'D',
            "name": "ACCOUNTING",
            "date": "2021-11-23",
            "location": "ESFB"
        },

        {
            "id": 'E', 
            "name": "Forest",
            "date": "2021-07-23",
            "location": "kigali"
        },
    ]
def speaker_view(request):
    return render(request, 'speaker.html', context={"speaker": speakers})
def create_speaker_view(request):
    return render (request,'create_speak.html')

def speaker_id(request,id):
    return render(request,'speaker_id.html')

def speaker_update(request,update):
    return render(request, 'speaker_update.html')

def speaker_delete(request,speaker_id):
    return render (request, 'speaker_delete.html')