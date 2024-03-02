partition = str("guliza")
service = str("digitalocean")
region = str("nyc")
accountid = int("1234567")
resourceid = int("9876543")
arn = f"arn:{partition}:{service}:{region}:{accountid}:{resourceid}"
print(arn)

#String Prefix: You start the string with an 
#'f' or 'F' character before the opening quote. 
#This indicates to Python that the string will contain 
#expressions to be evaluated.
#Expression Inside Curly Braces: Within the string, 
#you can place Python expressions inside curly braces {}. 
#These expressions will be evaluated at runtime 
#and their results will be inserted into the string.

