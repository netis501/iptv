# -*- coding: utf-8 -*-
#  enigma2 iptv player
#
#  Copyright (c) 2020 Alex Maystrenko <alexeytech@gmail.com>
#
# This is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2, or (at your option) any later
# version.

from __future__ import print_function

# system imports
import random
import urllib
from urllib2 import HTTPError
from json import loads as json_loads

# plugin imports
from abstract_api import OfflineFavourites
from ..utils import APIException, APILoginFailed, EPG, Channel, Group


class OTTProvider(OfflineFavourites):
	NAME = "AntiFriz"
	AUTH_TYPE = "Key"

	def __init__(self, username, password):
		super(OTTProvider, self).__init__(username, password)
		self.playlist_url = "https://antifriz.tv/api/enigma/%s" % username
		self.api_site = "http://api.iptvx.tv/"
		self._token = password
		self.web_names = {}
		self.urls = {}

	def start(self):
		try:
			reply = self.readHttp(self.playlist_url)
		except HTTPError as e:
			self.trace("HTTPError:", e, type(e), e.getcode())
			if e.code in (403, 404):
				raise APILoginFailed(e)
			else:
				raise APIException(e)
		except IOError as e:
			self.trace("IOError:", e, type(e))
			raise APIException(e)
		try:
			json = json_loads(reply)
		except Exception as e:
			raise APIException("Failed to parse json: %s" % str(e))
		self._parseChannels(json)

	def _getJson(self, url, params):
		try:
			self.trace(url)
			reply = self.readHttp(url + urllib.urlencode(params))
		except IOError as e:
			raise APIException(e)
		try:
			json = json_loads(reply)
		except Exception as e:
			raise APIException("Failed to parse json: %s" % str(e))
		# self.trace(json)
		return json

	def _parseChannels(self, channelsData):
		self.channels = {}
		self.groups = {}
		self.web_names = {}
		self.urls = {}
		group_names = {}
		for number, ch in enumerate(channelsData):
			group = ch['category'].encode('utf-8')
			try:
				gid = group_names[group]
				g = self.groups[gid]
			except KeyError:
				gid = len(group_names)
				group_names[group] = gid
				g = self.groups[gid] = Group(gid, group, [])

			cid = hash(ch['web_name'])
			c = Channel(cid, ch['name'].encode('utf-8'), number, bool(ch['archive']), False)
			self.channels[cid] = c
			self.web_names[cid] = ch['web_name'].encode('utf-8')
			self.urls[cid] = ch['url'].encode('utf-8')
			g.channels.append(c)

	def getStreamUrl(self, cid, pin, time=None):
		if time is None:
			ALPHA_NUM = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
			salt = ''.join(random.choice(ALPHA_NUM) for _ in range(5))
			return "%s_%s" % (self.urls[cid], salt)
		url = self.urls[cid]
		return url.replace(':80/', ':1600/s/%s/' % self.username) + '&utc=%s' % time.strftime('%s')

	def getDayEpg(self, cid, date):
		data = self._getJson(self.api_site + "/epg/%s/?" % self.web_names[cid], {"date": date.strftime("%Y-%m-%d")})
		return [
			EPG(e['time'], e['time_to'], e['name'].encode('utf-8'), e['descr'].encode('utf-8'))
			for e in data
		]

	def getChannelsEpg(self, cids):
		data = self._getJson(self.api_site + "/epg/current", {})
		for c in data:
			yield hash(c['alias']), [
				EPG(e['time'], e['time_to'], e['name'].encode('utf-8'), e['descr'].encode('utf-8'))
				for e in c['epg']
			]
