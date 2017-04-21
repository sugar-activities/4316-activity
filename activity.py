#! /usr/bin/env python

from olpcgames import activity
from gettext import gettext as _

class Activity(activity.PyGameActivity):
    """Your Sugar activity"""
    
    game_name = 'conozcouy'
    game_title = _('Conozco Numeros')
    game_size = (1200,900)
