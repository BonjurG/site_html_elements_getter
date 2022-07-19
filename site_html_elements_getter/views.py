import http

from rest_framework.response import Response
from rest_framework.views import APIView

from celery.result import AsyncResult

from site_html_elements_getter.tasks import parse_page


class TagsView(APIView):
    def get(self, request, task_id: str) -> Response:
        task = AsyncResult(id=task_id)
        payload = ''
        if task.ready():
            payload = {"HTML tags": task.get()}
        else:
            payload = f'The task {task_id} now in {task.status} status'
        return Response(status=http.HTTPStatus.OK, data=payload)

    def post(self, request) -> Response:
        site_url = request.data.get("url")
        if site_url:
            task = parse_page.delay(site_url)
            return Response(status=http.HTTPStatus.CREATED, data=task.id)
        return Response(status=http.HTTPStatus.BAD_REQUEST)
