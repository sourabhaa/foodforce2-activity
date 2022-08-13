from sugar3.activity import activity
from gettext import gettext as _
import Foodforce2

class Activity(activity.Activity):
    """Your Sugar activity"""
    def __init__(self, handle):
        activity.Activity.__init__(self, handle)
        self.game = Foodforce2
        self.game.main()
        game_name = 'Foodforce2:main'
        game_title = _('FoodForce2')
        game_size = None
