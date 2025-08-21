# 15. Accept the percentage from the user and display the grade according to the following 
# criteria. 
# ● 
# Below 25 – D 
# ● 
# 25 to 45 – C 
# ● 
# 45 to 65 – B 
# ● 
# 65 to 85 – A 
# ● 
# Above 85 – A+


a=int(input(" enter the percentage "))

if a<0 and a>25:
    print("below 25-d")
elif a<25 and a>45:
    print("25 to 45-c")
elif a<45 and a>65:
    print("45 to 65-b")
elif a<65 and a>85:
    print("65 to 85-a")
else:
    print("above 85-a+")