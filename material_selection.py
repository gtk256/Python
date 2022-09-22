print("""Please enter a postive numerical value for the importance factor
with higher valued numbers having more importance for the following:
If you are indifferent to the property, enter zero""")
#checks to ensure user input is a positive number
while True:
    try:
        yield_strength_rating = float(input("Yield Strength: "))
        if yield_strength_rating < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a numerical value")
        continue

    try:
        ultimate_strength_rating = float(input("Ultimate Strength: "))
        if ultimate_strength_rating < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a numerical value")
        continue

    try:
        elongation_rating = float(input("Elongation: "))
        if elongation_rating < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a numerical value")
        continue

    try:
        elastic_modulus_rating = float(input("Elastic Modulus: "))
        if elastic_modulus_rating < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a numerical value")
        continue

    try:
        density_rating = float(input("Density: "))
        if density_rating < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a numerical value")
        continue

    try:
        poissons_ratio_rating = float(input("Poisson's Ratio: "))
        if poissons_ratio_rating < 0:
            print("Please enter a positive value")
            continue
    except ValueError:
        print("Please enter a numerical value")
        continue
    else:
        print("Thank you \n")
        break



rating_total = yield_strength_rating + ultimate_strength_rating
rating_total += elongation_rating + elastic_modulus_rating
rating_total += density_rating + poissons_ratio_rating
#the multipliers will be even if all traits are given zero values
if rating_total==0:
    yield_strength_multiplier = 100 / 6
    ultimate_strength_multiplier = 100 / 6
    elongation_multiplier = 100 / 6
    elastic_modulus_multiplier = 100 / 6
    density_multiplier = 100 / 6
    poissons_ratio_multiplier = 100 / 6
else:
    yield_strength_multiplier = (100 / rating_total) * yield_strength_rating
    ultimate_strength_multiplier = (100 / rating_total) * ultimate_strength_rating
    elongation_multiplier = (100 / rating_total) * elongation_rating
    elastic_modulus_multiplier = (100 / rating_total) * elastic_modulus_rating
    density_multiplier = (100 / rating_total) * density_rating
    poissons_ratio_multiplier = (100 / rating_total) * poissons_ratio_rating
#one hundred is divided by the prior values to keep things relative to each other
#and then multiplied by the user input to reflect their preferences 
non_ferrous_yield_strength_multiplier = yield_strength_multiplier
ferrous_yield_strength_multiplier = yield_strength_multiplier
non_ferrous_ultimate_strength_multiplier = ultimate_strength_multiplier
ferrous_ultimate_strength_multiplier = ultimate_strength_multiplier
non_ferrous_elongation_multiplier = elongation_multiplier
ferrous_elongation_multiplier = elongation_multiplier
non_ferrous_elastic_modulus_multiplier = elastic_modulus_multiplier
ferrous_elastic_modulus_multiplier = elastic_modulus_multiplier
non_ferrous_density_multiplier = density_multiplier
ferrous_density_multiplier = density_multiplier
non_ferrous_poissons_ratio_multiplier = poissons_ratio_multiplier
ferrous_poissons_ratio_multiplier = poissons_ratio_multiplier


#a check to ensure correct input and see which material class the
#user prefers 
x = 0
while x == 0:
    preference = input("Would you prefer Ferrous Allyos? y/n: ")
    if preference == 'y':
        print("Great choice \n")
        x = 1
    elif preference == 'n':
        print("Great choice \n")
        x = 2
    else:
        print("""Incorrect option, please input 'y' for
Ferrous Alloys and 'n' for non Ferrous Alloys""")



class Ferrous_Alloys:
    def __init__(self, yield_strength, ultimate_strength, elongation,
                 elastic_modulus, density, poissons_ratio, condition):
        self.yield_strength = yield_strength
        self.ultimate_strength = ultimate_strength
        self.elongation = elongation
        self.elastic_modulus = elastic_modulus
        self.density = density
        self.poissons_ratio = poissons_ratio
        self.condition = condition 
#the first class with seven assignable traits and eight materials with
#their own values for these traits
Carbon_Steel_1 = Ferrous_Alloys(yield_strength=32, ultimate_strength=50,
               elongation=25, elastic_modulus=29e6, density=0.283,
                poissons_ratio=0.32, condition="AISI 1020 Hot Rolled")

Carbon_Steel_2 = Ferrous_Alloys(yield_strength=80, ultimate_strength=90,
               elongation=5, elastic_modulus=29e6, density=0.283,
                poissons_ratio=0.32, condition="AISI 1045 Cold Worked")

Alloy_Steel_1 = Ferrous_Alloys(yield_strength=70, ultimate_strength=90,
               elongation=20, elastic_modulus=29e6, density=0.283,
                poissons_ratio=0.32, condition="AISI 4130 Hot Rolled")

Alloy_Steel_2 = Ferrous_Alloys(yield_strength=46, ultimate_strength=67,
               elongation=18, elastic_modulus=30e6, density=0.282,
                poissons_ratio=0.3, condition="ASTM A242")

Stainless_Steel_1 = Ferrous_Alloys(yield_strength=40, ultimate_strength=75,
               elongation=40, elastic_modulus=28e6, density=0.289,
                poissons_ratio=0.27, condition="AISI 201 Austentic, Annealed")

