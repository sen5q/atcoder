import io,sys,os
os.system("Cls")
with open("_input.txt") as TxtOpen:
    INPUT=TxtOpen.read() 
sys.stdin=io.StringIO(INPUT)
# --------------------------------------------------------


ab, ac, bc = input().split()

if ab=="<" and ac=="<" and bc=="<":
    print("B")

if ab=="<" and ac=="<" and bc==">":
    print("C")

if ab==">" and ac=="<" and bc=="<":
    print("A")

if ab==">" and ac==">" and bc=="<":
    print("C")

if ab=="<" and ac==">" and bc==">":
    print("A")

if ab==">" and ac==">" and bc==">":
    print("B")