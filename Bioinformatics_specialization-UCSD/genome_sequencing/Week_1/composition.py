import sys

def composition(seq,num):
	reads = []
	for i in range(len(seq) - num + 1):
		reads.append(seq[i:i+num])
	return reads


def main():
	file_name = sys.argv[1]
	with open(file_name) as file:
		k = int(file.readline())
		sequence = file.readline()[:-1]

	ans = composition(sequence,k)
	with open('ans.txt','w') as out:
		for s in ans:
			out.write(s)
			out.write('/n')
	for s in ans:
		print s
