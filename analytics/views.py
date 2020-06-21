import datetime

from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from analytics.models import Navigation


@api_view(['POST'])
def create_navigation(request):
    user = request.data.get('user')
    session = request.data.get('session')
    path = request.data.get('path')

    Navigation.objects.create(user=user, session=session, path=path)

    return Response({
        'message': True,
        'status_code': 200
    })


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')

    # Todo: Use from and to dates to filter navigation data dashboard from frontend
    if from_date and to_date:
        navigations = Navigation.objects.filter(access_time__lte=to_date, access_time__gte=from_date)
    else:
        navigations = Navigation.objects.all()

    # Main kpis
    user_count = navigations.distinct('user').count()
    session_count = navigations.distinct('session').count()
    path_count = navigations.exclude(path='/').distinct('path', 'session').count()

    # Chart labels and dataset construction
    today = datetime.date.today()
    dates = [(today - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(6, -1, -1)]
    values = [navigations.filter(access_time__date=date).count() for date in dates]
    sessions_by_day = {
        'dates': dates,
        'data': values
    }

    # Table construction
    path_by_day = navigations.values(
        'path',
        'access_time__date',
    ).annotate(
        count=Count('path'),
    )

    return Response({
        'user_count': user_count,
        'session_count': session_count,
        'path_count': path_count,
        'sessions_by_day': sessions_by_day,
        'path_by_day': path_by_day,
    })
