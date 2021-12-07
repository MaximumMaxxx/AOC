# This code reads, then imports the input into the uwupp file becuase you can't directly do it
def main():
    with open("sampleinput.txt","r") as input:
        inputraw = input.read()

    crabs = [int(crab) for crab in inputraw.split(",")]

    print(crabs)

    with open("main.uwupp","w") as UwU:
        UwU.write(f"awway_len iws {len(crabs)}\n") 

        for crab in enumerate(crabs):
            UwU.write(f"cwabs[{crab[0]}] iws {crab[1]}\n") 

if __name__ == "__main__":
    main()