#Number_01:
    
n = [i for i in range(1,1001)
        if i%8==0]
print(n)

#Number_02:
n = [i for i
        in range(1,1001)
        if '6' in str(i)]
print(n)

#Number_03:   
string = "Practice Problems to Drill List Comprehension in your Head."

n = [i for i in string if i==" "]

print("The number of spaces: ")
print(len(n))

#Number_04:
string = "Practice Problems to Drill List Comprehension in your Head."

n = [i for i in string
       if i!='a' and
       i!='e' and
       i!='i' and
       i!='o' and
       i!='u' ]
print("After removing the vowels: ")
print(''.join(n))

#Number_05:
string = "Practice Problems to Drill List Comprehension in your Head."

n = [i for i in string
       if i!='a' and
       i!='e' and
       i!='i' and
       i!='o' and
       i!='u' ]
print("After removing the vowels: ")
print(''.join(n))

#Number_06:
string = "Practice Problems to Drill List Comprehension in your Head"
w1 = string.split()
X = {w2 : len(w2) for w2 in w1}
print("The length of each word in a sentence: ")
print(X)

#Number_07:
numbers=[i for i in range (1,1001) ]

ans=[n for n in numbers
        if [a for a in range(2,10)
            if n%a == 0]]
print(ans)

#Number_08:
numbers=[i for i in range (1,1001)]
ans = {n:max([d for d in range(1,10) if n % d == 0 ])for n in numbers}
print(ans)

