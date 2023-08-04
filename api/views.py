from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET', 'POST'])
def hello_world(request: Request, name: str=None) -> Response:
    if request.method == 'GET':
        if name:
            data = {"message": f"hello, {name}"}
        else:
            data = {"message": "hello, world"}

        return Response(data=data)

