""" Filename Changer
Pylename Changer? Probably not.
I guess since it's python now it needs a creative name.

This is mostly a staging ground for porting my filename changer over.
tkinter for the windows
glob
os
sys
string
itertools
functools?
files

Separate the code from the windows code
The window code can probably import the Filename Changer code?
that would make sense

Recursive directories will be so much easier!

Phylename Changer

Should there be classes? What would they be? Perhaps the different function thingies
so like
oh yes! because then I could have generators for creating serial numbers
I can scrape tvdb i guess
not really interested in that....

classes for the things
Fix Capitalization
Concatenate
Switch characters

Clicking on letters to select them
using a fixed width font
clicking and dragging the highlighting on the text box
or adding a line in between
colors?
so like

Original Text: xxxxxxxxx
Modified Text: xxxabcxxxx12xx
And see the changes real time like that?
I've thought of that before, but how to change?
a tree view?


alphafilename.txt
	betafilename01.txt
alphafilenname (2).txt
	betafilename02.txt

I think selection by highlighting is good to show what files will be effected by what rules

so why a class for the queue items?
what do I call the queue items?
queue_items sounds good.
QueueItems class holds all queue_items
QueueItems class holds all Qi type

What is the Qi type? (or Queue Item type, for long)
it is what all other queue types are.

it takes a filename (individual or list or sequence, probably)
it returns a filename

that's good enough for now!

Then, all QueueItem classes will inherit from the Qi type class.
I think that's how that works.
Or they subclass them
I can't remember if they're synonyms.


"""
class Qi():
	""" All QI types inherit from this
	"""
	def filename_to_modify(self, filename):
		""" Accepts and stores the filename being modified
		"""  

	def __str__(self, filename_to_modify):
		""" I think this is how I'd return a value from this class
		"""
	
	def __repr__(self):
		""" I don't think I need this but I don't yet know the difference between str and repr 
		"""





# TDD of course

# phone test 20180331
