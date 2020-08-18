from app.vat_calculator import VatCalculator

if __name__ == '__main__':
    vc = VatCalculator(22)
    print(vc.gross(101))
    print(vc.net(123))
    print(vc.net_vat(123))
