class Operacion:
    # Inicializa los polinomios que luego usa para operar
    def __init__(self, polinomio1, polinomio2):
        self.polinomio1 = polinomio1
        self.polinomio2 = polinomio2
        return
    def operar(self, operacion):
        if operacion == "+":
            return self.suma()
        if operacion == "-":
            return self.res()
    def res(self):
        return self.polinomio1 - self.polinomio2
    def suma(self):
	    return self.polinomio1 + self.polinomio2
