class RetrieveMixin:
    def get(self, request):
        return "GET: " + request.get('url')


class CreateMixin:
    def post(self, request):
        return "POST: " + request.get('url')


class UpdateMixin:
    def put(self, request):
        return "PUT: " + request.get('url')


class GeneralView:
    allowed_methods = ('GET', 'POST', 'PUT', 'DELETE')

    def render_request(self, request):
        if not request.get('method').upper() in self.allowed_methods:
            raise TypeError(f"Method {request.get('method')} is not allowed.")

        method_name = request.get('method').lower()
        method = getattr(self, method_name)
        return method(request)


class DetailView(RetrieveMixin, UpdateMixin, GeneralView):
    allowed_methods = ('GET', 'PUT', )


view = DetailView()
html = view.render_request({'url': 'https://google.com', 'method': 'Get'})
print(html)
