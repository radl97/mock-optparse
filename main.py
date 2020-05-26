from youtube_dl.options import parseOpts

(parser, _, _) = parseOpts()

print(parser.data)
