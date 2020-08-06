#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
                                                    __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
               ___-==_       _-~o~  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
          '         ~-|      /|    |-~\~~       __--~~
                      |-~~-_/ |    |   ~\_   _-~            /\
                           /  \     \__   \/~                \__
                       _--~ _/ | .-~~____--~-/                  ~~==.
                      ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                 -_     ~\      ~~---l__i__i__i--~~_/
                                 _-~-__   ~)  \--______________--~~
                               //.-~~~-~_--~- |-------~~~~~~~~
                                      //.-~~~--\
                               神兽保佑
                              代码无BUG!

"""

from django.shortcuts import render


def bad_request(request, exception, template_name='errorpages/400.html'):
    return render(request, template_name)


def permission_denied(request, exception, template_name='errorpages/403.html'):
    return render(request, template_name)


def page_not_found(request, exception, template_name='errorpages/404.html'):
    return render(request, template_name)


# 注意这里没有 exception 参数
def server_error(request, template_name='errorpages/500.html'):
    return render(request, template_name)
