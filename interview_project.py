# interview project for Emsi

class poem:
	def __init__(self,lines):
		self.lines = lines
		self.vocabulary = {} # vocabulary[word] = [word_index,count]
		self.line_vectors = [] # vector for each line (bag-of-words model)
		self.dimension = 0 # dimension of vector space
		
		# build vocabulary, treating each word as a single token
		word_index = 0
		for line in lines:
			for word in line.split():
				word = self.normalize(word)
				if word in self.vocabulary:
					self.vocabulary[word][1] += 1
				else:
					self.vocabulary[word] = [word_index,1]
					word_index +=1
		self.dimension = word_index

		# populate line_vectors
		for line in lines:
			vector = self.string_to_vector(line)
			self.line_vectors.append(vector)	
		
	def best_match(self, input_string):
		# returns the line that's the most likely match to the input_string
		
		# get corresponding vector for input string
		input_vector = self.string_to_vector(input_string)

		# for each line vector compute the number of words that also appear
		# in the input vector. This will be our similarity score
		non_zero_indices = [i for i in range(len(input_vector)) if input_vector[i] != 0]
		scores = []
		for target in self.line_vectors:
			similarity_score = 0
			for i in non_zero_indices:
				if target[i] != 0:
					similarity_score += 1
			scores.append(similarity_score)
	
		# find largest similarity score, return corresponding line
		max_index = scores.index(max(scores))
		return self.lines[max_index]							

	def normalize(self, string):
		# function that normalizes a string by making it lower-case, removing punctuation
		string = string.lower()
		punctuation = """'!()-;?.,"""
		for c in punctuation:
			string = string.replace(c,"")
		return string
	
	def string_to_vector(self,string):
		# function that returns the vector associated to a string
		vector = [0 for _ in range(self.dimension)]
		for word in string.split():
			word = self.normalize(word)
			if word in self.vocabulary:
				index = self.vocabulary[word][0]
				vector[index] += 1
		return vector


def main():
	# read in poem from file
	lines = [] # list containing each non-empty line from poem
	file = open("lepanto.txt","r")
	for line in file:
		if line != "\n":
			if line[-1] == "\n": line = line[:-1]
			lines.append(line)
	
	# instantiate a poem object
	lepanto = poem(lines)

	# take input string from user
	input_string = input("Enter the words you remember: ")
	
	# compute best match
	output_string = lepanto.best_match(input_string)
	print(output_string)
	
if __name__ == "__main__":
	main()
