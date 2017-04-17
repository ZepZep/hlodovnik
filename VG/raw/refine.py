def putSection(s):
    return "\\section{"+s+"}\n"

def putSubsection(s):
    return "  \\subsection{"+s+"}\n"

def makeTexHlod(s):
    return "    \\hlod{"+s+"}\n"

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
                    autor = l[1]
                    outFile.write(putSection(rok))
                    outFile.write(putSubsection(autor))
                elif l[1] != autor:
                    autor = l[1]
                    outFile.write(putSubsection(autor))
                
                hlod += l[2][0:-1] + "\\newline\n"
                nextNewHlod = False
                continue
            else:
                hlod += line[0:-1] + "\\newline\n"
         
