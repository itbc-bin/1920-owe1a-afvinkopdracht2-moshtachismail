z = input("Enter your mRNA: ")
b = input("Enter your DNA: ")
print("/////////////////////////////////////////////////////////////////////////")

# counts all the ATCG's of mRNA
Z = z.count("G")
c = z.count("C")
P = z.count("A")
O = z.count("T")
# counts all the ATCG's of DNA
B = b.count("G")
D = b.count("C")
K = b.count("A")
M = b.count("T")

# makes a sum to count up the GC's for mRNA
H = int(Z) + int(c)
# makes a sum to count up the GC's for DNA
G = int(B) + int(D)

# makes a sum to count up all the ATCG's for mRNA
Q = int(Z) + int(c) + int(P) + int(O)
# makes a sum to count up all the ATCG's for DNA
W = int(B) + int(D) + int(K) + int(M)

# prints all the info of the sums above
print("Amount of GC in mRna:")
print(H)
print("Amount of GC in DNA:")
print(G)
print("Full size mRna:")
print(Q)
print("Full size DNA:")
print(W)

# divides the amount of GC's mRNA by the full size and makes it an precantage
F = int(H) / int(Q) * int(100)
print("GC% mRna:")
print(F, "%")

# divides the amount of GC's DNA by the full size and makes it an precantage
f = int(G) / int(W) * int(100)
print("GC% DNA:")
print(f, "%")

# divides DNA size by mRNA size
L = int(W) / int(Q)
print("The amount of times mRNA fits in DNA:")
print(L)

# shows difference in length of DNA and mRNA
# by subtracting the mRNA size of the DNA size
l = int(W) - int(Q)
print("Difference in length between DNA en mRna:")
print(l)