from django.db import models

import mongoengine
class message(mongoengine.Document):                    #交通信息
    t_type = mongoengine.StringField(max_length=60)
    t_no = mongoengine.StringField(max_length=200)
    t_date = mongoengine.DateTimeField(null=True)
    t_no_sub = mongoengine.StringField(max_length=200)
    t_pos_start = mongoengine.StringField(max_length=200)
    t_pos_end = mongoengine.StringField(max_length=200)
    t_memo = mongoengine.StringField(max_length=200)
    t_start = mongoengine.DateTimeField(null=True)
    t_end = mongoengine.DateTimeField(null=True)
    source = mongoengine.StringField(max_length=200)
    who = mongoengine.StringField(max_length=200)
    created_at = mongoengine.DateTimeField(null=True)
    updated_at = mongoengine.DateTimeField(null=True)
    verified = mongoengine.IntField(max_length=30)
