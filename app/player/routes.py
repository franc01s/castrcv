from flask import render_template
from . import player

@player.route('/')
def root():
    return render_template('player/player.html')
