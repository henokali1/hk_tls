from django.shortcuts import render

def index(request):
    apps = [
        {
            'name': 'Dead Hang',
            'description': 'Track and improve your grip strength with the ultimate hang timer.',
            'url': '/dead-hang/',
            'icon': '⏱️',
            'color': '#38bdf8',
        },
        # Add more apps here in the future
    ]
    return render(request, 'dashboard/index.html', {'apps': apps})
