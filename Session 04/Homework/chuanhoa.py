n = input("Full name la gi vay: ")
save = n.split()
out = [ ]
for i in range(len(save)):
    out.append(str(save[i]).capitalize())
print("Tra lai ne: ", *out)