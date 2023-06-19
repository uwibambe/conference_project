from django.shortcuts import render

conferences = [
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
def conferences_view(request):
    return render(request, 'conferences.html', context={"conferences": conferences})
def create_conference_view(request):
    return render (request,'create_conf.html')
