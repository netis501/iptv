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

# system imports
from json import loads as json_loads

# plugin imports
from m3u import M3UProvider
from ..utils import Channel, APIException


class OTTProvider(M3UProvider):
	NAME = "WowTV"
	TVG_MAP = True

	def __init__(self, username, password):
		super(OTTProvider, self).__init__(username, password)
		self.site = "http://iptvdream.zapto.org/epg-it999/"
		self.playlist = "edem_pl.m3u8"
		self._tvg_info = {}

	def start(self):
		try:
			self._tvg_info = json_loads(self.readHttp('http://technic.cf/iptvdream4x/it999/tvg.json'))
		except IOError as e:
			self.trace("error!", e)
			raise APIException(e)

	def setChannelsList(self):
		m3u = self._locatePlaylist()
		with open(m3u) as f:
			self._parsePlaylist(f.read().split('\n'))

	def makeChannel(self, num, name, url, tvg, logo, rec):
		m = self._url_regexp.match(url)
		if m:
			cid = int(m.group(1))
		else:
			cid = hash(url)
		try:
			data = self._tvg_info[cid]
			tvg = data['tvg-id']
			logo = data['tvg-logo']
		except KeyError:
			pass
		return Channel(cid, name, num, rec), {'tvg': tvg, 'url': url, 'logo': logo}
