label,opcode,operand=input("Read first input line: ")
symtab={"Label":"0000"} #label:address
optab={"Mnemonic":"machineCode"} #menmonic:machineEquivalent
if opcode =='start':
    startAdds=addressOf(operand)
    locctr=startAdds
    midFile=label+opcode+operand
    lable,opcode,operand=input("Read next input line: ")
else:
    locctr=0
while opcode !='end':
    if label=='.':
        #Is a comment
        if label is not None:   #search if label exists in LABEL FIELD
            if label in symtab.keys(): #search if label exists in symtab
                print("Set Error flag: Duplicate symbol")
            else:
                #insertSymtab(label,locctr)
                symtab.update({label,locctr})
        if opcode in optab.keys():
            locctr+=3
        elif opcode=='WORD':
            locctr+=3
        elif opcode=='RESW':
            locctr+=(3*addressOf(operand))
        elif opcode=='RESB':
            locctr+=addressOf(operand)
        elif opcode=="BYTE":
            locctr+=len(opcode)
        else:
            print("Set Error Flag")

    midFile=label+opcode+operand          
    lable,opcode,operand=input("Read next input line: ")
print('last line')
midFile=label+opcode+operand 
progLen=locctr