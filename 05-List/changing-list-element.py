country=["Bangladesh", " India","Nepal", "Bhutan"," Thailand"]
country[1]="Bindia"
print(country)
country[1:4]="Sakib","Apu", " Rajib"
print(country)
country[1:2]="US","UK","Italy"
print(country)
#so if we want to add new element without replace other element use insert() function on the following way.
Name=["sakib","rajib","maruf"]
Name.insert(1,"apu") # always remember insert functio can only insert one element at a time.
print(Name)
Name[0:0]="rubai","ridoy"
print(Name)
# if you want to insert multiple element at a tiem use slicing .