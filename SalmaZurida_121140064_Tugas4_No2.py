import random
class Robot:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
        self.jumlah_turn = 0

class Antares(Robot):
    def __init__(self):
        super().__init__("Antares", 50000, 5000)
        self.multiplier = 1.0

    def lakukan_aksi(self, lawan):
        if self.jumlah_turn % 3 == 0 and self.jumlah_turn != 0:
            self.multiplier = 1.5
            print(f"{self.name} mendapatkan multiplier sebanyak {self.multiplier}")
        else:
            self.multiplier = 1.0
        damage = int(self.damage * self.multiplier)
        print(f"{self.name} menyerang sebanyak {damage} DMG")
        lawan.terima_aksi(damage)
        self.jumlah_turn += 1
    
    def terima_aksi(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage
            print(f"{self.name} menerima serangan sebanyak {damage} DMG")

class Alphasetia(Robot):
    def __init__(self):
        super().__init__("Alphasetia", 40000, 6000)
        self.jumlah_turn_tambahan = 0

    def lakukan_aksi(self, lawan):
        if self.jumlah_turn % 2 == 0 and self.jumlah_turn != 0:
            self.health += 4000
            print(f"{self.name} mendapatkan kesehatan sebanyak 4000 HP")
        print(f"{self.name} menyerang sebanyak {self.damage} DMG")
        lawan.terima_aksi(self.damage)
        self.jumlah_turn += 1
    
    def terima_aksi(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage
            print(f"{self.name} menerima serangan sebanyak {damage} DMG")

class Lecalicus(Robot):
    def __init__(self):
        super().__init__("Lecalicus", 45000, 5500)
        self.multiplier = 1.0
        self.jumlah_turn_tambahan = 0

    def lakukan_aksi(self, lawan):
        if self.jumlah_turn % 4 == 0 and self.jumlah_turn != 0:
            self.health += 7000
            self.multiplier = 2.0
            print(f"{self.name} mendapatkan HP sebanyak 7000 HP dan multiplier sebanyak {self.multiplier}")
        else:
            self.multiplier = 1.0
        damage = int(self.damage * self.multiplier)
        print(f"{self.name} menyerang sebanyak {damage} DMG")
        lawan.terima_aksi(damage)
        self.jumlah_turn += 1

    def terima_aksi(self, damage):
        if self.health - damage <= 0:
            self.health = 0
        else:
            self.health -= damage
            print(f"{self.name} menerima serangan sebanyak {damage} DMG")


print("Selamat datang di pertandingan robot Yamako")
robotku = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : "))
robotmu = random.randint(1, 3)
print(f"Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus) : {robotmu}")

if robotku == 1:
    robot_1 = Antares()
elif robotku == 2:
    robot_1 = Alphasetia()
elif robotku == 3:
    robot_1 = Lecalicus()
else:
    print("pilih angka 1-3")

if robotmu == 1:
    robot_2 = Antares()
elif robotmu == 2:
    robot_2 = Alphasetia()
elif robotmu == 3:
    robot_2 = Lecalicus()
else:
    print("pilih angka 1-3")

turn = 0
print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting")
while robot_1.health > 0 and robot_2.health > 0:
    print()
    turn += 1
    print(f"turn saat ini = {turn}")
    print(f"robotmu {robot_1.name} - {robot_1.health} HP , robot lawan {robot_2.name} - {robot_2.health} HP")
    tangan_1 = int(input(f"Pilih tangan robotmu ({robot_1.name}): "))
    tangan_2 = random.randint(1, 3)
    print(f"Pilih tangan robot lawan ({robot_1.name}]): {tangan_2}")

    if (tangan_1 == 3 and tangan_2 == 2) or (tangan_1 == 1 and tangan_2 == 3) or (tangan_1 == 2 and tangan_2 == 1):
        robot_1.lakukan_aksi(robot_2)
    elif tangan_1 == tangan_2:
        print("Seri!")
    else:
        robot_2.lakukan_aksi(robot_1)

print("game selesai!")