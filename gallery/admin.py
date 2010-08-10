from django.contrib import admin
from imagesearch.gallery.models import Annotation, AnnotationOwner, AnnotationObject

admin.site.register(AnnotationOwner)
admin.site.register(Annotation)
admin.site.register(AnnotationObject)
