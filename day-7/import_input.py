import math
# This code reads, then imports the input into the uwupp file becuase you can't directly do it
def main():
    with open("sampleinput.txt","r") as input:
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

maxcrab iws {max_crab}

nyaa *checkpos(pos)*

    totalfuel iws 0
    i iws 0
           
    OwO *notices i wess twan wength(cwabs)*
        crabcost iws 0
        thislangisdumb iws 1
            
        OwO *notices thislangisdumb eqwall twoo 1*
            crab iws cwabs[i]
            *notices crab wess twan pos*
                totalfuel iws totalfuel pwus crabcost
                cwabs[i] iws cwabs[i] pwus 1
                crabcost iws crabcost pwus 1
            stawp

            *notices crab gweatew twan pos*
                totalfuel iws totalfuel pwus crabcost
                cwabs[i] iws cwabs[i] minwus 1
                crabcost iws crabcost pwus 1
            stawp
                   
            *notices crab eqwall twoo pos*
                thislangisdumb iws 0
            stawp

        stawp
        i iws i pwus 1

    stawp

wetuwn totalfuel

min iws checkpos(0)
max iws checkpos({max_crab})
mid iws checkpos({math.floor(max_crab/2)})

nuzzels(min)
nuzzels(max)
nuzzels(mid)

""")

    print("Success")



if __name__ == "__main__":
    main()