Stainless_Steel_2 = Ferrous_Alloys(yield_strength=150, ultimate_strength=177,
               elongation=6, elastic_modulus=29e6, density=0.282,
                poissons_ratio=0.27, condition="17-7PH, TH1050") 
    
Cast_Iron_1 = Ferrous_Alloys(yield_strength=40, ultimate_strength=60,
               elongation=18, elastic_modulus=24.5e6, density=0.256,
                poissons_ratio=0.29, condition="ASTM A536, Grade 60-40-18")

Cast_Iron_2 = Ferrous_Alloys(yield_strength=90, ultimate_strength=120,
               elongation=2, elastic_modulus=23.8e6, density=0.256,
                poissons_ratio=0.28, condition="ASTM A536, Grade 120-90-02")


#dictionaries are made with the values for each trait, containing all material values
Ferrous_Alloys_Yield_Strength = {32:'CS1', 80:'CS2', 70:'AS1', 46:'AS2', 40.001:'SS1',
                                 150:'SS2', 40.002:'CI1', 90:'CI2'}
Sorted_Ferrous_Alloys_Yield_Strength={}
#these values are sorted for the materials with the highest number, showing which are
#best at that specific trait
for i in sorted(Ferrous_Alloys_Yield_Strength):
   Sorted_Ferrous_Alloys_Yield_Strength[i]=Ferrous_Alloys_Yield_Strength[i]
Ferrous_Alloys_Yield_Strength_Temp = sum(Ferrous_Alloys_Yield_Strength)
#further dictionaires are made which can interact with the trait dictionary in an
#equation to score the individual materials on all of their traits compared
#to the other materials 
FAYST = Ferrous_Alloys_Yield_Strength_Temp
Ferrous_Alloys_Yield_Strength_Total = {'CS1':FAYST, 'CS2':FAYST, 'AS1':FAYST, 'AS2':FAYST,
                                'SS1':FAYST, 'SS2':FAYST, 'CI1':FAYST, 'CI2':FAYST}
FYSM = ferrous_yield_strength_multiplier 
ferrous_yield_strength_multipliers = {'CS1':FYSM, 'CS2':FYSM, 'AS1':FYSM, 'AS2':FYSM,
                                'SS1':FYSM, 'SS2':FYSM, 'CI1':FYSM, 'CI2':FYSM}



Ferrous_Alloys_Ultimate_Strength = {50:'CS1', 90.001:'CS2', 90.002:'AS1', 67:'AS2', 75:'SS1',
                                    177:'SS2', 60:'CI1', 120:'CI2'}
Sorted_Ferrous_Alloys_Ultimate_Strength={}
for i in sorted(Ferrous_Alloys_Ultimate_Strength):
   Sorted_Ferrous_Alloys_Ultimate_Strength[i]=Ferrous_Alloys_Ultimate_Strength[i]
Ferrous_Alloys_Ultimate_Strength_Temp = sum(Ferrous_Alloys_Ultimate_Strength)
FAUST = Ferrous_Alloys_Ultimate_Strength_Temp
Ferrous_Alloys_Ultimate_Strength_Total = {'CS1':FAUST, 'CS2':FAUST, 'AS1':FAUST, 'AS2':FAUST,
                                'SS1':FAUST, 'SS2':FAUST, 'CI1':FAUST, 'CI2':FAUST}
FUSM = ferrous_ultimate_strength_multiplier 
ferrous_ultimate_strength_multipliers = {'CS1':FUSM, 'CS2':FUSM, 'AS1':FUSM, 'AS2':FUSM,
                                'SS1':FUSM, 'SS2':FUSM, 'CI1':FUSM, 'CI2':FUSM}



Ferrous_Alloys_Elongation = {25:'CS1', 5:'CS2', 20:'AS1', 18.001:'AS2', 40:'SS1',
                             6:'SS2', 18.002:'CI1', 2:'CI2'}
Sorted_Ferrous_Alloys_Elongation={}
for i in sorted(Ferrous_Alloys_Elongation):
   Sorted_Ferrous_Alloys_Elongation[i]=Ferrous_Alloys_Elongation[i]
Ferrous_Alloys_Elongation_Temp = sum(Ferrous_Alloys_Elongation)
FAET = Ferrous_Alloys_Elongation_Temp
Ferrous_Alloys_Elongation_Total = {'CS1':FAET, 'CS2':FAET, 'AS1':FAET, 'AS2':FAET,
                                'SS1':FAET, 'SS2':FAET, 'CI1':FAET, 'CI2':FAET}
FEM = ferrous_elongation_multiplier 
ferrous_elongation_multipliers = {'CS1':FEM, 'CS2':FEM, 'AS1':FEM, 'AS2':FEM,
                                'SS1':FEM, 'SS2':FEM, 'CI1':FEM, 'CI2':FEM}



Ferrous_Alloys_Elastic_Modulus = {29.001e6:'CS1', 29.002e6:'CS2', 29.003e6:'AS1', 30e6:'AS2',
                                  28e6:'SS1', 29.004e6:'SS2', 24.5e6:'CI1', 23.8e6:'CI2'}
Sorted_Ferrous_Alloys_Elastic_Modulus={}
for i in sorted(Ferrous_Alloys_Elastic_Modulus):
   Sorted_Ferrous_Alloys_Elastic_Modulus[i]=Ferrous_Alloys_Elastic_Modulus[i]
