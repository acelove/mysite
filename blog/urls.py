#!/usr/bin/env python
# coding=utf-8
from django.conf.urls import *
from blog.views import archive

urlpatterns = [
    url(r'^$',archive),
]
