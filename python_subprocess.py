import subprocess #สำหรับrun therminal command

if __name__ == "__main__":
   #basic therminal command
   subprocess.run(["ls", "-ltr"])

   print("first run num=100 xx=90")
   subprocess.run(["python", "fristpy.py", "--num", "100","-xx","90"])
   print("----------------------------------------------------------") 
   print("secord run num=10 xx=90")
   subprocess.run(["python", "fristpy.py", "--num", "10","-xx","-90"])
   print("----------------------------------------------------------") 
   print("third run num=0 ")
   subprocess.run(["python", "fristpy.py", "--num", "0"])

#use output from other program
   process_output = subprocess.Popen(["python", "fristpy.py", "--num", "0"],
                                      stdout = subprocess.PIPE,
                                      stderr = subprocess.PIPE)
   
   out, err = process_output.communicate()
   print(out.decode('utf-8'))
   print(len(out.decode('utf-8')))




     
