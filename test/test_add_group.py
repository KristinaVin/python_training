# -*- coding: utf-8 -*-
from model.group import Group





def test_add_group(app):
    app.group.create(Group(name="dsvv", header="sdvsdv", footer="svdsv"))



def test_add_empty_group(app):
     app.group.create(Group(name="", header="", footer=""))

