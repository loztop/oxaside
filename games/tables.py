import django_tables2 as tables
from games.models import Game

class GameTable(tables.Table):
    #user = tables.Column(verbose_name="User")
    game_text = tables.Column(verbose_name="Details")
    contact_text = tables.Column(verbose_name="Contact")
    location_text = tables.Column(verbose_name="Location")
    players_needed = tables.Column(verbose_name="Spaces")
    kickoff_date = tables.Column(verbose_name="Kickoff")

    class Meta:
        model = Game
        # add class="paleblue" to <table> tag
        attrs = {'class': 'paleblue'}
        fields = ('game_text','contact_text','location_text','kickoff_date','players_needed',)



#class UserTable(tables.Table):
#    game_text = tables.Column(verbose_name="Details")
#    contact_text = tables.Column(verbose_name="Contact")
#    location_text = tables.Column(verbose_name="Location")
#    players_needed = tables.Column(verbose_name="Spaces",accessor=4)
#    kickoff_date = tables.Column(verbose_name="Kickoff")

#    class Meta:
#        model = Game
#        # add class="paleblue" to <table> tag
#        attrs = {'class': 'paleblue'}
#        fields = ('game_text','contact_text','location_text','kickoff_date','players_needed',)