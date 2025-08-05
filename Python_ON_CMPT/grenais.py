goalsx = 0
goalsy = 0
winx = 0
winy = 0
matches = 0
draws = 0
ans = 1

while ans == 1:
    x,y = map(int, input().split())

    if x > y:
        goalsx += x
        winx += 1
    elif x < y:
        goalsy += y
        winy += 1
    elif x == y:
        goalsx += x
        goalsy += y
        draws += 1
    
    matches += 1
        
    ans = 0
    while ans not in(1,2):
        print("Novo grenal (1-sim 2-nao)")
        ans = int(input())

        if ans == 2:
            break
            

print(f"{matches} grenais")
print(f"Inter:{winx}")
print(f"Gremio:{winy}")
print(f"Empates:{draws}")

if winx > winy:
    print("Inter venceu mais")

elif winx < winy:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")
