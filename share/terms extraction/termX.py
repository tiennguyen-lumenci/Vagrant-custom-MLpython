import os
import argparse
import subprocess
import re
import pandas as pd

class termX(object):
    def __init__(self):
        self.result = []
        
    def __extract__(self,filename):
        with open(filename, 'r') as f:
            flag = 0
            flag2 = 0
            cc = 0
            tt = 0
            cclist = []
            ttlist = []
            ttlistX =[]
            ttlistY = []
            cct=""
            ttt=""
            termC = 0
            termC_ = 0
            count = 0
            for c,line in enumerate(f):
                #1 bug "IV." might appear in a sentense 
                if line.find("IV.")!=-1 and c > 100:
                    flag = 1
                    continue
                if flag == 1:
                    #get court construction
                    if (cc == 0) and re.search("Court.*Construction$",line) and (flag2 == 1):
                        cct+=line
                        cc = 1
                        flag2 = 0
                    elif cc >= 1:
                        if (cc >= 2) and re.search("^\s*[A-Z0-9]{1,3}\.\s*",line):
                            cc = 0
                            tt = 0
                            count = 0
                            ttlist.append(ttlistX)
                            ttlistX=[]
                            cclist.append(" ".join((cct.split())[3:]))
                            cct=""
                        elif (cc >= 2) and re.search("^\s*\n",line):
                            cc += 1
                            cct+=line
                        elif (cc == 1) and re.search("\w\.\W*\s*\n",line):
                            cc += 1
                            cct+=line
                        else:
                            cc = 1
                            cct+=line
                    #--- end court construction ---
                    #get table
                    if (tt == 0) and re.search("^\s*[A-Z]{1,2}\.",line):
                        if line.find("“") != -1:
                            flag2 = 1
                            tt = 1
                            termC_ = len([x for x in line.split() if (x.find("“") != -1)])
                            termC = 3*termC_
                    elif (tt == 1) and (count < termC):
                        if (count < termC_) and re.search("\w+",line):
                            if line.find("Claim") != -1:
                                if count == 0:
                                    ttt = ttt.split("“")
                                    c = 0
                                    s = ''
                                    temp = ttt[0].strip().split()
                                    while c < (len(temp)):
                                        if c%2 != 0:
                                            s += temp[c]
                                            ttlistX.append([s])
                                            s =''
                                        else:
                                            s += temp[c] + " "
                                        c += 1
                                    ttt = "“" + ttt[-1] + " "
                                count += 1
                                ttt += " ".join(line.split())
                                ttlistY.append(ttt)
                                ttt = ""
                            else:
                                ttt += " ".join(line.split()) + " "
                        elif (count >= termC_):
                            if re.search("\W", line) and (ttt == "") and (count==termC_):
                                ttt=""
                            if re.search("\w", line):
                                ttt += " ".join(line.split()) + " "
                            elif re.search("\W", line) and (ttt != ""):
                                count += 1
                                ttt = ttt.strip()
                                ttlistY.append(ttt)
                                ttt = ""
                        if (count > 0) and (len(ttlistY)==termC_) and (len(ttlistX)==3):
                            for x in ttlistY:
                                ttlistX[(count//termC_)-1].append(x)
                            ttlistY = [] 
                    #--- end get table ---
                    if line.find("V.")!=-1:
                        break
            #combine table
            for i in ttlist[1:]:
                for c,j in enumerate(i):
                    for c1,k in enumerate(j):
                            ttlist[0][c].append(k)
            self.result.append(ttlist[0])
            self.result.append(cclist)
                
    def pdf2text(self, filepath):
        out = filepath[0:-3] + "txt"
        subprocess.run(["pdf2txt.py", filepath, "-o",out])
        self.__extract__(out)
        
    def convert2csv(self,filepath):
        out = filepath[0:-3]
        df = pd.DataFrame(self.result[0]).T
        df.to_csv(out + "_1.csv",index=False, encoding='utf-8-sig')
        df1 = pd.DataFrame(self.result[1])
        df1.to_csv(out + "_2.csv",index=False, encoding='utf-8-sig')
        
def termX_wrapper(filepath):        
    r = termX()
    r.pdf2text(filepath)
    r.convert2csv(filepath)
    
def walkdir(path,d):
    newP = path+"/"+d
    #for p in os.listdir(newP):
    #    print(newP+"/"+p)
    for p in os.listdir(newP):
        if os.path.isfile(newP+"/"+p) and (p[-3:] == "pdf"):
            termX_wrapper(newP+"/"+p)
        elif os.path.isdir(newP+"/"+p):
            walkdir(newP,p)
    
def main():
    parser = argparse.ArgumentParser(description='Process userinput')
    parser.add_argument("-f", "--file", required=False, type=str, default="", help="name of the input file that is in the same folder as this script or any subfolder")
    parser.add_argument("-d", "--dir", required=False, type=str, default="", help="name of the sub directory that have all of the pdf files within the folder contains this script")
    
    args = vars(parser.parse_args())
    if (args["file"] != "") and (os.path.isfile(args["file"])):
        termX_wrapper(args["file"])
    elif (args["dir"] != "") and (os.path.isdir(args["dir"])):
        walkdir(os.getcwd(), args["dir"])
    else:
        print("Please try again!")    

if __name__ == "__main__":
    #termX_wrapper("test1.pdf")
    main()