import typing, http
from fastapi import Request

# from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import ASGIApp, Message, Scope, Receive, Send


class CustomHTTPException(Exception):
    def __init__(self, status_code: int, detail: typing.Optional[dict] = None) -> None:
        if detail is None:
            detail = http.HTTPStatus(status_code).phrase
        self.status_code = status_code
        self.detail = detail

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(status_code={self.status_code!r}, detail={self.detail!r})"


from .helpers import decrypt_rsa


# class DecryptionMiddleware(BaseHTTPMiddleware):
#     # def __init__(self, app):
#     #     super().__init__(app)

#     async def dispatch(self, request: Request, next_call):
#         encrypted_data = await request.body()
#         if encrypted_data := encrypted_data.decode("utf-8"):
#             decrypted_data = self.decrypt_request(encrypted_data)
#             request._body = decrypted_data
#         response = await next_call(
#             Request(request.scope, request.receive, request._send)
#         )
#         return response


#     def decrypt_request(self, encrypted_data):
#         decrypted_data = decrypt_rsa(encrypted_data)
#         return decrypted_data
class DecryptionMiddleware:
    def __init__(self, app: ASGIApp):
        self.app = app

    # async def __call__(self, request: Request, next_call):
    #     encrypted_data = await request.body()
    #     if encrypted_data := encrypted_data.decode("utf-8"):
    #         decrypted_data = self.decrypt_request(encrypted_data)
    #         request._body = decrypted_data
    #     response = await next_call(
    #         Request(request.scope, request.receive, request._send)
    #     )
    #     return response

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            return await self.app(scope, receive, send)

        async def receive_decrypted_request_body():
            message = await receive()
            if encrypted_data := message.get("body").decode("utf-8"):
                decrypted_data = decrypt_rsa(encrypted_data)
                print(decrypted_data)
                return {"type": "http.request", "body": decrypted_data}
            return message

        await self.app(scope, receive_decrypted_request_body, send)

    def decrypt_request(self, encrypted_data):
        decrypted_data = decrypt_rsa(encrypted_data)
        return decrypted_data
