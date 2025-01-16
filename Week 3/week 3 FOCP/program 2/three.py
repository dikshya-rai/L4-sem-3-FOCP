num=int(input("How many students?"))
grp=int(input("Required group size? "))
group=num//grp
left=num%grp
if left!=1:
    print(f"There will {group} groups with {left} students left over")
else:
    print(f"There will be {group} groups with {left} students left over")
    