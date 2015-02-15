import pyak as pk
import time
import datetime

class MegaWord:
   def __init__(self, word, count):
      self.count = 1
   def __str__(self):
      return 'Word: %s Count: %s' % (self.word.ljust(40), self.count)
   def __repr__(self):
      return str(self)
   def __lt__(self, other):
      return self.count > other.count

#Preliminary stuff
test_message = " "
words = []
word_list = []
temp = MegaWord('', 0)
tempIndex = 0
myflag = 1
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
temp_iterator = 0


my_out_file = open('OutFile', 'r+')

for line in my_out_file:
   line_words = line.split()
   print(line_words)
   

   temp.word = line_words[1]
   temp.count = line_words[3]

   print(temp)

   word_list.append(temp)

print (word_list)

print("Getting yaks from Rutgers area")

# Decide on location to check with your location
location = pk.Location(40.478671, -74.431789)      
# Cal Poly: 35.3017,  120.6598
# Rutgers: 40.478671, -74.431789
testyakker = pk.Yakker(None, location, False)
yaklist = testyakker.get_yaks()

yakNum = 1
for yak in yaklist:
   # line between yaks
   print ("_" * 93)
   print (yakNum)
   test_comment = yak.print_yak()

   words = test_comment.split()

   for string in words:
      print("in here\n")
      temp = MegaWord('', 0)
      string = string.lower()
      temp.word = string
      temp.count = 1

      for myMegaWord in word_list:
         if (myMegaWord.word == temp.word):
            myMegaWord.count += 1
            myflag = 0

      if myflag == 1 and len(temp.word) >3: 
         word_list.append(temp)
      
      myflag = 1
      
   yakNum += 1

word_list.sort()


print("got here\n")
for MegaWord in word_list:
   print (MegaWord + " \n")
#my_out_file.write('Word: %s Count: %s\n' % (MegaWord.word.ljust(40), MegaWord.count))































   
