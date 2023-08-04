from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request


@api_view(['GET', 'POST'])
def hello_world(request: Request, name: str=None) -> Response:
    if request.method == 'GET':
        # get query parameters from request
        params = request.query_params

        name = params.get('name')

    if request.method == 'POST':
        # get data from request
        data = request.data

        name = data.get('name')

    if name:
        data = {"message": f"hello, {name}"}
    else:
        data = {"message": "hello, world"}

    return Response(data)
