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

from datetime import datetime, timedelta

# from api.abstract_api import AbstractStream
from utils import trace, APIException, EPG
from layer import eTimer

try:
	from typing import List, Dict, Callable, Tuple  # pylint: disable=unused-import
except ImportError:
	pass


class LiveEpgWorker(object):
	"""
	This class always has most recent live epg for all channels
	"""

	def __init__(self, db):
		self.onUpdate = []  # type: List[Callable[ [List[Tuple[int, EPG]]], None ]]
		self.db = db  # type: AbstractStream
		self._timer = eTimer()
		self._timer.callback.append(self.update)
		self._epg = {}  # type: Dict[int, List[EPG]]
		if len(self.db.channels):
			self.update()
		else:
			self.trace("No channels!")

	def trace(self, *args):
		trace("LiveEpgWorker", *args)

	def update(self):
		t = datetime.now()
		self.trace("update() at", t)
		if self._epg:
			self.trace(min([programs[0].end for programs in self._epg.values() if programs]))
			to_update = [cid for cid, programs in self._epg.items() if (programs and programs[0].end <= t)]
			self.trace("expired for", to_update)
		else:
			to_update = self.db.channels.keys()

		if to_update:
			try:
				data = self.db.getChannelsEpg(to_update)
				self._epg.update(data)
			except APIException as ex:
				self.trace("get data failed!", ex)
				self._timer.startLongTimer(60)  # retry in one minute
				return

			if not self._epg:
				self.trace("empty data! Stop.")
				return
		else:
			data = None
			self.trace("warning: already up to date")

		next_update = min(p.end for programs in self._epg.values() for p in programs[:1])
		self.trace("schedule to", next_update)
		diff = int((next_update + timedelta(seconds=1) - datetime.now()).total_seconds() * 1000)
		self._timer.start(max(60 * 1000, min(60 * 60 * 1000, diff)), True)  # 1 min < timer < 1 hour
		if data:
			self._runCallbacks(set(self._epg.keys()).intersection(set(to_update)))

	def _runCallbacks(self, channel_ids):
		new_data = []
		for cid in channel_ids:
			if self._epg[cid]:
				new_data.append((cid, self._epg[cid][0]))
		for func in self.onUpdate:
			func(new_data)

	def destroy(self):
		"""Call before del to avoid cycle references, because eTimer holds reference to self."""
		self._timer.callback.remove(self.update)
		self._timer.stop()

	def stop(self):
		self.trace("Stop.")
		self._timer.stop()

	def get(self, cid):
		try:
			return self._epg[cid][0]
		except (KeyError, IndexError):
			return None

	def getNext(self, cid):
		try:
			return self._epg[cid][1]
		except (KeyError, IndexError):
			return None
