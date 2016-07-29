# about interning

# @AndyK somestring = intern(somestring). Do this consistently 
# and there will only ever be one str object with that value in memory.
# Say you are processing a large body of text and you need to map 
# each word to some statistics. The corpus of text is really large, 
# there are a lot of words that'll be occurring often. 
# Your statistics include references to other words in 
# the corpus; say 'common next word' or something.
# Because you are reading this text from another source (file, network) 
# and splitting the text into words, you'll have a lot of string objects. 
# Many of those string objects will have the same value (e.g. "any" or "some"), 
# and each of those str objects takes memory.
# By interning those words, you tell Python to examine the value 
# and giving you the one copy it has stored already; so each time you 
# produce a separate word string you ask Python does this value already exist? 
# If so, give me the one singleton object for it.
# You use that one singleton copy everywhere. This can reduce memory significantly.

# It can also speed up dictionary lookups, as Python will first use is to see if a 
# given dictionary key in the hashed slot is the key you are testing with.
# @ByteCommander it makes the initial processing of strings ever so slightly slower 
# as there is an additional equality test being done, yes.
# But hey, 3GB!