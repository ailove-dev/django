# -*- coding: utf-8 -*-

from django import http


try:
    import settings 
    XHR_SHARING_ALLOWED_ORIGINS = settings.XHR_SHARING_ALLOWED_ORIGINS
    XHR_SHARING_ALLOWED_METHODS = settings.XHR_SHARING_ALLOWED_METHODS
except:
    XHR_SHARING_ALLOWED_ORIGINS = '*'
    XHR_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']


class XhrSharing(object):
    def process_request(self, request):
        if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
            response = http.HttpResponse()
            response['Access-Control-Allow-Origin'] = XHR_SHARING_ALLOWED_ORIGINS
            response['Access-Control-Allow-Methods'] = ','.join(XHR_SHARING_ALLOWED_METHODS)

            return response

        return None

    def process_response(self, request, response):
        if response.has_header('Access-Control-Allow-Origin'):
            return response

        response['Access-Control-Allow-Origin'] = XHR_SHARING_ALLOWED_ORIGINS
        response['Access-Control-Allow-Methods'] = ','.join(XHR_SHARING_ALLOWED_METHODS)

        return response
