def calc_UT(t, UTP):
    return t*UTP

def calc_nt(t,CA,UT):
    return (t-CA-UT)

def calc_Ri(Do,nt):
    return Do/2-nt

def calc_d(Ri):
    return Ri*2

def calc_tmin_a(P,Do,S,E,W,Y):
    return round(P*Do/(2*(S*E*W+P*Y)),6)

def calc_tmin_b(P,d,CA,S,E,W,Y):
    return round(P*(d+2*CA)/(2*(S*E*W-P*(1-Y))),6)


# temp = 150 #design temp (Farenheit)
# material = "A312 TP316" #Specific Material
# Do = 1.315 #Outer diameter(inches)
# t = 0.179 #nominal wall thickness(inches)
# CA = 0 #corrosion allowance(inches)
# P = 90 #design pressure(psi)
# S = 20000 #allowable stress(psi)
# E = 0.80 #Longitudinal Efficiency
# UTP = 0.125 #undertolerance allowance
# W = 1.00    #weld joint reduction factor
# Y = 0.4 #Coefficient
# UT = calc_UT(t,UTP)
# nt = calc_nt(t,CA,UT)
# Ri = calc_Ri(Do,nt)
# d = calc_d(Ri)
# tmin_a = calc_tmin_a(P,Do,S,E,W,Y)
# tmin_b = calc_tmin_b(P,d,CA,S,E,W,Y)


# print(UT)
# print(nt)
# print(Ri)
# print(d)
# print(tmin_a)
# print(tmin_b)
