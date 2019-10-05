import os
import json
import base64
from PIL import Image
from django.conf import settings as stg
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from app.models import APP_Photo
# Create your views here.


class AppIndex(TemplateView):
    template_name = 'app_index.html'


    def get(self, request, *args, **kwargs):
        photos = APP_Photo.objects.order_by('-likes')
        return render(
            request,
            self.template_name,
            {
                'photos': photos
            })

    def post(self, request, *args, **kwargs):
        try:
            os.makedirs(os.path.join(stg.PROJECT_ROOT, 'files/uploads'))
        except Exception as e:
            print(".................ERROR makedirs in uploader_pic.................")

        f = request.POST['slim[]']
        xdata = json.loads(f)
        name = xdata['input']['name'].replace(' ', '-')
        full_filename = os.path.join(stg.PROJECT_ROOT, 'files/uploads', name)
        image = open(full_filename, "wb")
        img = xdata['output']['image']
        image_type = 'JPEG'
        if 'data:image/jpg;' in img:
            image_type = 'JPEG'
        elif 'data:image/png;' in img:
            image_type = 'PNG'
        elif 'data:image/gif;' in img:
            image_type = 'GIF'
        elif 'data:image/bmp;' in img:
            image_type = 'BMP'

        img = img.replace('data:image/jpeg;base64,', '')
        img = img.replace('data:image/jpg;base64,', '')
        img = img.replace('data:image/png;base64,', '')
        img = img.replace('data:image/bmp;base64,', '')
        img = img.replace('data:image/git;base64,', '')
        img = img.encode()
        image.write(base64.decodestring(img))
        image.close()
        file, ext = os.path.splitext(full_filename)
        #import ipdb; ipdb.set_trace()

        return HttpResponseRedirect('/')
