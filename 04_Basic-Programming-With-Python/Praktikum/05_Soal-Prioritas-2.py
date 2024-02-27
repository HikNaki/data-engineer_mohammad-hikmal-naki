print("program untuk menentukan prioritas dari proyek")

budget = int(input("Budget : "))
waktu = int(input("Waktu Pengerjaan: "))
kesulitan = int(input("Tingkat Kesulitan : "))

def cek_budget(budget):
    if budget >= 0 and budget <= 50 :
        a = 4
        return a
    elif budget >= 51 and budget <= 80 :
        a = 3
        return a
    elif budget >= 81 and budget <= 100 :
        a = 3
        return a
    elif budget > 100 :
        a = 1
        return a
    
def cek_waktu(waktu):
    if waktu >= 0 and waktu <= 20 :
        a = 10
        return a
    elif waktu >= 21 and waktu <= 30 :
        a = 5
        return a
    elif waktu >= 31 and waktu <= 50 :
        a = 2
        return a
    elif waktu > 50 :
        a = 1
        return a
    
def cek_kesulitan(kesulitan):
    if kesulitan >= 0 and kesulitan <= 3 :
        a = 10
        return a
    elif kesulitan >= 4 and kesulitan <= 6 :
        a = 5
        return a
    elif kesulitan >= 8 and kesulitan <= 10 :
        a = 1
        return a
    elif kesulitan > 10 :
        a = 0
        return a

prioritas = cek_budget(budget) + cek_waktu(waktu) + cek_kesulitan(kesulitan)

def cek_prioritas(prioritas):
    if prioritas <= 2 :
        return "Impossible"
    elif prioritas >= 3 and prioritas <= 9 :
        return "Low"
    elif prioritas >= 10 and prioritas <= 16 :
        return "Medium"
    elif prioritas >= 17 and prioritas <= 24 :
        return "High"
    
output_prioritas = cek_prioritas(prioritas)

print(f"Tingkat Prioritas : {output_prioritas}")

