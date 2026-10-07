siswa = {"nama": "Sari", "umur": 19}
siswa["kota"] = "Bandung"
siswa["umur"] = 20
print(siswa["nama"])
print(siswa.get("hobi", "-"))

for k, v in siswa.items():
    print(f"{k}: {v}")