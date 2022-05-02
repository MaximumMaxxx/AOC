import math
# This code reads, then imports the input into the uwupp file becuase you can't directly do it
def main():
    with open("input.txt","r") as input:
        inputraw = input.read()

    cwabs = [int(cwab) for cwab in inputraw.split(",")]


    with open("test.uwupp","w") as UwU:
        # This aprt generates the array of cwabs (cwabs)
        UwU.write(f"""
UwU This is the auto generated output of inport_input.py
UwU It's overall very similar to not-stupid-solution.py so I would whole heartedly suggest just using that

cwabs iws awway<{len(cwabs)};int>\n
""") 
        max_crab = 0
        for cwab in enumerate(cwabs):
            UwU.write(f"cwabs[{cwab[0]}] iws {cwab[1]}\n") 
            if cwab[1] > max_crab:
                max_crab = cwab[1]

        UwU.write(f"""
nuzzels(cwabs)

maxcrab iws 0
i iws 0
OwO *notices i wess twan wength(cwabs)*
    *notices cwabs[i] gweatew twan maxcrab*
        maxcrab iws cwabs[i]
    stawp
    i iws i pwus 1
stawp

nyaa *checkpos(pos)*

    totalfuel iws 0
    i iws 0
           
    OwO *notices i wess twan wength(cwabs)*
        crabcost iws 0
        thislangisdumb iws 1
            
        OwO *notices thislangisdumb eqwall twoo 1*
            crab iws cwabs[i]
            *notices crab wess twan pos*
                crabcost iws crabcost pwus 1
                cwabs[i] iws cwabs[i] pwus 1
                totalfuel iws totalfuel pwus crabcost
            stawp

            *notices crab gweatew twan pos*
                crabcost iws crabcost pwus 1
                cwabs[i] iws cwabs[i] minwus 1
                totalfuel iws totalfuel pwus crabcost
            stawp
                   
            *notices crab eqwall twoo pos*
                thislangisdumb iws 0
                
            stawp
        stawp
        nuzzels(i)
        i iws i pwus 1
    stawp
    return iws awway<2;int>
    return[0] iws totalfuel
    return[1] iws pos
wetuwn return

UwU this function is a hot mess but it works
nyaa *digfloat(num)*
    num2 iws num
    num4 iws num twimes 10
    num iws num4 diwide 2

    num2 iws num2 diwide 2
    num3 iws num2 twimes 20
    diff iws num4 minwus num3
    nuzzels(diff)
    return iws num2
    *notices diff gweatew twan 4*
        nuzzels("round up")
        return iws num2 pwus 1
    stawp
wetuwn return

min iws checkpos(0)
max iws checkpos(maxcrab)
mid iws checkpos(maxcrab diwide 2)

nuzzels(min)
nuzzels(max)
nuzzels(mid)

final iws awway<2;int>

thislangdumb iws 1
OwO *notices thislangdumb eqwall twoo 1*

    else iws 1
    *notices min[0] wess twan max[0]*
        else iws 0

        max iws mid
        temp iws max[1] pwus min[1]
        mid iws checkpos(temp diwide 2)
    stawp

    *notices else eqwall twoo 1*
        min iws mid
        temp iws max[1] pwus min[1]
        mid iws checkpos(temp diwide 2)
    stawp
    UwU Stop condition
    *notices max[1] eqwall twoo min[1]*
        thislangdumb iws 0
    stawp
    nuzzels(mid)
    dumpState()

stawp

nuzzels("The final answer is: ")
nuzzels(mid)


""")

    print("Success")



if __name__ == "__main__":
    main()