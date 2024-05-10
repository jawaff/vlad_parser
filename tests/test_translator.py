# This is for investigation purposes...

import unittest
from vlad_parser.translator import TokenTranslator


class TestTokenTranslator(unittest.TestCase):
    def test_tokenizer(self):
        translator = TokenTranslator("../text2sql4j/raw-files/flan-t5-large/tokenizer.json", ['order by', 'ORDER BY', 'desc', 'DESC'])
        print(translator.translate("decode"))
        print(translator.translate("decoding"))
        print(translator.translate("translate"))
        print(translator.translate("translating"))
        print(translator.translate("running"))
        print(translator.translate("run"))
        print(translator.translate("n"))
        print(translator.translate("ing"))
        print(translator.decode([661, 29, 53]))

        print(translator.decode([32, 52, 26, 15, 52]))
        print(translator.decode([32, 52, 26, 49]))
        print(translator.decode([42, 26, 15, 52]))
        print(translator.decode([42, 26, 49]))
        print(translator.decode([455]))
        print(translator.decode([32100]))
        print(translator.decode([32101]))
        print(translator.decode([32103]))
        print(translator.decode([32102]))
        print(translator.translate("er"))
        print(translator.translate("order by column desc"))
        print(translator.translate("ORDER BY column DESC"))


        print(translator.translate("SELECT count FROM count WHERE count < 10 ORDER BY count"))

        print(translator.translate("S"))
        print(translator.translate("SE"))
        print(translator.translate("SEL"))
        print(translator.translate("SELE"))
        print(translator.translate("SELEC"))
        print(translator.translate("SELECT"))
        print(translator.decode([23143]))
        print(translator.decode([14196]))
        print(translator.decode([23143, 14196]))

        print(translator.decode([93]))
        print(translator.decode([75]))
        print(translator.decode([455, 57]))
        print(translator.decode([6710]))

        print(translator.decode([4674]))
        print(translator.decode([11300]))
        print(translator.decode([272]))
        print(translator.decode([476]))
        print(translator.decode([309]))
        print(translator.decode([25067]))

if __name__ == '__main__':
    unittest.main()
