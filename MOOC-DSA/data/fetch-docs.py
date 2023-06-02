import pdb
import time
import json
import os
import glob








def main():
	all_paths = glob.glob(os.path.join("./data","*.json"))
	docs = []
	for path in all_paths:
		with open(path, 'r') as f:
			princeton_file = f.readlines()
			for each_line in princeton_file:
				json_obj = json.loads(each_line)
				text = json_obj['text']
				docs.append(text)

	for idx, doc in enumerate(docs):
		doc_file = str((idx+1))+".txt"
		doc_path = './data/docs/'+doc_file
		with open(doc_path, 'w') as f1:
			f1.write("%s"%doc)



if __name__ == '__main__':
	start_time = time.time()
	main()
	end_time = time.time()
	total_time = end_time - start_time
	print("total time: {}".format(total_time))