import pdb
import time
import copy







def remove_tab_newline(dlf):
    tmp_list = []
    for each_str in dlf:
        string = each_str[:-1].split("\t\t")
        tmp_list.append(string)
    
    return tmp_list








def main():
    with open("./data/DSA_LabeledFile",'r') as f1 \
        ,open("./data/preq.txt",'w') as f2 \
        ,open("./data/nonpreq.txt",'w') as f3:
        dsa_label_file = f1.readlines()
        concept_pair_with_label = remove_tab_newline(dsa_label_file)
        tmp_cp_with_label = copy.deepcopy(concept_pair_with_label)
        
        for each_list in tmp_cp_with_label:
            if each_list[2] == '-':
                each_list[2] = '0'
                each_list = ",".join(each_list)
                f3.write("%s\n"%each_list)
            if each_list[2] == '-1':
                each_list[2] = '1'
                each_list = ",".join(each_list)
                f2.write("%s\n"%each_list)
            if each_list[2] == '1-':
                i,j = 0,1
                each_list[i],each_list[j] = each_list[j],each_list[i]
                each_list[2] = '1'
                each_list = ",".join(each_list)
                f2.write("%s\n"%each_list)
                # pdb.set_trace()








if __name__ == '__main__':
	start_time = time.time()
	main()
	end_time = time.time()
	total_time = end_time - start_time
	print("total time: {}".format(total_time))

#total time: 0.00945 sec