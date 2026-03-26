#einstein e = mc^2

# This function calculates the energy equivalent of a given mass using Einstein's equation E=mc^2.
def energy(mass):
    c = 299792458 # speed of light in m/s
    return mass * c ** 2

def main():
    # take input for mass in kilograms
    mass_input = float(input("Enter the mass in kilograms: "))

    # calculate energy using the energy function
    energy_output = energy(mass_input)

    # print the result
    print(f"The energy equivalent of {mass_input} kg is {energy_output} joules.")
 
main()  