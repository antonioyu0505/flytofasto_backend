from rest_framework import renderers

class ApiRenderer(renderers.JSONRenderer):
    
  def render(self, data, accepted_media_type=None, renderer_context=None):
    status_code = renderer_context['response'].status_code
    response = {
      "status": "success",
      "code": status_code,
      "data": data
    }
    if(not str(status_code).startswith('2')): response["status"] = "error"
    return super(ApiRenderer, self).render(response, accepted_media_type, renderer_context)