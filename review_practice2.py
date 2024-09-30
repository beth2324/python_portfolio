#evaught@uncc.edu
#review practice assignment

#if not calling file from current dictionary, enter path here to call this file
path=""

#Part 1: Create a function with file name as the parameter, make a nested dictionary representation of the file
def read_data_file(name):
	#read data from the provided file
	with open(name,"r") as file:
		#start outer dictionary
		county_dict={}
		for iteration,line in enumerate(file):
			#start inner dictionary fresh
			inner={}
			#get rid of extra info in line and make string a list
			line=line.strip("'").split(",")
			#make list of years for inner keys
			if iteration==0:
				year=line[1:]
			else:
				#make inner dictionary
				for i,amount in enumerate(line[1:]):
					inner[year[i]]=int(amount)
				#format outer dictionary: key=county,value={year:amount of coal}
				county=line[0]
				county_dict[county]=inner
	#return the nested dictionary
	return county_dict

#Part 2: Write a function with nested dictionary as parameter and return county years total dictionary
def calculate_total_production(nested_dict):
	#start dictionary
	tot_product={}
	#make list of county names
	counties=list(nested_dict.keys())
	#start variable for while loop
	x=0
	#use a while loop
	while x!=len(counties):
		#start sum total at 0
		total=0
		#get sum of production from inner dictionary at county x
		total=sum(nested_dict[counties[x]].values())
		#make new dictionary key=county and value=total
		tot_product[counties[x]]=total
		#count iterations for while loop
		x+=1
	#return the generated dictionary
	return tot_product

def main():
	#add statements that call to these functions
	name=path+"coal_production.csv"
	nested_dict=read_data_file(name)
	tot_product=calculate_total_production(nested_dict)

	#present results
	print(f"\nTotal production of each county across all years can be seen here:\n")
	for name, production in tot_product.items():
		print(f"{name} : {production} tons")
if __name__ == '__main__':
	main()