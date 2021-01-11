from rest_framework import renderers


# Define Renderer for media_type Images
class JPEGRenderer(renderers.BaseRenderer):
    media_type = 'image/*'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


# Define Renderer for media_type Images
class PDFRenderer(renderers.BaseRenderer):
    media_type = 'application/PDF'
    format = 'pdf'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data


# Define a Binary Renderer class that outputs as a binary data
class BinaryRenderer(renderers.BaseRenderer):
    media_type = '*/*'
    charset = None
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        return data
