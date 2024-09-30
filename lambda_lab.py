#evaught@uncc.edu
#2/7/24
#lambda functions lab

def main():
	#make starter lists
	#q1 - strings and substring
	s_list1,substring=(['cats','dogs','sunsets','hot coco','mac and cheese','coconut pie'],'coco')
	#q2 and q3- format "aaa_x_bbb" - "a" & "b" = characters, "x" = number
	s_list2,s_list3=(['adf_18_dsh','sdf_3_jkl','uih_7_sdf','try_4_bnm','ewr_8_jkh'],['adf_1_dsh','sdf_3_jkl','uih_7_sdf','try_4_bnm','ewr_8_jkh'])


	#1) filter for strings with substring
	s_list1b=list(filter(lambda item: substring in item,s_list1))

	#2) sort by "x" number
	s_list2b=sorted(s_list2,key=(lambda x: int(x.split("_")[1])))
	
	#3) reformat items to "bbb_x"
	s_list3b=list(map(lambda section: section[6:]+section[3:5],s_list3))


	#display results
	print(f"\n1){s_list1}\n   -> {s_list1b}")
	print(f"\n2){s_list2}\n   -> {s_list2b}")
	print(f"\n3){s_list3}\n   -> {s_list3b}\n")
if __name__ == '__main__':
	main()