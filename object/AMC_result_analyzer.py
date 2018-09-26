import os.path

class mydict(dict):
	def __missing__(self, key):
		return 0

def AMC_result_analyzer(filename,outputfile,name):
	
	ability_value_count = mydict()
	ability_count = mydict()
	damage_count = mydict()
	
	ability_list = [
		"fire",
		"ice",
		"air",
		"earth",
		"light",
		"dark",
		"poison",
		"wound",
		"immobilize",
		"disarm",
		"stun",
		"muddle",
		"invisible",
		"push",
		"pull",
		"piece",
		"shield",
		"heal",
		"add target",
		"curse"
	]
	
	stackable_ability_list = [
		"push",
		"pull",
		"piece",
		"shield",
		"heal",
		"add target",
		"curse"
	]
	
	attack_count = 0
	total_damage = 0
	
	attack_records = list()
	
	
	f = open(filename, "r")
	next(f) #skip headings
	for line in f:
		if line == "":
			break
		line = line.rstrip()
		attack_count += 1
		attack_attribute = line.split("\t")
		damage_count[int(attack_attribute[0])] += 1
		total_damage += int(attack_attribute[0])
		
		attack_records.append(int(attack_attribute[0]))
		
		del attack_attribute[0]
		
		for attack_ability in attack_attribute:
			if (not attack_ability):
				continue
			if (attack_ability.find(":") != -1):
				ability , ability_value = attack_ability.split(":")
				ability_count[ability] += 1
				ability_value_count[ability] += int(ability_value)
			else:
				ability_count[attack_ability] += 1
	
	f.close()
	
	
	if (not os.path.isfile(outputfile)):
		f = open(outputfile, "a")
		f.write("Class\tDMG Exp. value\t%% of 0 damage\t10th\t30th\t50th\t70th\t90th"  )
		for key in ability_list:
			f.write("\t%s" %(key) )
			if (key in stackable_ability_list):
				f.write("\tExp. value"  )
		f.write("\n")
	else:
		f = open(outputfile, "a")
	
	

			
	
	f.write("%s\t" %(name))
	attack_records.sort()
	f.write("%.3f\t%.3f%%\t%d\t%d\t%d\t%d\t%d" %(
			(total_damage/ attack_count),
			(damage_count[0]/ attack_count),
			attack_records[int(attack_count/10)],
			attack_records[int(attack_count*3/10)],
			attack_records[int(attack_count*5/10)],
			attack_records[int(attack_count*7/10)],
			attack_records[int(attack_count*9/10)],
		))
	
	for key in ability_list:
		f.write("\t")
		if (key in ability_count):
			f.write("%.3f%%" %(ability_count[key]/attack_count *100) )
		if (key in stackable_ability_list):
			f.write("\t")
			if (key in ability_count):
				f.write("%.3f" %(ability_value_count[key]/attack_count) )
			
	f.write("\n")
	f.close()



