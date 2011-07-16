#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initial setup file"""
import  settings
from users import User

# add admin user
admin = User(settings.ADMIN, settings.ADMIN_PASSWORD, is_admin=True)
admin.save()



