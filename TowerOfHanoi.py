def TowerofHanoi(n, source, destination, auxillary):
    if n==1:
        print("Move Disk 1 from source", source, "to destination", destination)
        return
    TowerofHanoi(n-1, auxillary, destination, source)
    print("Move Disk",n,"from source", source, "to destination", destination)
    TowerofHanoi(n-1, auxillary, destination, source)

#input no. of rings from user
n=int(input("Enter Number of rings you want:"))
TowerofHanoi(n,'A','B','C')
