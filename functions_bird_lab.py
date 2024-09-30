#evaught@uncc.edu
#functions lab
#system for tracking observations of bird species


#1 take bird species,number of sightings
def simple_add(bird,count=1):
	bird_count[bird]+=count


#2 take multiple sets of species,number
def multi_add(*observations):
	prev_name=""
	for info in observations:
		if type(info) is str:
			bird_count[info]+=1
			prev_name=info
		else:
			bird_count[prev_name]+=(info-1)


#3 take multiple species and species=number
def add_kw_observations(*name,**kw_val):
	#why does it not take keyword argument as keyword argument
	for bird in name:
		bird_count[bird]+=1
	for bird,number in kw_val.items():
		bird_count[bird]+=number


#start dictionary with species:0
def make_dict(*names):
	global bird_count
	bird_count={}
	for name in names:
		#start count at 0
		bird_count[name]=0


#show results of updated dictionary
def admiration_station():
	print("\nObservation Dictionary")
	for name,number in bird_count.items():
		print(name+" : "+str(number))
	print("\n")


#call functions
def main():
	#start dictionary of bird types you will be counting
	make_dict("crow","penguin")

	#choose which function to use by setting associated 'run' to equal yes
	#simple add
	run=True
	if run==True:
		simple_add("crow",2)
	
	#multi add
	run1=True
	if run1==True:
		multi_add("crow","penguin",2)
	
	#keyword add
	run2=True
	if run2==True:
		add_kw_observations("penguin",crow=2)
	
	#print dictionary
	admiration_station()
if __name__ == '__main__':
	main()