Ferrous_Alloys_Elastic_Modulus_Temp = sum(Ferrous_Alloys_Elastic_Modulus)
FAEMT = Ferrous_Alloys_Elastic_Modulus_Temp
Ferrous_Alloys_Elastic_Modulus_Total = {'CS1':FAEMT, 'CS2':FAEMT, 'AS1':FAEMT, 'AS2':FAEMT,
                                'SS1':FAEMT, 'SS2':FAEMT, 'CI1':FAEMT, 'CI2':FAEMT}
FEMM = ferrous_elastic_modulus_multiplier 
ferrous_elastic_modulus_multipliers = {'CS1':FEMM, 'CS2':FEMM, 'AS1':FEMM, 'AS2':FEMM,
                                'SS1':FEMM, 'SS2':FEMM, 'CI1':FEMM, 'CI2':FEMM}



Ferrous_Alloys_Density = {0.283001:'CS1', 0.283002:'CS2', 0.283003:'AS1', 0.282001:'AS2',
                          0.289:'SS1', 0.282002:'SS2', 0.256001:'CI1', 0.256002:'CI2'}
Sorted_Ferrous_Alloys_Density={}
for i in sorted(Ferrous_Alloys_Density):
   Sorted_Ferrous_Alloys_Density[i]=Ferrous_Alloys_Density[i]
Ferrous_Alloys_Density_Temp = sum(Ferrous_Alloys_Density)
FADT = Ferrous_Alloys_Density_Temp
Ferrous_Alloys_Density_Total = {'CS1':FADT, 'CS2':FADT, 'AS1':FADT, 'AS2':FADT,
                                'SS1':FADT, 'SS2':FADT, 'CI1':FADT, 'CI2':FADT}
FDM = ferrous_density_multiplier 
ferrous_density_multipliers = {'CS1':FDM, 'CS2':FDM, 'AS1':FDM, 'AS2':FDM,
                                'SS1':FDM, 'SS2':FDM, 'CI1':FDM, 'CI2':FDM}



Ferrous_Alloys_Poissons_Ratio = dict()
Ferrous_Alloys_Poissons_Ratio = {0.32001:'CS1', 0.32002:'CS2', 0.32003:'AS1', 0.3:'AS2',
                                 0.27001:'SS1', 0.27002:'SS2', 0.29:'CI1', 0.28:'CI2'}
Sorted_Ferrous_Alloys_Poissons_Ratio={}
for i in sorted(Ferrous_Alloys_Poissons_Ratio):
   Sorted_Ferrous_Alloys_Poissons_Ratio[i]=Ferrous_Alloys_Poissons_Ratio[i]
Ferrous_Alloys_Poissons_Ratio_Temp = sum(Ferrous_Alloys_Poissons_Ratio)
FAPR = Ferrous_Alloys_Poissons_Ratio_Temp
Ferrous_Alloys_Poissons_Ratio_Total = {'CS1':FAPR, 'CS2':FAPR, 'AS1':FAPR, 'AS2':FAPR,
                                'SS1':FAPR, 'SS2':FAPR, 'CI1':FAPR, 'CI2':FAPR}
FPRM = ferrous_poissons_ratio_multiplier 
ferrous_poissons_ratio_multipliers = {'CS1':FPRM, 'CS2':FPRM, 'AS1':FPRM, 'AS2':FPRM,
                                'SS1':FPRM, 'SS2':FPRM, 'CI1':FPRM, 'CI2':FPRM}


#repeating the same process for the other material class, again with the same traits 
class Non_Ferrous_Alloys:
    def __init__(self, yield_strength, ultimate_strength, elongation,
                 elastic_modulus, density, poissons_ratio, condition):
        self.yield_strength = yield_strength
        self.ultimate_strength = ultimate_strength
        self.elongation = elongation
        self.elastic_modulus = elastic_modulus
        self.density = density
        self.poissons_ratio = poissons_ratio
        self.condition = condition 
    
Aluminium_Alloys_1 = Non_Ferrous_Alloys(yield_strength=59, ultimate_strength=67,
               elongation=7, elastic_modulus=10.5e6, density=0.101,
                poissons_ratio=0.33, condition="AI 2014, T6, T651")

Aluminium_Alloys_2 = Non_Ferrous_Alloys(yield_strength=16, ultimate_strength=26,
               elongation=16, elastic_modulus=9.9e6, density=0.098,
                poissons_ratio=0.33, condition="AI 6061, T4")

Nickel_Alloys_1 = Non_Ferrous_Alloys(yield_strength=55, ultimate_strength=110,
               elongation=30, elastic_modulus=29.8e6, density=0.305,
                poissons_ratio=0.28, condition="Inconel 625, Grade 1")

Nickel_Alloys_2 = Non_Ferrous_Alloys(yield_strength=40, ultimate_strength=75,
               elongation=45, elastic_modulus=29.6e6, density=0.3,
                poissons_ratio=0.31, condition="Inconel 625, Grade 1")

Copper_Alloys_1 = Non_Ferrous_Alloys(yield_strength=18, ultimate_strength=45,
               elongation=30, elastic_modulus=21.8e6, density=0.323,
                poissons_ratio=0.3, condition="70/30 Copper-Nickel, Annealed")

