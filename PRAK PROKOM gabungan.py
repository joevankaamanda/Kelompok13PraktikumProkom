hitung = ""
urutan = 0
def menu():
    print("[1] Balok")
    print("[2] Bola")
    print("[3] Kubus")
    print("[4] Limas Segiempat")
    print("[5] Tabung")
    print("[6] Prisma Segiempat")
    print("[7] Limas Segitiga")
    print("[8] Kerucut")
    pil = int(input("SILAKAN PILIH NOMOR BANGUN RUANG YANG AKAN DIHITUNG = "))
    if pil in range(1,9):
        if pil == 1:
            Balok()
        elif pil == 2:
            Bola()
        elif pil == 3:
            Kubus()
        elif pil == 4:
            LimasSegiEmpat()
        elif pil == 5:
            tabung()
        elif pil == 6:
            pristiga()
        elif pil == 7:
            LimasSegitiga()
        else:
            Kerucut()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        menu()
def Balok():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Panjang Balok")
    print("[4] Lebar Balok")
    print("[5] Tinggi Balok")
    pil = int(input("SILAKAN PILIH NOMOR YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nBALOK\n".format(urutan)
    if pil in range(1,6):
        if pil == 1:
            Vbalok()
        elif pil == 2:
            LPbalok()
        elif pil == 3:
            Pbalok()
        elif pil == 4:
            Lbalok()
        else:
            Tbalok()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Balok()
def Vbalok():
    print("Masukkan nilai panjang, lebar, dan tinggi balok")
    p = float(input("p = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if p>0 and l>0 and t>0:
        Volbalok = p*l*t
        print("Volume balok = ", Volbalok)
        global hitung 
        hitung = hitung + "Panjang balok = {}\nLebar balok = {}\nTinggi Balok = {}\nVolume balok = {}\n\n".format(p,l,t,Volbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vbalok()
def LPbalok():
    print("Masukkan nilai panjang, lebar, dan tinggi balok")
    p = float(input("p = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if p>0 and l>0 and t>0:
        LP_balok = (2*p*l)+(2*p*t)+(2*l*t)
        print("Luas Permukaan balok = ", LP_balok)
        global hitung 
        hitung = hitung + "Panjang balok = {}\nLebar balok = {}\nTinggi balok = {}\nLuas permukaan balok = {}\n\n".format(p,l,t,LP_balok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPbalok()
def Pbalok():
    print("[1] Volume, Lebar, Tinggi")
    print("[2] Luas permukaan, Lebar, Tinggi")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            P_Vbalok()
        else:
            P_LPbalok()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Pbalok()
def P_Vbalok():
    print("Masukkan nilai Volume, lebar, dan tinggi balok")
    V = float(input("V = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if V>0 and l>0 and t>0:
        PVbalok = V/(l*t)
        print("Panjang balok = ", PVbalok)
        global hitung 
        hitung = hitung + "Volume balok = {}\nLebar balok = {}\nTinggi balok = {}\nPanjang balok = {}\n\n".format(V,l,t,PVbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        P_Vbalok()
def P_LPbalok():
    print("Masukkan nilai Luas Permukaan, lebar, dan tinggi balok")
    LP = float(input("LP = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if LP>0 and l>0 and t>0:
        PLPbalok = (LP-(2*l*t))/(2*(l+t))
        print("Panjang balok = ", PLPbalok)
        global hitung 
        hitung = hitung + "Luas permukaan balok = {}\nLebar balok = {}\nTinggi balok = {}\nPanjang balok = {}\n\n".format(LP,l,t,PLPbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        P_LPbalok()
def Lbalok():
    print("[1] Volume, Panjang, Tinggi")
    print("[2] Luas permukaan, Panjang, Tinggi")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            L_Vbalok()
        else:
            L_LPbalok()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Lbalok()
def L_Vbalok():
    print("Masukkan nilai Volume, panjang, dan tinggi balok")
    V = float(input("V = "))
    p = float(input("p = "))
    t = float(input("t = "))
    if V>0 and p>0 and t>0:
        LVbalok = V/(p*t)
        print("Lebar balok = ", LVbalok)
        global hitung 
        hitung = hitung + "Volume balok = {}\nPanjang balok = {}\nTinggi balok = {}\nLebar balok = {}\n\n".format(V,p,t,LVbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        L_Vbalok()
def L_LPbalok():
    print("Masukkan nilai Luas Permukaan, panjang, dan tinggi balok")
    LP = float(input("LP = "))
    p = float(input("p = "))
    t = float(input("t = "))
    if LP>0 and p>0 and t>0:
        LLPbalok = (LP-(2*p*t))/(2*(p+t))
        print("Lebar balok = ", LLPbalok)
        global hitung 
        hitung = hitung + "Luas permukaan balok = {}\nPanjang balok = {}\nTinggi balok = {}\nLebar balok = {}\n\n".format(LP,p,t,LLPbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        L_LPbalok()
def Tbalok():
    print("[1] Volume, Panjang, Lebar")
    print("[2] Luas permukaan, Panjang, Lebar")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            T_Vbalok()
        else:
            T_LPbalok()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Tbalok()
def T_Vbalok():
    print("Masukkan nilai Volume, panjang, dan lebar balok")
    V = float(input("V = "))
    p = float(input("p = "))
    l = float(input("l = "))
    if V>0 and p>0 and l>0:
        TVbalok = V/(p*l)
        print("Tinggi balok = ", TVbalok)
        global hitung 
        hitung = hitung + "Volume balok = {}\nPanjang balok = {}\nLebar balok = {}\nTinggi balok = {}\n\n".format(V,p,l,TVbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_Vbalok()
def T_LPbalok():
    print("Masukkan nilai Luas Permukaan, panjang, dan lebar balok")
    LP = float(input("LP = "))
    p = float(input("p = "))
    l = float(input("l = "))
    if LP>0 and p>0 and l>0:
        TLPbalok = (LP-(2*p*l))/(2*(p+l))
        print("Tinggi balok = ", TLPbalok)
        global hitung 
        hitung = hitung + "Luas permukaan balok = {}\nPanjang balok = {}\nLebar balok = {}\nTinggi balok = {}\n\n".format(LP,p,l,TLPbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_LPbalok()
def Bola():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Jari-jari")
    pil = int(input("SILAKAN PILIH NOMOR YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nBOLA\n".format(urutan)
    if pil in range(1,4):
        if pil == 1:
            Vbola()
        elif pil == 2:
            LPbola()
        else:
            Rbola()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Bola()
def Vbola():
    print("Masukkan nilai jari-jari")
    r = float(input("r = "))
    if r>0:
        Volbola = (4*3.14*(r**3))/3
        print("Volume balok = ", Volbola)
        global hitung 
        hitung = hitung + "Jari-jari bola = {}\nVolume bola = {}\n\n".format(r,Volbola)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vbola()
def LPbola():
    print("Masukkan nilai jari-jari")
    r = float(input("r = "))
    if r>0:
        LP_bola = (4*3.14*(r**2))
        print("Volume bola = ", LP_bola)
        global hitung 
        hitung = hitung + "Jari-jari bola = {}\nLuas permukaan bola = {}\n\n".format(r,LP_bola)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPbola()
def Rbola():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            R_Vbola()
        else:
            R_LPbola()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Rbola()
def R_Vbola():
    print("Masukkan nilai Volume")
    V = float(input("V = "))
    if V>0:
        RVbola = ((3*V)/(4*3.14))**(1/3)
        print("Jari-jari bola = ", RVbola)
        global hitung 
        hitung = hitung + "Volume bola = {}\nJari-jari bola = {}\n\n".format(V,RVbola)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        R_Vbola()
def R_LPbola():
    print("Masukkan nilai Luas Permukaan")
    LP = float(input("LP = "))
    if LP>0:
        RLPbola = (LP/(4*3.14))**(1/2)
        print("Jari-jari bola = ", RLPbola)
        global hitung 
        hitung = hitung + "Luas permukaan bola = {}\nJari-jari bola = {}\n\n".format(LP,RLPbola)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        R_LPbola()
def Kubus():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Rusuk")
    pil = int(input("SILAKAN PILIH ELEMEN YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nKUBUS\n".format(urutan)
    if pil in range (1,4):
        if pil == 1:
            Vkubus()
        elif pil == 2:
            LPkubus()
        else:
            Skubus()
    else:
        print("Nomor yang anda masukkan salah, silahkan cek dan masukkan nilai kembali")
        Kubus()
def Vkubus():
    print("Masukkan nilai rusuk kubus")
    s = float(input("s = "))
    if s>0:
        V_kubus = s*s*s
        print("Volume kubus = ", V_kubus)
        global hitung 
        hitung = hitung + "Rusuk kubus = {}\nVolume kubus = {}\n\n".format(s,V_Kubus)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silahkan cek dan masukkan nilai kembali")
        Vkubus()
def LPkubus():
    print("Masukkan nilai rusuk kubus")
    s = float(input("s = "))
    if s>0:
        LP_kubus = 6*(s**2)
        print("Luas permukaan kubus = ", LP_kubus)
        global hitung 
        hitung = hitung + "Rusuk kubus = {}\nLuas permukaan = {}\n\n".format(s,LP_Kubus)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silahkan cek dan masukkan nilai kembali")
        LPkubus()
def Skubus():
    print("[1] Volume")
    print("[2] Luas permukaan")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = ")
    if pil in range(1,3):
        if pil == 1:
            Skubus1()
        else:
            Skubus2()
    else:
        print("Nomor yang anda masukkan salah, silahkan cek dan masukkan nomor kembali")
        Skubus()
def Skubus1():
    print("Masukkan nilai volume")
    V = float(input("V = "))
    if V>0:
        S_kubus = V**(1/3)
        print("Rusuk kubus = ", S_kubus)
        global hitung 
        hitung = hitung + "Volume =  {}\nRusuk = {}\n\n".format(V,S_kubus)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Skubus1()
def Skubus2():
    print("Masukkan nilai luas permukaan")
    LP = float(input("LP = "))
    if LP>0:
        S_kubus = (LP/6)**(1/2)
        print("Rusuk kubus = ", S_kubus)
        global hitung 
        hitung = hitung + "Luas Permukaan =  {}\nRusuk = {}\n\n".format(LP,S_kubus)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Skubus2()
def LimasSegiEmpat(): 
    print("[1] Limas Persegi")
    print("[2] Limas Persegi Panjang")
    pil = int(input("SILAKAN PILIH NOMOR LIMAS YANG AKAN DIHITUNG = "))
    if pil in range(1,3):
        if pil == 1:
            LimasPersegi()
        else: 
            LimasPersegiPanjang()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        LimasSegiEmpat()
def LimasPersegi():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Selimut")
    print("[4] Tinggi")
    pil = int(input("SILAKAN PILIH ELEMEN YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nLIMAS PERSEGI\n".format(urutan)
    if pil in range(1,5):
        if pil == 1:
            Vlimaspersegi()
        elif pil == 2:
            LPlimaspersegi()
        elif pil == 3:
            Slimaspersegi()
        else:
            Tlimaspersegi()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        LimasPersegi()
def Vlimaspersegi():
    print ("Masukkan nilai panjang rusuk dan tinggi")
    s = float(input("Panjang Rusuk = "))
    t = float(input("Tinggi = "))
    if s>0 and t>0:
        V_limaspersegi = (1/3)*(s**2)*t
        print("Volume Limas Persegi = ", V_limaspersegi)
        global hitung 
        hitung = hitung + "Panjang rusuk = {}\nTinggi limas persegi = {}\nVolume limas persegi = {}\n\n".format(s,t,V_limaspersegi)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vlimaspersegi()  
def LPlimaspersegi() :
    print("Masukkan nilai panjang rusuk, luas alas, dan tinggi segitiga")
    s = float(input("Panjang Rusuk = "))
    a = float(input("Luas Alas = "))
    t = float(input("Tinggi Segitiga = "))
    if s>0 and a>0 and t>0:
        LP_limaspersegi = (s**2) + (4*(1/2)*a*t)
        print("Luas permukaan limas persegi = ", LP_limaspersegi)
        global hitung 
        hitung = hitung + "Panjang rusuk = {}\nLuas alas = {}\nTinggi segitiga= {}\nLuas permukaan limas persegi = {}\n\n".format(s,a,t,LP_limaspersegi)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPlimaspersegi()  
def Slimaspersegi():
    print ("Masukkan nilai luas permukaan dan panjang rusuk")
    LP = float(input("Luas Permukaan = "))
    s = float(input("Panjang Rusuk = "))
    if LP>0 and s>0:
        S_limaspersegi = LP - (s*s)
        print("Selimut Limas Persegi = ", S_limaspersegi)
        global hitung 
        hitung = hitung + "Luas permukaan = {}\nPanjang rusuk = {}\nSelimut limas persegi = {}\n\n".format(LP,s,S_limaspersegi)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Slimaspersegi()  
def Tlimaspersegi():
    print("[1] Volume, Panjang Rusuk ")
    print("[2] Sisi Miring Segitiga, Diagonal Alas")
    pil = int(input("MASUKKAN NILAI YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            Tlimaspersegi1()
        else:
            Tlimaspersegi2()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Tlimaspersegi()
def Tlimaspersegi1():
    print("Masukkan nilai volume, panjang rusuk")
    V = float(input("Volume = "))
    s = float(input("Panjang Rusuk = "))
    if V>0 and s>0:
        T_limaspersegi = (3*V)/(s*s)
        print("Tinggi Limas Persegi = ", T_limaspersegi)
        global hitung 
        hitung = hitung + "Volume = {}\nPanjang rusuk =  {}\nTinggi limas persegi = {}\n\n".format(V,s,T_limaspersegi)
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tlimaspersegi1()    
def Tlimaspersegi2():
    print("Masukkan nilai sisi miring segitiga, diagonal alas")
    s = float(input("Sisi Miring Segitiga = "))
    d = float(input("Diagonal Alas = "))
    if s>0 and d>0:
        T_limaspersegi = (s**2-((1/2*d)**2))**(1/2)
        print("Tinggi Limas Persegi = ", T_limaspersegi)
        global hitung 
        hitung = hitung + "Sisi miring segitiga = {}\nDiagonal alas =  {}\nTinggi limas persegi = {}\n\n".format(s,d,T_limaspersegi)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tlimaspersegi2()
def LimasPersegiPanjang():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Selimut")
    print("[4] Tinggi")
    pil = int(input("SILAKAN PILIH ELEMEN YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nLIMAS PERSEGI PANJANG\n".format(urutan)
    if pil in range(1,5):
        if pil == 1:
            Vlimaspersegipanjang()
        elif pil == 2:
            LPlimaspersegipanjang()
        elif pil == 3:
            Slimaspersegipanjang()
        else:
            Tlimaspersegipanjang()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        LimasPersegiPanjang()
def Vlimaspersegipanjang():
    print ("Masukkan nilai panjang alas, lebar alas, dan tinggi limas")
    p = float(input("Panjang Alas = "))
    l = float(input("Lebar Alas = "))
    t = float(input("Tinggi Limas = "))
    if p>0 and l>0 and t>0:
        V_limaspersegipanjang = (1/3)*p*l*t
        print("Volume Limas Persegi Panjang = ", V_limaspersegipanjang )
        global hitung 
        hitung = hitung + "Panjang alas = {}\nLebar alas = {}\nTinggi limas persegi panjang= {}\n\n".format(p,l,t,V_limaspersegipanjang)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vlimaspersegipanjang()  
def LPlimaspersegipanjang():
    print("Masukkan nilai panjang alas, lebar alas, dan tinggi segitiga")
    p = float(input("Panjang Alas = "))
    l = float(input("Lebar Alas = "))
    t = float(input("Tinggi Segitiga = "))
    if p>0 and l>0 and t>0:
        LP_limaspersegipanjang = (p*l)+(p*t)+(l*t)
        print("Luas permukaan limas persegi = ", LP_limaspersegipanjang)
        global hitung 
        hitung = hitung + "Panjang alas = {}\nLebar alas = {}\nTinggi segitiga = {}\n\n".format(p,l,t,LP_limaspersegipanjang)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPlimaspersegipanjang()  
def Slimaspersegipanjang():
    print ("Masukkan nilai luas permukaan, panjang alas, dan lebar alas")
    LP = float(input("Luas Permukaan = "))
    p = float(input("Panjang Alas = "))
    l = float(input("Lebar Alas = "))
    if LP>0 and p>0 and l>0:
        S_limaspersegipanjang = LP - (p*l)
        print("Selimut Limas Persegi Panjang = ", S_limaspersegipanjang)
        global hitung 
        hitung = hitung + "Luas permukaan = {}\nPanjang alas = {}\nLebar alas = {}\nSelimut = {}\n\n".format(LP,p,l,S_limaspersegipanjang)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Slimaspersegipanjang()  
def Tlimaspersegipanjang():
    print("[1] Volume, Panjang Alas, Lebar Alas")
    print("[2] Sisi Miring Segitiga, Diagonal Alas")
    pil = int(input("MASUKKAN NILAI YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            Tlimaspersegipanjang1()
        else:
            Tlimaspersegipanjang2()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Tlimaspersegipanjang()
def Tlimaspersegipanjang1():
    print("Masukkan nilai volume, panjang alas, lebar alas")
    V = float(input("Volume = "))
    p = float(input("Panjang Alas = "))
    l = float(input("Lebar Alas = "))
    if V>0 and p>0 and l>0:
        T_limaspersegipanjang = (3*V)/(p*l)
        print("Tinggi Limas Persegi Panjang = ", T_limaspersegipanjang)
        global hitung 
        hitung = hitung + "Volume = {}\nPanjang alas = {}\nLebar alas = {}\nTinggi limas persegi panjang = {}\n\n".format(V,p,l,T_limaspersegipanjang)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tlimaspersegipanjang1()  
def Tlimaspersegipanjang2():
    print("Masukkan nilai sisi miring, diagonal alas")
    s = float(input("Sisi Miring Segitiga = "))
    d = float(input("Diagonal Alas = "))
    if s>0 and d>0:
        T_limaspersegipanjang = (s**2-((1/2*d)**2))**(1/2)
        print("Tinggi Limas Persegi Panjang = ", T_limaspersegipanjang)
        global hitung 
        hitung = hitung + "Sisi miring segitiga = {}\nDiagonal alas = {}\nTinggi limas persegi panjang = {}\n\n".format(s,d,T_limaspersegipanjang)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tlimaspersegipanjang2()
def tabung():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Jari-Jari")
    print("[4] Tinggi Tabung")
    pil = int(input("SILAKAN PILIH ELEMEN YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nTABUNG\n".format(urutan)
    if pil in range(1,5):
        if pil == 1:
            Vtabung()
        elif pil == 2:
            LPtabung()
        elif pil == 3:
            Rtabung()
        else:
            Ttabung()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        tabung()
def Vtabung() :
    print("Masukkan nilai jari-jari dan tinggi tabung")
    r = float(input("r = "))
    t = float(input("t = "))
    if r>0 and t>0:
        V_tabung = 3.14*(r**2)*t
        print("Volume tabung = ", V_tabung)
        global hitung 
        hitung = hitung + "Jari-jari tabung = {}\nTinggi tabung = {}\nVolume tabung = {}\n\n".format(r,t,V_tabung)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vtabung()
def LPtabung() :
    print("Masukkan nilai jari-jari dan tinggi tabung")
    r = float(input("r = "))
    t = float(input("t = "))
    if r>0 and t>0:
        LP_tabung = 2*3.14*r*(r+t)
        print("Luas permukaan tabung = ", LP_tabung)
        global hitung 
        hitung = hitung + "Jari-jari tabung = {}\nTinggi tabung = {}\nLuas permukaan tabung = {}\n\n".format(r,t,LP_tabung)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPtabung()
def Rtabung() :
    print("Masukkan nilai volume dan tinggi tabung")
    V = float(input("V = "))
    t = float(input("t = "))
    if V>0 and t>0:
        R_tabung = (V/(3.14*t))**(1/2)
        print("Jari-jari tabung = ", R_tabung)
        global hitung 
        hitung = hitung + "Volume tabung = {}\nTinggi tabung = {}\nJari-jari tabung = {}\n\n".format(V,t,R_tabung)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Rtabung()
def Ttabung() :
    print("[1] Volume dan Jari-Jari")
    print("[2] Luas Permukaan dan Jari-Jari")
    pil = int(input("MASUKKAN NILAI YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            Ttabung1()
        else:
            Ttabung2()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Ttabung()
def Ttabung1():
    print("Masukkan nilai volume dan jari-jari")
    V = float(input("V = "))
    r = float(input("r = "))
    if V>0 and r>0:
        T_tabung = V/(3.14*(r**2))
        print("Tinggi tabung = ", T_tabung)
        global hitung 
        hitung = hitung + "Volume tabung = {}\nJari-jari tabung = {}\nTinggi tabung = {}\n\n".format(V,r,T_tabung)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Ttabung1()
def Ttabung2():
    print("Masukkan nilai luas permukaan dan jari-jari")
    LP = float(input("LP = "))
    r = float(input("r = "))
    if LP>0 and r>0:
        T_tabung = (LP/(2*3.14*r))-r
        print("Tinggi tabung = ", T_tabung)
        global hitung 
        hitung = hitung + "Luas permukaan tabung = {}\nJari-jari tabung = {}\nTinggi tabung = {}\n\n".format(LP,r,T_tabung)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Ttabung2()
def pristiga():
    print("[1] Luas Alas")
    print("[2] Keliling Alas")
    print("[3] Volume")
    print("[4] Luas Permukaan")
    print("[5] Luas Selimut")
    print("[6] Tinggi Prisma")
    pil = int(input("SILAKAN PILIH ELEMEN YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nPRISMA SEGITIGA\n".format(urutan)
    if pil in range(1,7):
        if pil == 1:
            LApristiga()
        elif pil == 2:
            KApristiga()
        elif pil == 3:
            Vpristiga()
        elif pil == 4:
            LPpristiga()
        elif pil == 5:
            LSpristiga()
        else:
            Tpristiga()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        pristiga()
def LApristiga() :
    print("[1] Alas dan Tinggi Segitiga")
    print("[2] Seluruh Sisi Segitiga")
    pil = int(input("MASUKKAN NILAI YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            LApristiga1()
        else:
            LApristiga2()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        LApristiga()
def LApristiga1():
    print("Masukkan nilai alas dan tinggi segitiga")
    alas_segitiga = float(input("alas = "))
    tinggi_segitiga = float(input("tinggi = "))
    if alas_segitiga>0 and tinggi_segitiga>0:
        LA_pristiga = (alas_segitiga * tinggi_segitiga) / 2
        print("Luas alas prisma segitiga = ", LA_pristiga)
        global hitung 
        hitung = hitung + "Alas segitiga = {}\nTinggi segitiga = {}\nLuas alas prisma segitiga = {}\n\n".format(alas_segitiga,tinggi_segitiga,LA_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LApristiga1()
def LApristiga2():
    print("Masukkan nilai sisi-sisi segitiga")
    sisi1 = float(input("sisi 1 = "))
    sisi2 = float(input("sisi 2 = "))
    sisi3 = float(input("sisi 3 = "))
    if sisi1>0 and sisi2>0 and sisi3>0:
        s = (sisi1+sisi2+sisi3)/2
        LA_pristiga = (s*(s-sisi1)*(s-sisi2)*(s-sisi3))**(1/2)
        print("Luas alas prisma segitiga = ", LA_pristiga)
        global hitung 
        hitung = hitung + "Sisi 1 = {}\nSisi 2 = {}\nSisi 3 = {}\nLuas alas prisma segitiga = {}\n\n".format(sisi1,sisi2,sisi3,LA_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LApristiga2()
def KApristiga():
    print("Masukkan nilai sisi-sisi segitiga")
    sisi1 = float(input("sisi 1 = "))
    sisi2 = float(input("sisi 2 = "))
    sisi3 = float(input("sisi 3 = "))
    if sisi1>0 and sisi2>0 and sisi3>0:
        KA_pristiga = sisi1+sisi2+sisi3
        print("Keliling alas prisma segitiga = ", KA_pristiga)
        global hitung 
        hitung = hitung + "Sisi 1 = {}\nSisi 2 = {}\nSisi 3 = {}\nKeliling alas prisma segitiga = {}\n\n".format(sisi1,sisi2,sisi3,KA_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        KApristiga()
def Vpristiga() :
    print("Masukkan nilai luas alas dan tinggi prisma")
    LA = float(input("Luas Alas = "))
    t = float(input("Tinggi Prisma = "))
    if LA>0 and t>0:
        V_pristiga = LA*t
        print("Volume prisma segitiga = ", V_pristiga)
        global hitung 
        hitung = hitung + "Luas alas prisma segitiga = {}\nTinggi prisma segitiga = {}\nVolume prisma segitiga = {}\n\n".format(LA,t,V_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vpristiga()
def LPpristiga() :
    print("Masukkan nilai luas alas, keliling alas, dan tinggi prisma")
    LA = float(input("Luas Alas = "))
    KA = float(input("Keliling Alas = "))
    t = float(input("Tinggi Prisma = "))
    if LA>0 and KA>0 and t>0:
        LP_pristiga = (2*LA) + (KA*t)
        print("Luas permukaan prisma segitiga = ", LP_pristiga)
        global hitung 
        hitung = hitung + "Luas alas prisma segitiga = {}\nKeliling alas prisma segitiga = {}\nTinggi prisma segitiga = {}\nLuas permukaan prisma segitiga = {}\n\n".format(LA,KA,t,LP_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPpristiga()
def LSpristiga() :
    print("Masukkan nilai keliling alas dan tinggi prisma")
    KA = float(input("Keliling Alas = "))
    t = float(input("Tinggi Prisma = "))
    if KA>0 and t>0:
        LS_pristiga = KA*t
        print("Luas selimut prisma segitiga = ", LS_pristiga)
        global hitung 
        hitung = hitung + "Keliling alas prisma segitiga = {}\nTinggi prisma segitiga = {}\nLuas selimut prisma segitiga = {}\n\n".format(KA,t,LS_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LSpristiga()
def Tpristiga():
    print("[1] Luas Alas dan Volume")
    print("[2] Luas Alas, Keliling Alas, dan Luas Permukaan")
    print("[3] Luas Selimut dan Keliling ALas")
    pil = int(input("MASUKKAN NILAI YANG DIKETAHUI = "))
    if pil in range(1,4):
        if pil == 1:
            Tpristiga1()
        if pil == 2:
            Tpristiga2()
        else:
            Tpristiga3()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Tpristiga()
def Tpristiga1():
    print("Masukkan nilai luas alas dan volume")
    LA = float(input("Luas Alas = "))
    V = float(input("Volume = "))
    if LA>0 and V>0:
        T_pristiga = V / LA
        print("Tinggi prisma segitiga = ", T_pristiga)
        global hitung 
        hitung = hitung + "Luas alas prisma segitiga = {}\nVolume prisma segitiga = {}\nTinggi prisma segitiga = {}\n\n".format(LA,V,T_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tpristiga1()
def Tpristiga2():
    print("Masukkan nilai luas alas, keliling alas, dan luas permukaan")
    LA = float(input("Luas Alas = "))
    KA = float(input("Keliling Alas = "))
    LP = float(input("Luas Permukaan = "))
    if LA>0 and KA>0 and LP>0:
        T_pristiga = (LP - (2*LA))/KA
        print("Tinggi prisma segitiga = ", T_pristiga)
        global hitung 
        hitung = hitung + "Luas alas prisma segitiga = {}\nKeliling alas prisma segitiga = {}\nLuas permukaan prisma segitiga = {}\nTinggi prisma segitiga = {}\n\n".format(LA,KA,LP,T_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tpristiga2()
def Tpristiga3():
    print("Masukkan nilai luas selimut dan keliling alas")
    LS = float(input("Luas Selimut = "))
    KA = float(input("Keliling Alas = "))
    if LS>0 and KA>0:
        T_pristiga = LS / KA
        print("Tinggi prisma segitiga = ", T_pristiga)
        global hitung 
        hitung = hitung + "Luas selimut prisma segitiga = {}\nKeliling alas prisma segitiga = {}\nTinggi prisma segitiga = {}\n\n".format(LS,KA,T_pristiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Tpristiga3()
def LimasSegitiga():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Luas Selimut")
    print("[4] Tinggi Limas")
    pil = int(input("SILAKAN PILIH NOMOR YANG AKAN DIHITUNG = "))
    if pil in range(1,5):
        if pil == 1:
            VLimasSegitiga()
        elif pil == 2:
            LPLimasSegitiga()
        elif pil == 3:
            LSLimasSegitiga()
        else :
            TLimasSegitiga()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        LimasSegitiga()
def VLimasSegitiga():
    print("Masukkan nilai alas segitiga, tinggi segitiga, dan tinggi limas")
    a = float(input("alas = "))
    t = float(input("tinggi = "))
    T = float(input("tinggi limas = "))
    if a>0 and t>0 and T>0:
        VolLimasSegitiga = (1/3)*(1/2)*a*t*T
        print("Volume Limas Segitiga = ", VolLimasSegitiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        VLimasSegitiga()
def LPLimasSegitiga():
    print("Masukkan nilai alas segitiga, tinggi segitiga, luas tegak segitiga 1, luas tegak segitiga 2, luas tegak segitiga 3")
    a = float(input("a = "))
    t = float(input("t = "))
    luastegaksegitiga1 = float(input("luas tegak segitiga 1 = "))
    luastegaksegitiga2 = float(input("luas tegak segitiga 2 = "))
    luastegaksegitiga3 = float(input("luas tegak segitiga 3 = "))
    if a>0 and t>0 and luastegaksegitiga1>0 and luastegaksegitiga2>0 and luastegaksegitiga3>0:
        LP_LimasSegitiga = ((1/2)*a*t)+(luastegaksegitiga1+luastegaksegitiga2+luastegaksegitiga3)
        print("Luas Permukaan Limas Segitiga = ", LP_LimasSegitiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPLimasSegitiga()
def LSLimasSegitiga():
    print("Masukkan nilai alas segitiga, Luas Permukaan, dan tinggi segitiga")
    a = float(input("alas = "))
    LP = float(input("Luas Permukaan = "))
    t = float(input("tinggi = "))
    if a>0 and LP>0 and t>0:
        LS_LimasSegitiga = LP-((1/2)*a*t)
        print("Luas Selimut Limas Segitiga = ", LS_LimasSegitiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LSLimasSegitiga()
def TLimasSegitiga():
    print("Masukkan nilai alas segitiga, Volume, dan tinggi segitiga")
    a = float(input("alas = "))
    V = float(input("Volume = "))
    t = float(input("tinggi = "))
    if a>0 and V>0 and t>0:
        T_LimasSegitiga = 3*V*(1/2)*a*t
        print("Tinggi Limas Segitiga = ", T_LimasSegitiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        TLimasSegitiga()
def Kerucut():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Jari-jari")
    print("[4] Tinggi kerucut")
    pil = int(input("SILAKAN PILIH NOMOR YANG AKAN DIHITUNG = "))
    global urutan
    urutan += 1
    global hitung
    hitung += "---{}---\nKERUCUT\n".format(urutan)
    if pil in range(1,5):
        if pil == 1:
            VKerucut()
        elif pil == 2:
            LPKerucut()
        elif pil == 3:
            rKerucut()
        else :
            TKerucut()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        Kerucut()
def VKerucut():
    print("Masukkan nilai jari-jari, dan tinggi")
    r = float(input("jari-jari = "))
    t = float(input("tinggi = "))
    if r>0 and t>0:
        VolKerucut = (1/3)*3.14*t*(r**2)
        print("Volume Kerucut = ", VolKerucut)
        global hitung 
        hitung = hitung + "Jari-jari kerucut = {}\nTinggi kerucut = {}\nVolume kerucut = {}\n\n".format(r,t,VolKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        VKerucut()
def LPKerucut():
    print("Masukkan nilai jari-jari, dan garis pelukis")
    r = float(input("jari-jari = "))
    s = float(input("garis pelukis = "))
    if r>0 and s>0 :
        LP_Kerucut = (3.14*r*s)+(3.14*r**2)
        print("Luas Permukaan Kerucut = ", LP_Kerucut)
        global hitung 
        hitung = hitung + "Jari-jari kerucut = {}\nGaris pelukis kerucut = {}\nLuas permukaan kerucut = {}\n\n".format(r,s,LP_Kerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LPKerucut()
def rKerucut():
    print("[1] Volume, Tinggi Kerucut")
    print("[2] Garis Pelukis, Tinggi Kerucut")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            r_VKerucut()
        else:
            r_sKerucut()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        rKerucut()
def r_VKerucut():
    print("Masukkan nilai Volume, dan tinggi")
    V = float(input("Volume = "))
    t = float(input("ttinggi = "))
    if V>0 and t>0:
        rVKerucut = ((3*V)/(3.14*t))**(1/2)
        print("Jari-jari Kerucut = ", rVKerucut)
        global hitung 
        hitung = hitung + "Volume kerucut = {}\nTinggi kerucut = {}\nJari-jari kerucut = {}\n\n".format(V,t,rVKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        r_VKerucut()
def r_sKerucut():
    print("Masukkan nilai garis pelukis, dan tinggi")
    s = float(input("garis pelukis = "))
    t = float(input("tinggi = "))
    if s>0 and t>0:
        rsKerucut = ((s**2)-(t**3))**(1/2)
        print("Jari-jari Kerucut = ", rsKerucut)
        global hitung 
        hitung = hitung + "Garis pelukis kerucut = {}\nTinggi kerucut = {}\nJari-jari kerucut = {}\n\n".format(s,t,rsKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        r_sKerucut()
def TKerucut():
    print("[1] Volume, Jari-jari")
    print("[2] Garis Pelukis, Jari-jari")
    pil = int(input("SILAKAN PILIH NOMOR YANG DIKETAHUI = "))
    if pil in range(1,3):
        if pil == 1:
            T_VKerucut()
        else:
            T_sKerucut()
    else:
        print("Nomor yang anda masukkan salah, silakan cek dan masukkan nomor kembali")
        TKerucut()
def T_VKerucut():
    print("Masukkan nilai Volume, dan jari-jari")
    V = float(input("Volume = "))
    r = float(input("jari-jari = "))
    if V>0 and r>0:
        TVKerucut = (3*V)/(3.14*(r**2))
        print("Tinggi Kerucut = ", TVKerucut)
        global hitung 
        hitung = hitung + "Volume kerucut = {}\nJari-jari kerucut = {}\nTinggi kerucut = {}\n\n".format(V,r,TsKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_VKerucut()
def T_sKerucut():
    print("Masukkan nilai garis pelukis, dan jari-jari")
    s = float(input("garis pelukis = "))
    r = float(input("jari-jari = "))
    if s>0 and r>0:
        TsKerucut = ((s**2)-(r**2))**(1/2)
        print("Tinggi Kerucut = ", TsKerucut)
        global hitung 
        hitung = hitung + "Garis pelukis kerucut = {}\nJari-jari kerucut = {}\nTinggi kerucut = {}\n\n".format(s,r,TsKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_sKerucut()
def ngitunglagi():
    hitung = str(input("Apakah anda ingin menghitung lagi? Ketik Y untuk YA atau T untuk TIDAK = "))
    if hitung == "Y" or hitung == "T":
        if hitung == "Y":
            menu()
        else:
            history()
    else:
        print("Huruf yang anda masukkan salah, silakan isi kembali")
        ngitunglagi()
def history():
    htr = str(input("Ingin melihat history perhitungan anda? Ketik Y untuk YA atau T untuk TIDAK = "))
    if htr == "Y" or htr == "T":
        if htr == "Y":
            namafile = str(input("Tulis nama file untuk history perhitungan = "))
            file_history = open(namafile, "w")
            file_history.write(hitung)
            file_history.close()
        else:
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM KAMI:)")
    else:
        print("Huruf yang anda masukkan salah, silakan isi kembali")
        history()

print("HALO SELAMAT DATANG DI KALKULATOR BANGUN RUANG")
menu()
