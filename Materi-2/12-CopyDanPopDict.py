# Copy Dictionary

teman_teman = {
    "rz":"Rizki",
    "rk":"Reky",
    "my":"Hilmy",
    "ya":"Yahya",
    "nf":"Naufal"
}

friends = teman_teman.copy()

print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

teman_teman["nf"] = "Ucup"
print(f"teman-teman: {teman_teman}\n")
print(f"friends: {friends}\n")

# Pop Dictionary (berdasarkan key)

dataNaufal = friends.pop("nf")
print(f"Data Naufal = {dataNaufal}\n")
print(f"Friends = {friends}\n")

# Popitem Dictionary (paling terakhir)

dataTerakhir = friends.popitem()
print(f"Data Terakhir = {dataTerakhir}\n")
print(f"Friends = {friends}\n")