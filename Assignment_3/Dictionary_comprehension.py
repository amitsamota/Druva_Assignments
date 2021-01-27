
#program to zip key value of two dictionary into one


k={'k1':'k1_val','k2':'k2_val'}
j={'j1':'j1_val','j2':'j2_val'}

print(k.keys() + j.keys())
print(list(k.keys()) + list(j.keys()))          #['k1', 'k2', 'j1', 'j2']
print(list(k.values()) + list(j.values()))      #['k1_val', 'k2_val', 'j1_val', 'j2_val']

print (dict(zip(list(k.keys()) + list(j.keys()) , list(k.values()) + list(j.values()))))


