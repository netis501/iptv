# -*- coding: utf-8 -*-
#  enigma2 iptv player
#
#  Copyright (c) 2018 Alex Maystrenko <alexeytech@gmail.com>
#
# This is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2, or (at your option) any later
# version.

from __future__ import print_function

# plugin imports
from m3u import M3UProvider


class OTTProvider(M3UProvider):
	NAME = "EdemTV-Yahan"

	def __init__(self, username, password):
		super(OTTProvider, self).__init__(username, password)
		self.site = "http://technic.cf/epg"
		self.playlist = "edem_pl.m3u8"
		self.playlist_url = "http://epg.it999.ru/edem_epg_ico.m3u8"
