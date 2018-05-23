#Read source file

try:
    f=open("Bereishis 1.txt", "r+", encoding="utf8")
    print(f.readline())
   
finally:
    f.close()
#It works!


   
