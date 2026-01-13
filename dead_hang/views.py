import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Max, Count
from .models import HangSession

def index(request):
    return render(request, 'dead_hang/index.html')

def stats(request):
    sessions = HangSession.objects.all().order_by('timestamp')
    best_hang = sessions.aggregate(Max('duration'))['duration__max'] or 0
    avg_hang = sessions.aggregate(Avg('duration'))['duration__avg'] or 0
    total_sessions = sessions.count()
    
    context = {
        'best_hang': round(best_hang, 2),
        'avg_hang': round(avg_hang, 2),
        'total_sessions': total_sessions,
        'sessions_json': json.dumps([
            {'date': s.timestamp.strftime('%Y-%m-%d %H:%M'), 'duration': s.duration}
            for s in sessions
        ])
    }
    return render(request, 'dead_hang/stats.html', context)

@csrf_exempt
def save_result(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            duration = float(data.get('duration'))
            session = HangSession.objects.create(duration=duration)
            return JsonResponse({'status': 'success', 'id': session.id})
        except (ValueError, TypeError, json.JSONDecodeError):
            return JsonResponse({'status': 'error', 'message': 'Invalid data'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)

@csrf_exempt
def clear_data(request):
    if request.method == 'POST':
        HangSession.objects.all().delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