Copper_Alloys_2 = Non_Ferrous_Alloys(yield_strength=140, ultimate_strength=165,
               elongation=3, elastic_modulus=18.85e6, density=0.298,
                poissons_ratio=0.27, condition="70/30 Copper-Nickel, Annealed")

Titanium_Alloys_1 = Non_Ferrous_Alloys(yield_strength=40, ultimate_strength=50,
               elongation=20, elastic_modulus=14.8e6, density=0.163,
                poissons_ratio=0.34, condition="Commercially Pure")

Titanium_Alloys_2 = Non_Ferrous_Alloys(yield_strength=85, ultimate_strength=100,
               elongation=10, elastic_modulus=16e6, density=0.16,
                poissons_ratio=0.31, condition="Commercially Pure")   



Non_Ferrous_Alloys_Yield_Stength = {59:'AA1', 16:'AA2', 55:'NA1', 40.001:'NA2',
                                18:'CA1', 140:'CA2', 40.002:'TA1', 85:'TA2'}
Sorted_Non_Ferrous_Alloys_Yield_Strength={}
for i in sorted(Non_Ferrous_Alloys_Yield_Stength):
   Sorted_Non_Ferrous_Alloys_Yield_Strength[i]=Non_Ferrous_Alloys_Yield_Stength[i]
Non_Ferrous_Alloys_Yield_Strength_Temp = sum(Non_Ferrous_Alloys_Yield_Stength)
NFAYST = Non_Ferrous_Alloys_Yield_Strength_Temp
Non_Ferrous_Alloys_Yield_Strength_Total = {'AA1':NFAYST, 'AA2':NFAYST, 'NA1':NFAYST, 'NA2':NFAYST,
                                'CA1':NFAYST, 'CA2':NFAYST, 'TA1':NFAYST, 'TA2':NFAYST}
NFYSM = non_ferrous_yield_strength_multiplier 
non_ferrous_yield_strength_multipliers = {'AA1':NFYSM, 'AA2':NFYSM, 'NA1':NFYSM, 'NA2':NFYSM,
                                'CA1':NFYSM, 'CA2':NFYSM, 'TA1':NFYSM, 'TA2':NFYSM}



Non_Ferrous_Alloys_Ultimate_Strength = {67:'AA1', 26:'AA2', 110:'NA1', 75:'NA2',
                                45:'CA1', 165:'CA2', 50:'TA1', 100:'TA2'}
Sorted_Non_Ferrous_Alloys_Ultimate_Strength={}
for i in sorted(Non_Ferrous_Alloys_Ultimate_Strength):
   Sorted_Non_Ferrous_Alloys_Ultimate_Strength[i]=Non_Ferrous_Alloys_Ultimate_Strength[i]
Non_Ferrous_Alloys_Ultimate_Strength_Temp = sum(Non_Ferrous_Alloys_Ultimate_Strength)
NFAUST = Non_Ferrous_Alloys_Ultimate_Strength_Temp
Non_Ferrous_Alloys_Ultimate_Strength_Total = {'AA1':NFAUST, 'AA2':NFAUST, 'NA1':NFAUST, 'NA2':NFAUST,
                                'CA1':NFAUST, 'CA2':NFAUST, 'TA1':NFAUST, 'TA2':NFAUST}
NFUSM = non_ferrous_ultimate_strength_multiplier 
non_ferrous_ultimate_strength_multipliers = {'AA1':NFUSM, 'AA2':NFUSM, 'NA1':NFUSM, 'NA2':NFUSM,
                                'CA1':NFUSM, 'CA2':NFUSM, 'TA1':NFUSM, 'TA2':NFUSM}



Non_Ferrous_Alloys_Elongation = {7:'AA1', 16:'AA2', 30.001:'NA1', 45:'NA2',
                                30.001:'CA1', 3:'CA2', 20:'TA1', 10:'TA2'}
Sorted_Non_Ferrous_Alloys_Elongation={}
for i in sorted(Non_Ferrous_Alloys_Elongation):
   Sorted_Non_Ferrous_Alloys_Elongation[i]=Non_Ferrous_Alloys_Elongation[i]
Non_Ferrous_Alloys_Elongation_Temp = sum(Non_Ferrous_Alloys_Elongation)
NFAET = Non_Ferrous_Alloys_Elongation_Temp
Non_Ferrous_Alloys_Elongation_Total = {'AA1':NFAET, 'AA2':NFAET, 'NA1':NFAET, 'NA2':NFAET,
                                'CA1':NFAET, 'CA2':NFAET, 'TA1':NFAET, 'TA2':NFAET}
NFEM = non_ferrous_elongation_multiplier 
non_ferrous_elongation_multipliers = {'AA1':NFEM, 'AA2':NFEM, 'NA1':NFEM, 'NA2':NFEM,
                                'CA1':NFEM, 'CA2':NFEM, 'TA1':NFEM, 'TA2':NFEM}



Non_Ferrous_Alloys_Elastic_Modulus = {10.5e6:'AA1', 9.9e6:'AA2', 29.8e6:'NA1', 29.6e6:'NA2',
                                21.8e6:'CA1', 18.85e6:'CA2', 14.8e6:'TA1', 16e6:'TA2'}
