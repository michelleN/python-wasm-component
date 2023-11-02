from http_app import exports

from http_app.imports.types import (
    IncomingRequest,
    OutgoingResponse,
    ResponseOutparam,
    OutgoingBody,
    Fields,
    Ok,
)


class IncomingHandler(exports.IncomingHandler):
    def handle(self, request: IncomingRequest, response_out: ResponseOutparam):
        response = OutgoingResponse(200, Fields([("HELLO", b"WORLD")]))

        ResponseOutparam.set(response_out, Ok(response))
