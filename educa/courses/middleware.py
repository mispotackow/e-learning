from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Course


def subdomain_course_middleware(get_response):
    """
    Поддомены для курсов
    """
    def middleware(request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':
            # получить курс для данного поддомена
            course = get_object_or_404(Course, slug=host_parts[0])
            course_url = reverse('course_detail', args=[course.slug])
            # перенаправить текущий запрос в представление course_detail
            url = '{}://{}{}'.format(request.scheme, '.'.join(host_parts[1:]), course_url)
            return redirect(url)

        response = get_response(request)
        return response
    return middleware