Sorted_Non_Ferrous_Alloys_Elastic_Modulus={}
for i in sorted(Non_Ferrous_Alloys_Elastic_Modulus):
   Sorted_Non_Ferrous_Alloys_Elastic_Modulus[i]=Non_Ferrous_Alloys_Elastic_Modulus[i]
Non_Ferrous_Alloys_Elastic_Modulus_Temp = sum(Non_Ferrous_Alloys_Elastic_Modulus)
NFAEMT = Non_Ferrous_Alloys_Elastic_Modulus_Temp
Non_Ferrous_Alloys_Elastic_Modulus_Total = {'AA1':NFAEMT, 'AA2':NFAEMT, 'NA1':NFAEMT, 'NA2':NFAEMT,
                                'CA1':NFAEMT, 'CA2':NFAEMT, 'TA1':NFAEMT, 'TA2':NFAEMT}
NFEMM = non_ferrous_elastic_modulus_multiplier 
non_ferrous_elastic_modulus_multipliers = {'AA1':NFEMM, 'AA2':NFEMM, 'NA1':NFEMM, 'NA2':NFEMM,
                                'CA1':NFEMM, 'CA2':NFEMM, 'TA1':NFEMM, 'TA2':NFEMM}



Non_Ferrous_Alloys_Density = {0.101:'AA1', 0.098:'AA2', 0.305:'NA1', 0.3:'NA2',
                                0.323:'CA1', 0.298:'CA2', 0.163:'TA1', 0.16:'TA2'}
Sorted_Non_Ferrous_Alloys_Density={}
for i in sorted(Non_Ferrous_Alloys_Density):
   Sorted_Non_Ferrous_Alloys_Density[i]=Non_Ferrous_Alloys_Density[i]
Non_Ferrous_Alloys_Density_Temp = sum(Non_Ferrous_Alloys_Density)
NFADT = Non_Ferrous_Alloys_Density_Temp
Non_Ferrous_Alloys_Density_Total = {'AA1':NFADT, 'AA2':NFADT, 'NA1':NFADT, 'NA2':NFADT,
                                'CA1':NFADT, 'CA2':NFADT, 'TA1':NFADT, 'TA2':NFADT}
NFDM = non_ferrous_density_multiplier 
non_ferrous_density_multipliers = {'AA1':NFDM, 'AA2':NFDM, 'NA1':NFDM, 'NA2':NFDM,
                                'CA1':NFDM, 'CA2':NFDM, 'TA1':NFDM, 'TA2':NFDM}



Non_Ferrous_Alloys_Poissons_Ratio = {0.33001:'AA1', 0.33002:'AA2', 0.28:'NA1', 0.31001:'NA2',
                                0.3:'CA1', 0.27:'CA2', 0.34:'TA1', 0.31002:'TA2'}
Sorted_Non_Ferrous_Alloys_Poissons_Ratio={}
for i in sorted(Non_Ferrous_Alloys_Poissons_Ratio):
   Sorted_Non_Ferrous_Alloys_Poissons_Ratio[i]=Non_Ferrous_Alloys_Poissons_Ratio[i]
Non_Ferrous_Alloys_Poissons_Ratio_Temp = sum(Non_Ferrous_Alloys_Poissons_Ratio)
NFAPR = Non_Ferrous_Alloys_Poissons_Ratio_Temp
Non_Ferrous_Alloys_Poissons_Ratio_Total = {'AA1':NFAPR, 'AA2':NFAPR, 'NA1':NFAPR, 'NA2':NFAPR,
                                'CA1':NFAPR, 'CA2':NFAPR, 'TA1':NFAPR, 'TA2':NFAPR}
NFPRM = non_ferrous_poissons_ratio_multiplier 
non_ferrous_poissons_ratio_multipliers = {'AA1':NFPRM, 'AA2':NFPRM, 'NA1':NFPRM, 'NA2':NFPRM,
                                'CA1':NFPRM, 'CA2':NFPRM, 'TA1':NFPRM, 'TA2':NFPRM}


