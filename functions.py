class physics_forms:
    # age calculator/birth year check
    def age_calculator():
        fn = input("Input 'a' to check your age,input 'y' to check your birth year: ")
        if fn == "a":
            year = int(input("whats your birth year: "))
            pres = int(input("what is the present year: "))
            final = pres - year
            print(final)
        elif fn == "y":
            age = int(input("how old are you: "))
            pres = int(input("what is the present year: "))
            final = pres - age
            print(final)
        else:
            print("wrong input")

    # Calculate the velocity of an object using the formula v = u + at, where v is the final velocity, u is the initial velocity, a is the acceleration, and t is the time.
    def calculate_velocity(u, a, t):
        """
        This function calculates the velocity of an object using the formula v = u + at.
        """
        v = u + a * t
        return v

    def calculate_kinetic_energy(m, v):
        """
        This function calculates the kinetic energy of an object using the formula KE = 0.5 * m * v^2.
        """
        ke = 0.5 * m * v ** 2
        return ke

    def calculate_distance(u, a, t):
        """
        This function calculates the distance traveled by an object using the formula d = ut + 0.5 * at^2.
        """
        d = u * t + 0.5 * a * t ** 2
        return d

    def calculate_power(F, v):
        """
        This function calculates the power of an object using the formula P = F * v.
        """
        P = F * v
        return P

    def calculate_gravitational_force(m1, m2, r):
        """
        This function calculates the gravitational force between two objects using the formula F = G * (m1 * m2) / r^2.
        """
        G = 6.67430e-11  # Gravitational constant
        F = G * (m1 * m2) / r ** 2
        return F

    import math

    def calculate_work_done(F, d, theta):
        """
        This function calculates the work done on an object using the formula W = F * d * cos(theta).
        """
        theta_rad = math.radians(theta)  # Convert angle to radians
        W = F * d * math.cos(theta_rad)
        return W

    def calculate_momentum(m, v):
        """
        This function calculates the momentum of an object using the formula p = m * v.
        """
        p = m * v
        return p

    def convert_wavelength_m_to_nm(wavelength_m):
        """
        This function converts a wavelength from meters to nanometers.
        """
        wavelength_nm = wavelength_m * 1e9
        return wavelength_nm

    def calculate_period(f):
        """
        This function calculates the period of a wave using the formula T = 1 / f.
        """
        T = 1 / f
        return T

    def calculate_resistance(V, I):
        """
        This function calculates the resistance of a resistor using Ohm's law: R = V / I.
        """
        R = V / I
        return R

    def calculate_capacitance(Q, V):
        """
        This function calculates the capacitance of a capacitor using the formula C = Q / V.
        """
        C = Q / V
        return C

    def calculate_inductance(Phi, I):
        """
        This function calculates the inductance of an inductor using the formula L = Phi / I.
        """
        L = Phi / I
        return L

    def calculate_power_IV(I, V):
        """
        This function calculates the power of an object using the formula P = IV.
        """
        P = I * V
        return P

    def calculate_power_I2R(I, R):
        """
        This function calculates the power of an object using the formula P = I^2 * R.
        """
        P = I


#