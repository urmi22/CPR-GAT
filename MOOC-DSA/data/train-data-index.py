import pdb




def concept_index(concepts):

	c_to_i = {concept[:-1]: i for i, concept in enumerate(concepts)}
	
	return c_to_i


def build_train_data_idx(c_i, balanced_data):

	td_i_with_label = []

	for sample in balanced_data:
		
		split_line = sample[:-1].split(",")
		c1 = split_line[0]
		c2 = split_line[1]
		l = int(split_line[2])
		
		td_i_with_label.append(tuple((c_i[c1], c_i[c2], l)))

	return td_i_with_label


def file_write(td_i):

	with open("./data/train-data-index.txt",'w') as f:
		for tup in td_i:
			f.write("%s %s %s\n"%(str(tup[0]), str(tup[1]), str(tup[2])))


def main():

	with open("./data/concepts.txt", 'r') as f \
		,open("./data/balanced-data.txt", 'r') as f1:
		concepts = f.readlines()
		balanced_data = f1.readlines()


	concept_to_idx = concept_index(concepts)
	train_data_idx_l = build_train_data_idx(concept_to_idx, balanced_data)
	
	file_write(train_data_idx_l)
	# pdb.set_trace()


if __name__ == '__main__':
	main()



