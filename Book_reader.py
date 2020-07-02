import re
import PyPDF2 
  
# creating a pdf file object 
pdfFileObj = open('Arihant-general_knowledge.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
  

name=[]
num=pdfReader.numPages
book=[]
c_name=''
for i in range(num):
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
  
    l=pageObj.extractText()
    get=re.findall(r'[ A-Za-z0-9]*\nSGAEŒ',l)
    if c_name!=get and len(get)!=0:
        c_name=get
        book.append('')
        book[-1]+=l
    else:
        book[-1]+=l
        
        
    name.append(get)
    
    
# closing the pdf file object 
pdfFileObj.close()



with open("Book.txt","w", encoding="utf-8") as f:
    for x in book:
        li=x.split('TYPEŒ')
        dic={}
        for j in li:
            if j[0:3] not in dic.keys():
                dic[j[0:3]]=[j]
            else:
                dic[j[0:3]].append(j)
        c=0

        for i in dic.keys():
            if c==0:
                f.write("CHAPTER - ")
                f.write(dic[i][0])
            else:
                f.write("TYPE - ")
                f.write(i)
                outcome=re.findall(r"[0-9]+[\n]*[\.\-]+[\nA-Z]",dic[i][0])
                ques_ind=[]
                for j in outcome:
                    ques_ind.append(dic[i][0].find(j))           

                ans_num=re.findall(r"[0-9]+[\n]*\.[\n]*",dic[i][1])
                print(ques_ind)
                ans_ind=[]
                for j in ans_num:
                    ans_ind.append(dic[i][1].find(j))
              
    
                z=min(len(ques_ind),len(ans_ind))
                
                for j in range(z-1):
                    
                    temp=dic[i][0][ques_ind[j]:ques_ind[j+1]]
                    temp=temp.replace('\n','')
                    temp=temp.replace('(','\n(')
                    
                    f.write(temp)
                    f.write('\n')
                    f.write("\nANSWER:\n")
                    temp2=dic[i][1][ans_ind[j]:ans_ind[j+1]]
                    temp2=temp2.replace('\n','')
                    f.write(temp2)
                    f.write('\n\n')

                temp=dic[i][0][ques_ind[-1]:]
                temp=temp.replace('\n','')
                temp=temp.replace('(','\n(')
                f.write(temp)
                f.write('\n')
                f.write("\nANSWER:\n")
                temp2=dic[i][1][ans_ind[-1]:]
                temp2=temp2.replace('\n','')
                f.write(temp2)
                f.write('\n\n')

            c+=1