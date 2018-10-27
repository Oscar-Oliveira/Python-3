"""
Exercise 7
"""

delimiter = ";"

data = [] 
data.append(["Year","Make","Model","Description","Price"])
data.append(["1997","Ford","E350",'"ac, abs, moon"',"3000.00"])
data.append(["1999","Chevy",'"Venture ""Extended Edition"""','""',"4900.00"])
data.append(["1999","Chevy",'"Venture ""Extended Edition, Very Large"""',"","5000.00"])
data.append(["1996","Jeep","Grand Cherokee",'"MUST SELL! air, moon roof, loaded"',"4799.00"])

file = open("data.csv", "w")
for line in data:
    file.write(delimiter.join(line) + "\n")
file.close()
