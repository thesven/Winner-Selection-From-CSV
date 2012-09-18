import argparse, randomdotorg, csv

#define functions to be used

#get a random number from random.org
def getRandomNumber(low, high):
  print 'getting number from random.org between ', low, 'and', high
  r = randomdotorg.RandomDotOrg()
  return r.randrange(low, high)

#get all the rows for a CSV and return them as an array
def getCSVRows(dataFile):
  print 'getting rows from: ', dataFile
  with open(dataFile, 'rb') as csvfile:
   return list(csv.reader(csvfile, delimiter=','))
   
#end of functions used
  
#add the arguments to parse
parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='input_file', help='input file to use', required=True, type=str)
parser.add_argument('-o', action='store', dest='output_file', help='output file to write to', required=True, type=str)
parser.add_argument('-head', action='store', dest='has_header', help='does the input csv have a header row', default=True)

#get the results of the arguments
results = parser.parse_args()

#print argument info for user to see
print 'input file = ', results.input_file
print 'input has header row = ', results.has_header
print 'output file = ', results.output_file

#get the data from the input csv file
data = getCSVRows(results.input_file)

#select a random number
randomNumber = 0
if results.has_header == True:
  randomNumber = getRandomNumber(1, len(data) -1)
else:
  randomNumber = getRandomNumber(0, len(data) - 1)

#print the random number and winner
print 'random number = ', randomNumber
print 'winner = ', data[randomNumber]

#write the winner info to the output csv file
print 'writing winner csv file to: ', results.output_file
output = open(results.output_file, 'wb')
writer = csv.writer(output)

if results.has_header == True:
  writer.writerow(data[0])

writer.writerow(data[randomNumber])
print 'finished writing winner file!'