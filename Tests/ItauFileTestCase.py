import unittest
from pg_cnab240.file import File
from pg_cnab240.company import Company
from pg_cnab240.payment import Payment
import os

# create company object
company = Company('BF Servicos De Cobranca Ltda', '07179434000140')
company.set_bank_acccount(341, '00772', '69637', 3)
company.set_address('Av. Andrômeda', 2000, 'Bl.8-4 andar', 'Alphaville Residencial Plus', 'Barueri', 'SP', '06473000')

company_j = Company('Arizona 701', '20093235000182')
company_j.set_bank_acccount(237, '0296', '01081', 2)
company_j.set_address('Rua Arizona', 701, '', 'Brooklin', 'São Paulo', 'SP', '04567002')


class ItauFileTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
    #
    # @staticmethod
    # def test_1_generate_header():
    #     payment_file = File('Itau', company)
    #     payment_file.header.set_company_data(company)
    #     header_line = payment_file.header.to_line()
    #     assert '240' in str(len(header_line))
    #
    # @staticmethod
    # def test_2_process_one_paymentA():
    #     payment_file = File('Itau', company)
    #     payment_file.header.set_company_data(company)
    #     payment_file.payments = []
    #
    #     payment = Payment(type='ted',
    #                       favored_name='Cliente Teste',
    #                       favored_bank='033', agency='01111',
    #                       account='000011111111',
    #                       account_digit=0,
    #                       your_number='5511972063805440',
    #                       pay_date='10052018',
    #                       ispb_code='90400888',
    #                       payment_amount=2400.00,
    #                       favored_document_number='11111111111111')
    #
    #     # add payment
    #     payment_file.add_payment(payment)
    #
    #     # generate
    #     payment_file.generate()
    #
    #     body_big_line = ''.join(payment_file.body)
    #
    #     root_path = os.path.dirname(os.path.abspath(__file__))
    #     body_big_file_path = os.path.join(root_path, 'body_big_file_segment_a.rem')
    #     f = open(body_big_file_path, 'w')
    #     f.write(body_big_line)
    #     f.close()
    #
    #     assert '34100011C2041040 207179434000140                    01111 000011111111 3BF SERVICOS DE COBRANCA LTDA' \
    #            '                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI' \
    #            '             06473000SP                  3410001300001A00000003301111 000011111111 0CLIENTE TESTE' \
    #            '                 5511972063805440    10052018REA904008880000000000000000240000' \
    #            '                            000000000000000                    00000011111111111111' \
    #            '                       34100015         000003000000000000240000000000000000000000' \
    #            '                                                                                                    ' \
    #            '                                                                                 ' in body_big_line
    #
    @staticmethod
    def test_3_process_one_paymentJ():
        payment_file = File('Itau', company)
        payment_file.header.set_company_data(company)
        payment_file.payments = []

        payment = Payment(type='other_bank_slip',
                          favored_name=company_j.name,
                          favored_bank=company_j.bank_account.bank_code,
                          agency=company.bank_account.agency,
                          account=company.bank_account.account,
                          account_digit=company.bank_account.digit,
                          pay_date='05072019',
                          currency_type=9,
                          dv='3',
                          due_rule='7941',
                          amount=1029.41,
                          free_field='0296090001270557500010810',
                          due_date='05072019',
                          title_amount=1029.41,
                          payment_amount=1029.41,
                          your_number='12345678901234567890',
                          recipient_document_type=2,
                          recipient_document_number=20093235000182,
                          recipient_name='ARIZONA 701')

        # add payment
        payment_file.add_payment(payment)

        # generate
        payment_file.generate()
        body_big_line = payment_file.get_content()

        root_path = os.path.dirname(os.path.abspath(__file__))
        body_big_file_path = os.path.join(root_path, 'body_big_file_segment_j.rem')
        f = open(body_big_file_path, 'w')
        f.write(body_big_line)
        f.close()

        assert '34100011C2031030 207179434000140                    01111 000011111111 3BF SERVICOS DE COBRANCA LTDA' \
               '                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI ' \
               '            06473000SP                  3410001300001J00003394752400010067609485239700000007661190101' \
               'CLIENTE TESTE                 14052018000000001006760000000000000000000000000000000100520180000000010' \
               '067600000000000000005506715023835136                                          34100015         000003' \
               '000000000001006760000000000000000000                                                                 ' \
               '                                                                                                     ' \
               '               ' in body_big_line
    #
    # @staticmethod
    # def test_4_process_one_paymentANF():
    #     payment_file = File('Itau', company)
    #     payment_file.header.set_company_data(company)
    #     payment_file.payments = []
    #
    #     payment = Payment(type='nf',
    #                       favored_name='Cliente Teste',
    #                       favored_bank='033', agency='01111',
    #                       account='000011111111',
    #                       account_digit=0,
    #                       pay_date='10052018',
    #                       ispb_code='90400888',
    #                       payment_amount=10067.60,
    #                       dv='4',
    #                       due_rule='7524',
    #                       amount=10067.60,
    #                       free_field='9485239700000007661190101',
    #                       due_date='14052018',
    #                       title_amount=10067.60,
    #                       your_number='5511972063805440',
    #                       nf_document='5646510065784320',
    #                       favored_document_number='11111111111111')
    #
    #     # add payment
    #     payment_file.add_payment(payment)
    #
    #     # generate
    #     payment_file.generate()
    #     body_big_line = ''.join(payment_file.body)
    #
    #     root_path = os.path.dirname(os.path.abspath(__file__))
    #     body_big_file_path = os.path.join(root_path, 'body_big_file_segment_anf.rem')
    #     f = open(body_big_file_path, 'w')
    #     f.write(body_big_line)
    #     f.close()
    #
    #     assert '34100011C2041040 207179434000140                    01111 000011111111 3BF SERVICOS DE COBRANCA LTDA' \
    #            '                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI ' \
    #            '            06473000SP                  3410001300001A00000003301111 000011111111 0CLIENTE TESTE    ' \
    #            '             5511972063805440    10052018REA000000000000000000000001006760                          ' \
    #            '  00000000000000056465100657843      000000111111111111112                      34100015        ' \
    #            ' 000003000000000001006760000000000000000000                                                      ' \
    #            '                                                                                                  ' \
    #            '                             ' in body_big_line
    #
    # @staticmethod
    # def test_5_process_many_payments():
    #     payment_file = File('Itau', company)
    #     payment_file.header.set_company_data(company)
    #     payment_file.payments = []
    #
    #     payment_a = Payment(type='ted',
    #                         favored_name='Cliente Teste',
    #                         favored_bank='033',
    #                         agency='01111',
    #                         account='000011111111',
    #                         account_digit=0,
    #                         your_number='5511972063805440',
    #                         pay_date='10052018',
    #                         ispb_code='90400888',
    #                         payment_amount=2400.00,
    #                         favored_document_number='11111111111111')
    #
    #     payment_j = Payment(type='other_bank_slip',
    #                         favored_name='Cliente Teste',
    #                         favored_bank='033',
    #                         agency='01111',
    #                         account='000011111111',
    #                         account_digit=0,
    #                         pay_date='10052018',
    #                         ispb_code='90400888',
    #                         currency_type=9,
    #                         dv='4',
    #                         due_rule='7524',
    #                         amount=10067.60,
    #                         free_field='9485239700000007661190101',
    #                         due_date='14052018',
    #                         title_amount=10067.60,
    #                         payment_amount=10067.60,
    #                         your_number='5506715023835136')
    #
    #     payment_anf = Payment(type='nf',
    #                           favored_name='Cliente Teste',
    #                           favored_bank='033',
    #                           agency='01111',
    #                           account='000011111111',
    #                           account_digit=0,
    #                           pay_date='10052018',
    #                           ispb_code='90400888',
    #                           payment_amount=10067.60,
    #                           dv='4',
    #                           due_rule='7524',
    #                           amount=10067.60,
    #                           free_field='9485239700000007661190101',
    #                           due_date='14052018',
    #                           title_amount=10067.60,
    #                           your_number='5511972063805440',
    #                           nf_document='5646510065784320',
    #                           favored_document_number='11111111111111')
    #
    #     # add payments
    #     payment_file.add_payment(payment_a)
    #     payment_file.add_payment(payment_j)
    #     payment_file.add_payment(payment_anf)
    #
    #     # generate
    #     payment_file.generate()
    #     body_big_line = ''.join(payment_file.body)
    #
    #     root_path = os.path.dirname(os.path.abspath(__file__))
    #     body_big_file_path = os.path.join(root_path, 'body_big_file_multiples_segments.rem')
    #     f = open(body_big_file_path, 'w')
    #     f.write(body_big_line)
    #     f.close()
    #
    #     assert '34100011C2041040 207179434000140                    01111 000011111111 3BF SERVICOS DE COBRANCA LTDA' \
    #            '                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI' \
    #            '             06473000SP                  3410001300001A00000003301111 000011111111 0CLIENTE TESTE' \
    #            '                 5511972063805440    10052018REA904008880000000000000000240000                      ' \
    #            '      000000000000000                    00000011111111111111                       34100015         ' \
    #            '000003000000000000240000000000000000000000                                                           ' \
    #            '                                                                                                     ' \
    #            '                     34100021C2031030 207179434000140                    ' \
    #            '01111 000011111111 3BF SERVICOS DE COBRANCA LTDA                                          ' \
    #            'AV ANDROMEDA                  02000BL84 ANDAR     BARUERI             06473000SP                  ' \
    #            '3410002300001J00003394752400010067609485239700000007661190101CLIENTE TESTE                 ' \
    #            '14052018000000001006760000000000000000000000000000000100520180000000010067600000000000000005506715023' \
    #            '835136                                          34100025         000003000000000001006760000000000000' \
    #            '000000                                                                                               ' \
    #            '                                                                                      ' \
    #            '34100031C2041040 207179434000140                    01111 000011111111 3BF SERVICOS DE COBRANCA LTDA' \
    #            '                                          AV ANDROMEDA                  02000BL84 ANDAR     BARUERI' \
    #            '             06473000SP                  3410003300001A00000003301111 000011111111 0CLIENTE TESTE    ' \
    #            '             5511972063805440    10052018REA000000000000000000000001006760                           ' \
    #            ' 00000000000000056465100657843      000000111111111111112                      34100035         ' \
    #            '000003000000000001006760000000000000000000                                                           ' \
    #            '                                                                                                     ' \
    #            '                     ' in body_big_line
    #
    # @staticmethod
    # def test_6_generate_footer():
    #     payment_file = File('Itau', company)
    #     payment_file.header.set_company_data(company)
    #     payment_file.payments = []
    #
    #     payment_a = Payment(type='ted',
    #                         favored_name='Cliente Teste',
    #                         favored_bank='033',
    #                         agency='01111',
    #                         account='000011111111',
    #                         account_digit=0,
    #                         your_number='5511972063805440',
    #                         pay_date='10052018',
    #                         ispb_code='90400888',
    #                         payment_amount=2400.00,
    #                         favored_document_number='11111111111111')
    #
    #     payment_j = Payment(type='other_bank_slip',
    #                         favored_name='Cliente Teste',
    #                         favored_bank='033', agency='01111',
    #                         account='000011111111',
    #                         account_digit=0,
    #                         pay_date='10052018',
    #                         ispb_code='90400888',
    #                         currency_type=9,
    #                         dv='4',
    #                         due_rule='7524',
    #                         amount=10067.60,
    #                         free_field='9485239700000007661190101',
    #                         due_date='14052018',
    #                         title_amount=10067.60,
    #                         payment_amount=10067.60,
    #                         your_number='5506715023835136')
    #
    #     payment_anf = Payment(type='nf',
    #                           favored_name='Cliente Teste',
    #                           favored_bank='033',
    #                           agency='01111',
    #                           account='000011111111',
    #                           account_digit=0,
    #                           pay_date='10052018',
    #                           ispb_code='90400888',
    #                           payment_amount=10067.60,
    #                           dv='4', due_rule='7524',
    #                           amount=10067.60,
    #                           free_field='9485239700000007661190101',
    #                           due_date='14052018',
    #                           title_amount=10067.60,
    #                           your_number='5511972063805440',
    #                           nf_document='5646510065784320',
    #                           favored_document_number='11111111111111')
    #
    #     # add payment
    #     payment_file.add_payment(payment_a)
    #     payment_file.add_payment(payment_j)
    #     payment_file.add_payment(payment_anf)
    #
    #     # generate
    #     payment_file.generate()
    #
    #     footer_line = payment_file.footer.to_line()
    #     assert '34199999         000003000011                                                                        ' \
    #            '                                                                                                     ' \
    #            '                                      ' in footer_line
    #
    # @staticmethod
    # def test_7_save_file():
    #     payment_file = File('Itau', company)
    #     payment_file.header.set_company_data(company)
    #     payment_file.payments = []
    #
    #     payment_a = Payment(type='ted',
    #                         favored_name='Cliente Teste',
    #                         favored_bank='033',
    #                         agency='01111',
    #                         account='000011111111',
    #                         account_digit=0,
    #                         your_number='5511972063805440',
    #                         pay_date='10052018',
    #                         ispb_code='90400888',
    #                         payment_amount=2400.00,
    #                         favored_document_number='11111111111111')
    #
    #     payment_j = Payment(type='other_bank_slip',
    #                         favored_name='Cliente Teste',
    #                         favored_bank='033',
    #                         agency='01111',
    #                         account='000011111111',
    #                         account_digit=0,
    #                         pay_date='10052018',
    #                         ispb_code='90400888',
    #                         currency_type=9,
    #                         dv='4',
    #                         due_rule='7524',
    #                         amount=10067.60,
    #                         free_field='9485239700000007661190101',
    #                         due_date='14052018',
    #                         title_amount=10067.60,
    #                         payment_amount=10067.60,
    #                         your_number='5506715023835136')
    #
    #     payment_anf = Payment(type='nf',
    #                           favored_name='Cliente Teste',
    #                           favored_bank='033',
    #                           agency='01111',
    #                           account='000011111111',
    #                           account_digit=0,
    #                           pay_date='10052018',
    #                           ispb_code='90400888',
    #                           payment_amount=10067.60,
    #                           dv='4',
    #                           due_rule='7524',
    #                           amount=10067.60,
    #                           free_field='9485239700000007661190101',
    #                           due_date='14052018',
    #                           title_amount=10067.60,
    #                           your_number='5511972063805440',
    #                           nf_document='5646510065784320',
    #                           favored_document_number='11111111111111')
    #
    #     # add payments
    #     payment_file.add_payment(payment_a)
    #     payment_file.add_payment(payment_j)
    #     payment_file.add_payment(payment_anf)
    #
    #     # generate
    #     file_full_path = payment_file.generate(os.path.dirname(os.path.abspath(__file__)))
    #
    #     f = open(file_full_path, 'r')
    #     file_content = f.read()
    #     f.close()
    #
    #     assert file_content in file_content
    #
    # @staticmethod
    # def test_8_read_header_from_file():
    #     payment_file = File('Itau')
    #     payment_file.payments = []
    #
    #     f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'SB23058F.RET'), 'r')
    #     file_content = f.read()
    #     f.close()
    #
    #     payment_file.read_file_content(file_content)
    #
    #     assert file_content in file_content


if __name__ == '__main__':
    unittest.main()
