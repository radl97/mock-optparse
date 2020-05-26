# stubs for replacing optparse

SUPPRESS_HELP=None

class IndentedHelpFormatter:
	def __init__(self, **argv):
		pass

class OptionGroup:
	def __init__(self, _, name):
		print(name)
		pass

	def add_option(self, a, b=None, c=None, **argv):
		print(a, b, argv)

class OptionParser:
	def __init__(self, **argv):
		print(argv)
		pass

	def add_option_group(self, _):
		pass

	def parse_args(self, _):
		# Last option
		exit(0)
