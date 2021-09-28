class dadaa:
    basketball = 3


class pappa(dadaa):
    dance = 2

    def isdance(self):
        return f"pappa can dance, {self.dance} no. of times"


class beta(pappa):
    dance = 4

    def isdance(self):  # overriding method
        return f"I can do better, i dance today {self.dance} no. of times"


dhruvin = beta()
papa = pappa()
dada = dadaa()
print(beta().isdance())  # overriding
print(papa.isdance())
print(dhruvin.basketball)  # dhruvin can access the attribute of dada
