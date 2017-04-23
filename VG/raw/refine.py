import pprint
from lidi import lidi

def putSection(s):
    return "\\section{"+s+"}\n"

def putSubsection(s):
    return "  \\subsection{"+s+"}\n"


def zavorky(s):
    s = s.replace("(", "\\textit{(")
    s = s.replace(")", ")}")
    return s

def vypustka(s):
    return s.replace("...", "\\ldots{}")

def uvozovky(s):
    s = s.replace("„", "\"")
    s = s.replace("“", "\"")
    l = s.split("\"")
    fin = s
    if len(l)%2 == 0:
        print("spatne uvozovky:")
        print(s)
    else:
        fin = ""
        for i, part in enumerate(l[0:-1]):
            fin += part
            if i % 2:
                fin += "}"
            else:
                fin += "\\uv{"
        fin += l[-1]
    return fin

def kurzJmena(s):
    l = s.split(":")
    fin = s
    if len(l)>1 and len(l[0].split(" ")) < 4:
        fin = "\\textit{" + lidi[l[0]] + "}:" + ":".join(l[1:])
        jmena.update({l[0]})
    return fin

def makeTexHlod(s):
    s = zavorky(s)
    s = uvozovky(s)
    s = vypustka(s)
    return "    \\hlod{"+s+"}\n"

jmena = set()

with open('hlody.txt', 'r') as inFile:
    with open('hlody.tex', 'w') as outFile:

        autor = "NULL"
        rok = "NULL"
        hlod = ""
        nextNewHlod = True
        for line in inFile:
            if line == "\n":
                nextNewHlod = True
                outFile.write(makeTexHlod(hlod))
                hlod = ""
                continue
            if nextNewHlod:
                l = line.split("\t")
                if l[0] != rok:
                    rok = l[0]
                    autor = l[1].replace("-", "--")
                    outFile.write(putSection(rok))
                    outFile.write(putSubsection(autor))
                elif l[1].replace("-", "--") != autor:
                    autor = l[1].replace("-", "--")
                    outFile.write(putSubsection(autor))
                
                hlod += kurzJmena(l[2][0:-1])
                nextNewHlod = False
                continue
            else:
                hlod += "\\newline\n    " + kurzJmena(line[0:-1]) 
                
#for jmeno in jmena:
    #print("'" + jmeno + "' : '" + jmeno + "'")
    
#print(len(jmena))

