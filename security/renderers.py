from rest_framework import renderers


# Define Renderer for media_type Images
class ImageRenderer(renderers.BaseRenderer):
    media_type = 'image/*'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


# Define Renderer for media_type PDF
class PDFRenderer(renderers.BaseRenderer):
    media_type = 'application/PDF'
    format = 'pdf'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


# Define a Renderer class that outputs as text file
class FileRenderer(renderers.BaseRenderer):
    media_type = 'text/plain'
    charset = None

    def render(self, data, media_type=None, renderer_context=None):
        return data


# Define Renderer for media_type Octlet Stream
class OctetRenderer(renderers.BaseRenderer):
    media_type = 'application/octet-stream'
    format = 'pdf'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
