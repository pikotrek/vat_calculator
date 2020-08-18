class VatCalculator:
    def __init__(self, tax_rate):
        self.tax_rate = tax_rate * .01

    def gross(self, net):
        return net * (1 + self.tax_rate)

    def net(self, gross):
        return gross / (1 + self.tax_rate)

    def net_vat(self, gross):
        net = self.net(gross)
        return net, gross - net
