#!/usr/bin/python

import dota2api

steam_key_api = '6DCDB66D280F81DFDB0644055CDFD6F2'
api = dota2api.Initialise(steam_key_api)
match = api.get_match_details(match_id=1000193456)

print match
