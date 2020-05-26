from youtube_dl.options import parseOpts
import json

(parser, _, _) = parseOpts()

for optionGroup in parser.data:
	for option in optionGroup['options']:
		if 'type' in option['named']:
			v = option['named']['type']
			# "type" cannot be encoded. Use the name of it instead.
			if isinstance(v, type):
				v = v.__name__
			option['named']['type'] = v
		# function cannot be encoded, we can just note that there is one
		if 'callback' in option['named']:
			option['named']['callback'] = True
print(json.dumps({'data': parser.data}))