#trait dictionaries are rearranged so that the itmes are the same, but the key and value are swapped
Rearranged_Ferrous_Alloys_Yield_Strength = {y: x for x, y in Sorted_Ferrous_Alloys_Yield_Strength.items()}
Rearranged_Ferrous_Alloys_Ultimate_Strength = {y: x for x, y in Sorted_Ferrous_Alloys_Ultimate_Strength.items()}
Rearranged_Ferrous_Alloys_Elongation = {y: x for x, y in Sorted_Ferrous_Alloys_Elongation.items()}
Rearranged_Ferrous_Alloys_Elastic_Modulus = {y: x for x, y in Sorted_Ferrous_Alloys_Elastic_Modulus.items()}
Rearranged_Ferrous_Alloys_Density = {y: x for x, y in Sorted_Ferrous_Alloys_Density.items()}
Rearranged_Ferrous_Alloys_Poissons_Ratio = {y: x for x, y in Sorted_Ferrous_Alloys_Poissons_Ratio.items()}
if x==1:
    #trait dictionaries can now be used arithmetically with the previous dictionaires
    #the scoring works by taking the percentage of the overall trait which the given material holds and multiplying it by the users trait
    #preferences which were given at the beginning. This makes the values relative to each other and gives more weight to the traits specified 
    Scoring_Ferrous_Alloys_Yield_Strength = {key:  Rearranged_Ferrous_Alloys_Yield_Strength[key] / Ferrous_Alloys_Yield_Strength_Total.get(key, 0)
                    for key in  Rearranged_Ferrous_Alloys_Yield_Strength.keys()}
    Scored_Ferrous_Alloys_Yield_Strength = {key:  Scoring_Ferrous_Alloys_Yield_Strength[key] * ferrous_yield_strength_multipliers.get(key, 0)
                    for key in  Scoring_Ferrous_Alloys_Yield_Strength.keys()}
    Final_Ferrous_Score = Scored_Ferrous_Alloys_Yield_Strength
    
    Scoring_Ferrous_Alloys_Ultimate_Strength = {key:  Rearranged_Ferrous_Alloys_Ultimate_Strength[key] / Ferrous_Alloys_Ultimate_Strength_Total.get(key, 0)
                    for key in  Rearranged_Ferrous_Alloys_Ultimate_Strength.keys()}
    Scored_Ferrous_Alloys_Ultimate_Strength = {key:  Scoring_Ferrous_Alloys_Ultimate_Strength[key] * ferrous_ultimate_strength_multipliers.get(key, 0)
                    for key in  Scoring_Ferrous_Alloys_Ultimate_Strength.keys()}
    Final_Ferrous_Score = {key:  Scored_Ferrous_Alloys_Ultimate_Strength[key] + Final_Ferrous_Score.get(key, 0)
                    for key in  Scored_Ferrous_Alloys_Ultimate_Strength.keys()}

    Scoring_Ferrous_Alloys_Elongation = {key:  Rearranged_Ferrous_Alloys_Elongation[key] / Ferrous_Alloys_Elongation_Total.get(key, 0)
                    for key in  Rearranged_Ferrous_Alloys_Elongation.keys()}
    Scored_Ferrous_Alloys_Elongation = {key:  Scoring_Ferrous_Alloys_Elongation[key] * ferrous_elongation_multipliers.get(key, 0)
                    for key in  Scoring_Ferrous_Alloys_Elongation.keys()}
    Final_Ferrous_Score = {key:  Scored_Ferrous_Alloys_Elongation[key] + Final_Ferrous_Score.get(key, 0)
                    for key in  Scored_Ferrous_Alloys_Elongation.keys()}
    
    Scoring_Ferrous_Alloys_Elastic_Modulus = {key:  Rearranged_Ferrous_Alloys_Elastic_Modulus[key] / Ferrous_Alloys_Elastic_Modulus_Total.get(key, 0)
                    for key in  Rearranged_Ferrous_Alloys_Elastic_Modulus.keys()}
    Scored_Ferrous_Alloys_Elastic_Modulus = {key:  Scoring_Ferrous_Alloys_Elastic_Modulus[key] * ferrous_elastic_modulus_multipliers.get(key, 0)
                    for key in  Scoring_Ferrous_Alloys_Elastic_Modulus.keys()}
    Final_Ferrous_Score = {key:  Scored_Ferrous_Alloys_Elastic_Modulus[key] + Final_Ferrous_Score.get(key, 0)
                    for key in  Scored_Ferrous_Alloys_Elastic_Modulus.keys()}

    Scoring_Ferrous_Alloys_Density = {key:  Rearranged_Ferrous_Alloys_Density[key] / Ferrous_Alloys_Density_Total.get(key, 0)
                    for key in  Rearranged_Ferrous_Alloys_Density.keys()}
    Scored_Ferrous_Alloys_Density = {key:  Scoring_Ferrous_Alloys_Density[key] * ferrous_density_multipliers.get(key, 0)
                    for key in  Scoring_Ferrous_Alloys_Density.keys()}
    Final_Ferrous_Score = {key:  Scored_Ferrous_Alloys_Density[key] + Final_Ferrous_Score.get(key, 0)
                    for key in  Scored_Ferrous_Alloys_Density.keys()}

    Scoring_Ferrous_Alloys_Poissons_Ratio = {key:  Rearranged_Ferrous_Alloys_Poissons_Ratio[key] / Ferrous_Alloys_Poissons_Ratio_Total.get(key, 0)
                    for key in  Rearranged_Ferrous_Alloys_Poissons_Ratio.keys()}
    Scored_Ferrous_Alloys_Poissons_Ratio = {key:  Scoring_Ferrous_Alloys_Poissons_Ratio[key] * ferrous_poissons_ratio_multipliers.get(key, 0)
                    for key in  Scoring_Ferrous_Alloys_Poissons_Ratio.keys()}
    Final_Ferrous_Score = {key:  Scored_Ferrous_Alloys_Poissons_Ratio[key] + Final_Ferrous_Score.get(key, 0)
                    for key in  Scored_Ferrous_Alloys_Poissons_Ratio.keys()}
    
    #the score dictionary is rearranged so that the values can be sorted, and then swapped again to show the material abbreviations first
    #these abbreviatons are checked to print the best material name and use the classes to print its individual trait values 
    Sorting_Final_Ferrous_Score = {y: x for x, y in Final_Ferrous_Score.items()}
    Sorted_Final_Ferrous_Score={}
    for i in sorted(Sorting_Final_Ferrous_Score):
        Sorted_Final_Ferrous_Score[i]=Sorting_Final_Ferrous_Score[i]
    Final_Ferrous = {y: x for x, y in Sorted_Final_Ferrous_Score.items()}
    List_Ferrous = list(Final_Ferrous.keys())

    print('Points from worst to best: \n', list(Final_Ferrous.items()))
    print('\n')

    print("""The values provided have the following units: Yield Strength [ksi],
Ultimate Strength [ksi], Elongation [%], Elastic Modulus [psi],
Density [lb/in^3] and Poisson's Ratio has no units \n""")
    Ferrous_Result = (List_Ferrous[-1])
    if Ferrous_Result == 'CS1':
        print("Your best material would be Carbon Steel with the following details: ")
        print(vars(Carbon_Steel_1))
    elif Ferrous_Result == 'CS2':
        print("Your best material would be Carbon Steel with the following details: ")
        print(vars(Carbon_Steel_2))
    elif Ferrous_Result == 'AS1':
        print("Your best material would be Alloy Steel with the following details: ")
        print(vars(Alloy_Steel_1))
    elif Ferrous_Result == 'AS2':
        print("Your best material would be Alloy Steel with the following details: ")
        print(vars(Alloy_Steel_2))
    elif Ferrous_Result == 'SS1':
        print("Your best material would be Stainless Steel with the following details: ")
        print(vars(Stainless_Steel_1))
    elif Ferrous_Result == 'SS2':
        print("Your best material would be Stainless Steel with the following details: ")
        print(vars(Stainless_Steel_2))
    elif Ferrous_Result == 'CI1':
        print("Your best material would be Cast Iron with the following details: ")
        print(vars(Cast_Iron_1))
    elif Ferrous_Result == 'CI2':
        print("Your best material would be Cast Iron with the following details: ")
        print(vars(Cast_Iron_2))



