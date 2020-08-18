import unittest

from app.vat_calculator import VatCalculator, InvalidTaxRateError


class TestVatCalculator(unittest.TestCase):
    def setUp(self):
        self.vc = VatCalculator(23)

    def test_gross(self):
        self.assertEqual(self.vc.gross(100), 123)

    def test_net(self):
        self.assertEqual(self.vc.net(123), 100)

    def test_net_vat(self):
        self.assertEqual(self.vc.net_vat(123), (100, 23))

    def test_net__float(self):
        self.assertAlmostEqual(self.vc.net(129), 104.88, places=2)

    def test_create__invalid(self):
        with self.assertRaises(InvalidTaxRateError):
            VatCalculator(-21)
