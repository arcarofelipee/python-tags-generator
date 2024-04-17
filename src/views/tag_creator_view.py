from src.views.http_types.http_request import HttpResquest
from src.views.http_types.http_response import HttpResponse
from src.controller.tag_creator_controller import CreateTagController

class TagCreatorView:
  def validade_and_create(self, http_request: HttpResquest) -> HttpResponse:
    tag_creator_controller = CreateTagController()

    body = http_request.body
    product_code = body["product_code"]

    formatted_response = tag_creator_controller.create(product_code)

    return HttpResponse(status_code=200, body=formatted_response)