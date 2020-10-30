file = open("/Users/rasmuser/Dropbox/ProjectEuler/59cipher.txt", "r")

nums = file.read().strip().split(',')
nums = [int(x) for x in nums]

for line in file:
    line = line.split(",")
    for k in range(0, len(line)):
        nums.append(int(line[k]))
  
message = ''
for n1 in range(97, 123):
    for n2 in range(97, 123):
        for n3 in range(97, 123):
            key = [n1, n2, n3]
            new = []
            for k in range(0, len(nums), 3):
                new.append(nums[k]^key[0])
                new.append(nums[k+1]^key[1])
                new.append(nums[k+2]^key[2])

            sone = ""
            for kk in range(0, len(new)):
                sone = sone + str(chr(new[kk]))
            if "perimeter" in sone:
                message = sone

message = list(message)
sum = 0
for k in message:
    sum = sum + ord(k)
    


