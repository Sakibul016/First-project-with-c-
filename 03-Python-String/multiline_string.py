x = """ hi,
This is Sakibul islam,
I am from Bangladesh,
And i will work for your company,
will you be my best friend ? """
print(x)
# if we want to know the length of a string , use  len()  funtion  inside print(len())
a = "Hi, SAkibul!"
print("The length is",len(a))
# we can use IN inside print to check wether any particular pharase is present in string or not , by following this rule.just write as i write here.
print("Rajib" in a)# if it presents it will ans True , otherwise it will ans False .
# we will use if statment .
if "Rajib " not in a:
    print(" you are not rajib , you are Sakibul")
    # use replace() function to change the character in string.like in the following.
    print(a.replace("S","B"))