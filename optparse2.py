# stubs for replacing optparse

SUPPRESS_HELP=None

class IndentedHelpFormatter:
	def __init__(self, **argv):
		pass

class OptionGroup:
	def __init__(self, _, name):
		self.data = { "name": name, "options": [] }
		pass

	def add_option(self, *args, **argv):
		self.data["options"].append({"positional": args, "named": argv})

class FakeOpts:
	def __init__(self):
		self.verbose = False

class OptionParser:
	def __init__(self, **argv):
		self.data = []
		pass

	def add_option_group(self, optionGroup):
		self.data.append(optionGroup.data)
		pass

	def parse_args(self, *args):
		# This is called only after last option added.
		# Dump output or do whatever :)
		return (FakeOpts(), None)
