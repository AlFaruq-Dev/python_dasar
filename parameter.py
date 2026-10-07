def sapa(nama, salam="Halo"):
    return f"{salam}, {nama}!"

print(sapa("Ani"))
print(sapa(salam="Hai", nama="Budi"))

def total(*angka):
    return sum(angka)

print(total(1, 2, 3, 4))