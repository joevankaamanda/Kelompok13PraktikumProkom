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
    print("Masukkan nilai p, l, dan t")
    p = float(input("p = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if p>0 and l>0 and t>0:
        Volbalok = p*l*t
        print("Volume balok = ", Volbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vbalok()
def LPbalok():
    print("Masukkan nilai p, l, dan t")
    p = float(input("p = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if p>0 and l>0 and t>0:
        LP_balok = (2*p*l)+(2*p*t)+(2*l*t)
        print("Luas Permukaan balok = ", LP_balok)
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
    print("Masukkan nilai V, l, dan t")
    V = float(input("V = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if V>0 and l>0 and t>0:
        PVbalok = V/(l*t)
        print("Panjang balok = ", PVbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        P_Vbalok()
def P_LPbalok():
    print("Masukkan nilai LP, l, dan t")
    LP = float(input("LP = "))
    l = float(input("l = "))
    t = float(input("t = "))
    if LP>0 and l>0 and t>0:
        PLPbalok = (LP-(2*l*t))/(2*(l+t))
        print("Panjang balok = ", PLPbalok)
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
    print("Masukkan nilai V, p, dan t")
    V = float(input("V = "))
    p = float(input("p = "))
    t = float(input("t = "))
    if V>0 and p>0 and t>0:
        LVbalok = V/(p*t)
        print("Lebar balok = ", LVbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        L_Vbalok()
def L_LPbalok():
    print("Masukkan nilai LP, p, dan t")
    LP = float(input("LP = "))
    p = float(input("p = "))
    t = float(input("t = "))
    if LP>0 and p>0 and t>0:
        LLPbalok = (LP-(2*p*t))/(2*(p+t))
        print("Lebar balok = ", LLPbalok)
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
    print("Masukkan nilai V, p, dan l")
    V = float(input("V = "))
    p = float(input("p = "))
    l = float(input("l = "))
    if V>0 and p>0 and l>0:
        TVbalok = V/(p*l)
        print("Tinggi balok = ", TVbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_Vbalok()
def T_LPbalok():
    print("Masukkan nilai LP, p, dan l")
    LP = float(input("LP = "))
    p = float(input("p = "))
    l = float(input("l = "))
    if LP>0 and p>0 and l>0:
        TLPbalok = (LP-(2*p*l))/(2*(p+l))
        print("Tinggi balok = ", TLPbalok)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_LPbalok()
def Bola():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Jari-jari")
    pil = int(input("SILAKAN PILIH NOMOR YANG AKAN DIHITUNG = "))
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
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        Vbola()
def LPbola():
    print("Masukkan nilai jari-jari")
    r = float(input("r = "))
    if r>0:
        LP_bola = (4*3.14*(r**2))
        print("Volume balok = ", LP_bola)
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
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        R_LPbola()
def tabung():
    print("[1] Volume")
    print("[2] Luas Permukaan")
    print("[3] Jari-Jari")
    print("[4] Tinggi Tabung")
    pil = int(input("SILAKAN PILIH ELEMEN YANG AKAN DIHITUNG = "))
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
        print("Luas Alas Prisma Segitiga = ", LA_pristiga)
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
        print("Luas Alas Prisma Segitiga = ", LA_pristiga)
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
        print("Keliling Alas Prisma Segitiga = ", KA_pristiga)
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
    print("Masukkan nilai a, t, dan T")
    a = float(input("a = "))
    t = float(input("t = "))
    T = float(input("T = "))
    if a>0 and t>0 and T>0:
        VolLimasSegitiga = (1/3)*(1/2)*a*t*T
        print("Volume Limas Segitiga = ", VolLimasSegitiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        VLimasSegitiga()
def LPLimasSegitiga():
    print("Masukkan nilai a, t, luas tegak segitiga 1, luas tegak segitiga 2, luas tegak segitiga 3")
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
    print("Masukkan nilai a, LP, dan t")
    a = float(input("a = "))
    LP = float(input("Luas Permukaan = "))
    t = float(input("t = "))
    if a>0 and LP>0 and t>0:
        LS_LimasSegitiga = LP-((1/2)*a*t)
        print("Luas Selimut Limas Segitiga = ", LS_LimasSegitiga)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        LSLimasSegitiga()
def TLimasSegitiga():
    print("Masukkan nilai a, V, dan t")
    a = float(input("a = "))
    V = float(input("Volume = "))
    t = float(input("t = "))
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
    print("Masukkan nilai r, dan t")
    r = float(input("r = "))
    t = float(input("t = "))
    if r>0 and t>0:
        VolKerucut = (1/3)*3.14*t*(r**2)
        print("Volume Kerucut = ", VolKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        VKerucut()
def LPKerucut():
    print("Masukkan nilai r, dan s")
    r = float(input("r = "))
    s = float(input("s = "))
    if r>0 and s>0 :
        LP_Kerucut = (3.14*r*s)+(3.14*r**2)
        print("Luas Permukaan Kerucut = ", LP_Kerucut)
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
    print("Masukkan nilai V, dan t")
    V = float(input("V = "))
    t = float(input("t = "))
    if V>0 and t>0:
        rVKerucut = ((3*V)/(3.14*t))**(1/2)
        print("Jari-jari Kerucut = ", rVKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        r_VKerucut()
def r_sKerucut():
    print("Masukkan nilai s, dan t")
    s = float(input("s = "))
    t = float(input("t = "))
    if s>0 and t>0:
        rsKerucut = ((s**2)-(t**3))**(1/2)
        print("Jari-jari Kerucut = ", rsKerucut)
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
    print("Masukkan nilai V, dan t")
    V = float(input("V = "))
    r = float(input("r = "))
    if V>0 and r>0:
        TVKerucut = (3*V)/(3.14*(r**2))
        print("Tinggi Kerucut = ", TVKerucut)
        ngitunglagi()
    else:
        print("Nilai yang anda masukkan salah, silakan cek dan masukkan nilai kembali")
        T_VKerucut()
def T_sKerucut():
    print("Masukkan nilai s, dan r")
    s = float(input("s = "))
    r = float(input("r = "))
    if s>0 and r>0:
        TsKerucut = ((s**2)-(r**2))**(1/2)
        print("Tinggi Kerucut = ", TsKerucut)
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
            print("TERIMA KASIH :)")
    else:
        print("Huruf yang anda masukkan salah, silakan isi kembali")
        ngitunglagi()

print("HALO SELAMAT DATANG")
menu()