Rearranged_Non_Ferrous_Alloys_Yield_Strength = {y: x for x, y in Sorted_Non_Ferrous_Alloys_Yield_Strength.items()}
Rearranged_Non_Ferrous_Alloys_Ultimate_Strength = {y: x for x, y in Sorted_Non_Ferrous_Alloys_Ultimate_Strength.items()}
Rearranged_Non_Ferrous_Alloys_Elongation = {y: x for x, y in Sorted_Non_Ferrous_Alloys_Elongation.items()}
Rearranged_Non_Ferrous_Alloys_Elastic_Modulus = {y: x for x, y in Sorted_Non_Ferrous_Alloys_Elastic_Modulus.items()}
Rearranged_Non_Ferrous_Alloys_Density = {y: x for x, y in Sorted_Non_Ferrous_Alloys_Density.items()}
Rearranged_Non_Ferrous_Alloys_Poissons_Ratio = {y: x for x, y in Sorted_Non_Ferrous_Alloys_Poissons_Ratio.items()}
if x==2:
    Scoring_Non_Ferrous_Alloys_Yield_Strength = {key:  Rearranged_Non_Ferrous_Alloys_Yield_Strength[key] / Non_Ferrous_Alloys_Yield_Strength_Total.get(key, 0)
                    for key in  Rearranged_Non_Ferrous_Alloys_Yield_Strength.keys()}
    Scored_Non_Ferrous_Alloys_Yield_Strength = {key:  Scoring_Non_Ferrous_Alloys_Yield_Strength[key] * non_ferrous_yield_strength_multipliers.get(key, 0)
                    for key in  Scoring_Non_Ferrous_Alloys_Yield_Strength.keys()}
    Final_Non_Ferrous_Score = Scored_Non_Ferrous_Alloys_Yield_Strength
    
    Scoring_Non_Ferrous_Alloys_Ultimate_Strength = {key:  Rearranged_Non_Ferrous_Alloys_Ultimate_Strength[key] / Non_Ferrous_Alloys_Ultimate_Strength_Total.get(key, 0)
                    for key in  Rearranged_Non_Ferrous_Alloys_Ultimate_Strength.keys()}
    Scored_Non_Ferrous_Alloys_Ultimate_Strength = {key:  Scoring_Non_Ferrous_Alloys_Ultimate_Strength[key] * non_ferrous_ultimate_strength_multipliers.get(key, 0)
                    for key in  Scoring_Non_Ferrous_Alloys_Ultimate_Strength.keys()}
    Final_Non_Ferrous_Score = {key:  Scored_Non_Ferrous_Alloys_Ultimate_Strength[key] + Final_Non_Ferrous_Score.get(key, 0)
                    for key in  Scored_Non_Ferrous_Alloys_Ultimate_Strength.keys()}

    Scoring_Non_Ferrous_Alloys_Elongation = {key:  Rearranged_Non_Ferrous_Alloys_Elongation[key] / Non_Ferrous_Alloys_Elongation_Total.get(key, 0)
                    for key in  Rearranged_Non_Ferrous_Alloys_Elongation.keys()}
    Scored_Non_Ferrous_Alloys_Elongation = {key:  Scoring_Non_Ferrous_Alloys_Elongation[key] * non_ferrous_elongation_multipliers.get(key, 0)
                    for key in  Scoring_Non_Ferrous_Alloys_Elongation.keys()}
    Final_Non_Ferrous_Score = {key:  Scored_Non_Ferrous_Alloys_Elongation[key] + Final_Non_Ferrous_Score.get(key, 0)
                    for key in  Scored_Non_Ferrous_Alloys_Elongation.keys()}
    
    Scoring_Non_Ferrous_Alloys_Elastic_Modulus = {key:  Rearranged_Non_Ferrous_Alloys_Elastic_Modulus[key] / Non_Ferrous_Alloys_Elastic_Modulus_Total.get(key, 0)
                    for key in  Rearranged_Non_Ferrous_Alloys_Elastic_Modulus.keys()}
    Scored_Non_Ferrous_Alloys_Elastic_Modulus = {key:  Scoring_Non_Ferrous_Alloys_Elastic_Modulus[key] * non_ferrous_elastic_modulus_multipliers.get(key, 0)
                    for key in  Scoring_Non_Ferrous_Alloys_Elastic_Modulus.keys()}
    Final_Non_Ferrous_Score = {key:  Scored_Non_Ferrous_Alloys_Elastic_Modulus[key] + Final_Non_Ferrous_Score.get(key, 0)
                    for key in  Scored_Non_Ferrous_Alloys_Elastic_Modulus.keys()}

    Scoring_Non_Ferrous_Alloys_Density = {key:  Rearranged_Non_Ferrous_Alloys_Density[key] / Non_Ferrous_Alloys_Density_Total.get(key, 0)
                    for key in  Rearranged_Non_Ferrous_Alloys_Density.keys()}
    Scored_Non_Ferrous_Alloys_Density = {key:  Scoring_Non_Ferrous_Alloys_Density[key] * non_ferrous_density_multipliers.get(key, 0)
                    for key in  Scoring_Non_Ferrous_Alloys_Density.keys()}
    Final_Non_Ferrous_Score = {key:  Scored_Non_Ferrous_Alloys_Density[key] + Final_Non_Ferrous_Score.get(key, 0)
                    for key in  Scored_Non_Ferrous_Alloys_Density.keys()}

    Scoring_Non_Ferrous_Alloys_Poissons_Ratio = {key:  Rearranged_Non_Ferrous_Alloys_Poissons_Ratio[key] / Non_Ferrous_Alloys_Poissons_Ratio_Total.get(key, 0)
                    for key in  Rearranged_Non_Ferrous_Alloys_Poissons_Ratio.keys()}
    Scored_Non_Ferrous_Alloys_Poissons_Ratio = {key:  Scoring_Non_Ferrous_Alloys_Poissons_Ratio[key] * non_ferrous_poissons_ratio_multipliers.get(key, 0)
                    for key in  Scoring_Non_Ferrous_Alloys_Poissons_Ratio.keys()}
    Final_Non_Ferrous_Score = {key:  Scored_Non_Ferrous_Alloys_Poissons_Ratio[key] + Final_Non_Ferrous_Score.get(key, 0)
                    for key in  Scored_Non_Ferrous_Alloys_Poissons_Ratio.keys()}
    

    Sorting_Final_Non_Ferrous_Score = {y: x for x, y in Final_Non_Ferrous_Score.items()}
    Sorted_Final_Non_Ferrous_Score={}
    for i in sorted(Sorting_Final_Non_Ferrous_Score):
        Sorted_Final_Non_Ferrous_Score[i]=Sorting_Final_Non_Ferrous_Score[i]
    Final_Non_Ferrous = {y: x for x, y in Sorted_Final_Non_Ferrous_Score.items()}
    List_Non_Ferrous = list(Final_Non_Ferrous.keys())

    print('Points from worst to best: \n', list(Final_Non_Ferrous.items()))
    print('\n')

    print("""The values provided have the following units: Yield Strength [ksi],
Ultimate Strength [ksi], Elongation [%], Elastic Modulus [psi],
Density [lb/in^3] and Poisson's Ratio has no units \n""")
    Non_Ferrous_Result = (List_Non_Ferrous[-1])
    if Non_Ferrous_Result == 'AA1':
        print("Your best material would be an Aluminium Alloy with the following details: ")
        print(vars(Aluminium_Alloys_1))
    elif Non_Ferrous_Result == 'AA2':
        print("Your best material would be an Aluminium Alloy with the following details: ")
        print(vars(Aluminium_Alloys_2))
    elif Non_Ferrous_Result == 'CA1':
        print("Your best material would be a Carbon Alloy with the following details: ")
        print(vars(Carbon_Alloys_1))
    elif Non_Ferrous_Result == 'CA2':
        print("Your best material would be a Carbon Alloy with the following details: ")
        print(vars(Carbon_Alloys_2))
    elif Non_Ferrous_Result == 'NA1':
        print("Your best material would be a Nickel Alloy with the following details: ")
        print(vars(Nickel_Alloys_1))
    elif Non_Ferrous_Result == 'NA2':
        print("Your best material would be a Nickel Alloy with the following details: ")
        print(vars(Nickel_Alloys_2))
    elif Non_Ferrous_Result == 'TA1':
        print("Your best material would be a Titanium Ally with the following details: ")
        print(vars(Titanium_Alloys_1))
    elif Non_Ferrous_Result == 'TA2':
        print("Your best material would be a Titanium Alloy with the following details: ")
        print(vars(Titanium_Alloys_2))
















   
