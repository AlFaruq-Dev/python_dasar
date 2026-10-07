umur, ktp = 20, True
if umur >= 17:
    if ktp:
        print("Boleh membuat KTP")
    else:
        print("Buat KTP dulu")

umur = 16
s = "dewasa" if umur >= 17 else "anak-anak"
print(s)

hari = "sabtu"

match hari:
    case "sabtu" | "minggu":
        print("Hari libur")
    case "senin":
        print("Semangat!")
    case _:
        print("Hari kerja")