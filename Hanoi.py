def moveTower(height,fromPole,toPole,withPole):
    if height>=1:
        moveTower(height-1,fromPole,toPole,withPole)
        moveDisk(height,fromPole,withPole)
        moveTower(height-1,withPole,fromPole,toPole)

def moveDisk(disk,fromPole,toPole):
    print(f"moving disk[{disk}] from {fromPole} to {toPole}")

moveTower(3,"#1","#2","#3")