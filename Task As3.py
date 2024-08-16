M = 1.989*(10**30) #given
a = 1.5*(10**11) #given
G = 6.674*(10**(-11)) #given

T = ((4*(3.14**2)*(a**3)/(G*M))**0.5)/31536000 #apply formula in terms of Earth years

print(f"Orbital period: {T} Earth years")
