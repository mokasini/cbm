#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This file is part of CbM (https://github.com/ec-jrc/cbm).
# Author    : Gilbert Voican, Konstantinos Anastasakis
# Credits   : GTCAP Team
# Copyright : 2021 European Commission, Joint Research Centre
# License   : 3-Clause BSD


from ipywidgets import Tab
from cbm.ipycbm.ipy_foi import foi_settings, foi_panel, foi_help

def foi_widget_box():

    tab_box = Tab(children=[foi_panel.foi(), foi_panel.foi_v2(), foi_help.widget_box_foi(),
                  foi_settings.widget_box()])

    tab_box.set_title(0, 'FOI Assessment V1')
    tab_box.set_title(1, 'FOI Assessment V2')
    tab_box.set_title(2, 'Help')
    tab_box.set_title(3, 'Settings')

    return tab_box
