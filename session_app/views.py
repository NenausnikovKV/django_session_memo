from django.http import HttpResponse

def index(request):
    origin_visit_count = request.session.get("visit_count", 0)
    request.session["visit_count"] = origin_visit_count + 1
    http_response = HttpResponse(f"Session request count  - {origin_visit_count}")
    return http_response


