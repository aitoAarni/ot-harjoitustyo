import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(100)

    def test_atribuutit_oikein1(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)


    def test_atribuutit_oikein2(self):
        self.assertEqual(self.kassa.edulliset, 0)


    def test_atribuutit_oikein3(self):
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_toimii_edullisilla_kun_on_varaa1(self):
        kateinen = 241
        maksu = self.kassa.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000 + 240)

    def test_kateisosto_toimii_edullisilla_kun_on_varaa2(self):
        kateinen = 241
        maksu = self.kassa.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(self.kassa.edulliset, 1)

    def test_kateisosto_toimii_edullisilla_kun_on_varaa3(self):
        kateinen = 241
        maksu = self.kassa.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(maksu, kateinen - 240)

    def test_kateisosto_toimii_edullisilla_kun_ei_ole_varaa1(self):
        kateinen = 200
        maksu = self.kassa.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_edullisilla_kun_ei_ole_varaa2(self):
        kateinen = 200
        maksu = self.kassa.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisosto_toimii_edullisilla_kun_ei_ole_varaa3(self):
        kateinen = 200
        maksu = self.kassa.syo_edullisesti_kateisella(kateinen)
        self.assertEqual(maksu, kateinen)

    def test_kaitesosto_toimii_maukkaalla_kun_on_varaa1(self):
        kateinen = 401
        maksu = self.kassa.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000+400)

    def test_kaitesosto_toimii_maukkaalla_kun_on_varaa2(self):
        kateinen = 401
        maksu = self.kassa.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_kaitesosto_toimii_maukkaalla_kun_on_varaa3(self):
        kateinen = 401
        maksu = self.kassa.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(maksu, kateinen-400)


    def test_kateisosto_toimii_maukkaalla_kun_ei_ole_varaa1(self):
        kateinen = 200
        maksu = self.kassa.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kateisosto_toimii_maukkaalla_kun_ei_ole_varaa2(self):
        kateinen = 200
        maksu = self.kassa.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisosto_toimii_maukkaalla_kun_ei_ole_varaa3(self):
        kateinen = 200
        maksu = self.kassa.syo_maukkaasti_kateisella(kateinen)
        self.assertEqual(maksu, kateinen)

    def test_kortti_osto_toimii_edullisille_kun_on_katetta1(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 401 - 240)

    def test_kortti_osto_toimii_edullisille_kun_on_katetta2(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)


    def test_kortti_osto_toimii_edullisille_kun_on_katetta3(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(maksu_onnistui, True)

    def test_kortti_osto_toimii_edullisille_kun_on_katetta4(self):
            self.kortti.lataa_rahaa(301)
            maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
            self.assertEqual(self.kassa.kassassa_rahaa, 100000)


    def test_kortti_osto_toimii_edullisilla_kun_ei_ole_saldoa1(self):
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)

    def test_kortti_osto_toimii_edullisilla_kun_ei_ole_saldoa2(self):
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 0)


    def test_kortti_osto_toimii_edullisilla_kun_ei_ole_saldoa3(self):
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(maksu_onnistui, False)


    def test_kortti_osto_toimii_edullisilla_kun_ei_ole_saldoa4(self):
        maksu_onnistui = self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortti_osto_toimii_maukkailla_kun_on_katetta1(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 401 - 400)

    def test_kortti_osto_toimii_maukkailla_kun_on_katetta2(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(maksu_onnistui, True)

    def test_kortti_osto_toimii_maukkailla_kun_on_katetta3(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual( self.kassa.maukkaat, 1, 100000)

    def test_kortti_osto_toimii_maukkailla_kun_on_katetta4(self):
        self.kortti.lataa_rahaa(301)
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)


    def test_kortti_osto_toimii_maukkailla_kun_ei_ole_saldoa1(self):
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 100)

    def test_kortti_osto_toimii_maukkailla_kun_ei_ole_saldoa2(self):
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(maksu_onnistui, False)

    def test_kortti_osto_toimii_maukkailla_kun_ei_ole_saldoa3(self):
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kortti_osto_toimii_maukkailla_kun_ei_ole_saldoa4(self):
        maksu_onnistui = self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortilla_ladataan_rahaa_toimii_ja_kassaan_tulee_lisaa_rahaa1(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 1100)

    def test_kortilla_ladataan_rahaa_toimii_ja_kassaan_tulee_lisaa_rahaa2(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortille_ladataan_negatiivinen_maara_rahaa1(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -3)
        self.assertEqual(str(self.kortti), "saldo: 1.0")

    def test_kortille_ladataan_negatiivinen_maara_rahaa2(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -3)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)


    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.kortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.kortti), "saldo: 1.0")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.kortti.lataa_rahaa(101)
        self.assertEqual(str(self.kortti), "saldo: 2.01")

    def test_saldo_vahenee_oikein(self):
        self.kortti.ota_rahaa(9)
        self.assertEqual(str(self.kortti), "saldo: 0.91")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.kortti.ota_rahaa(1001)
        self.assertEqual(str(self.kortti), "saldo: 1.0")

    def test_metodi_palauttaa_true_jos_rahaa_riittavasti(self):
        arvo = self.kortti.ota_rahaa(3)
        self.assertEqual(arvo, True)

    def test_metodi_palauttaa_false_jos_rahaa_ei_ole_riittavasti(self):
        arvo = self.kortti.ota_rahaa(10000000)
        self.assertEqual(arvo, False)