note1 = float(input())

note = note1

hundred = int(note / 100)
note = note - (hundred * 100)

fifty = int(note / 50)
note = note - (fifty * 50)

twenty = int(note / 20)
note = note - (twenty * 20)

ten = int(note / 10)
note = note - (ten * 10)

five = int(note / 5)
note = note - (five * 5)

two = int(note / 2)
note = note - (two * 2)


print("NOTAS:")
print(f"{hundred} nota(s) de R$ 100.00")
print(f"{fifty} nota(s) de R$ 50.00")
print(f"{twenty} nota(s) de R$ 20.00")
print(f"{ten} nota(s) de R$ 10.00")
print(f"{five} nota(s) de R$ 5.00")
print(f"{two} nota(s) de R$ 2.00")

one = int(note / 1)
note = note - (one * 1)

fifty_ps = int(note / .50)
note = note - (fifty_ps * .50)

twenty_five_ps = int(note / .25)
note = note - (twenty_five_ps * .25)

ten_ps = int(note / .10)
note = note - (ten_ps * .10)

five_ps = int(note / .05)
note = note - (five_ps * .05)

one_ps = int(note / .01)

print("MOEDAS:")
print(f"{one} moeda(s) de R$ 1.00")
print(f"{fifty_ps} moeda(s) de R$ 0.50")
print(f"{twenty_five_ps} moeda(s) de R$ 0.25")
print(f"{ten_ps} moeda(s) de R$ 0.10")
print(f"{five_ps} moeda(s) de R$ 0.05")
print(f"{one_ps} moeda(s) de R$ 0.01")
