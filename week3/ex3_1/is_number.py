import string

def is_number(s):
	if s.startswith("0") and s.replace("0", "") != "": return False
	if s.isdigit(): return True # if int
	dot = s.find(".")
	if dot == 0: return False
	exp = s.find("e-")
	# exp goes before dot
	if (exp != -1) and (exp < dot): return False
	# no number after exp
	if (exp != -1 ) and len(s) <= exp+2: return False
	
	if s.startswith("-"):
		s = s.replace("-", "", 1)
	
	s = s.replace(".", "", 1)
	if (exp != -1): s = s.replace("e-", "", 1)
	return s.isdigit()

'''
print(is_number("10")) #true
print(is_number("-10")) #true
print(is_number("10.0")) #true
print(is_number("-10.0")) #true
print(is_number("10.150e-2")) #true
print(is_number("-10.150e-2")) #true
print(is_number("10.150e-")) #false
print(is_number("-10.150e-")) #false
print(is_number("11e-.10")) #false
print(is_number("blargh")) #false
print(is_number("--10")) #false
print(is_number("-10..01")) #false
print(is_number("0")) #true
print(is_number("00")) #true
print(is_number("001")) #false
'''