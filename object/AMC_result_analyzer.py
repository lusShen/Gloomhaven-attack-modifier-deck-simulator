class mydict(dict):
	def __missing__(self, key):
		return 0

def AMC_result_analyzer(filename,outputfile):
	
	ability_value_count = mydict()
	ability_count = mydict()
	damage_count = mydict()
	
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
	
	f = open(outputfile, "a")
	f.write("the analyze of %s\n\n" %(filename))
	f.write("Expected value of damage:\t%f\n\n" % (total_damage/ attack_count ) )
	attack_records.sort()
	f.write("10th percentile of damage:\t%d\n" % (attack_records[int(attack_count/10)]) )
	f.write("25th percentile of damage:\t%d\n" % (attack_records[int(attack_count/4)]) )
	f.write("50th percentile of damage:\t%d\n" % (attack_records[int(attack_count/2)]) )
	f.write("75th percentile of damage:\t%d\n\n" % (attack_records[int(attack_count*3/4)]) )
	
	for key in sorted(damage_count):
		f.write("Damage %d:\t%.3f%%\n" % (key,(damage_count[key] / attack_count *100)) )
		
	f.write("\n")
	
	for key in sorted(ability_count):
		if (not key):
			continue
		f.write("%s:\t%.3f%%\n" %(key,(ability_count[key] / attack_count *100)) )
		
	f.write("\n")
	
	for key in sorted(ability_value_count):
		f.write("Expected value of %s:\t%.3f\n" %(key,(ability_value_count[key] / attack_count)) )
	
	
	f.write("\n\n")
	
	f.close()



