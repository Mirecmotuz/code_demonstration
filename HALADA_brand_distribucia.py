import csv
import time

import pandas as pd
import datetime as datetime
import sys
#sys.path.append(r"C:\Users\martin.minarik\OneDrive - ALO jewelry CZ, s.r.o\Desktop\programovanie\AI")
sys.path.append(r"C:\Users\Public\Projekty\univerzalni")
from Data import Data

pd.set_option("display.max_rows", None, "display.max_columns", None, "display.width", None)

class Distribucia_brand_HALADA:

    butiky = ["HALADA PRIKOPY", "HALADA PARIZSKA", "HALADA BRNO", "HALADA EUROVEA BRATISLAVA",
              "HALADA AVION BRATISLAVA", "HALADA AVION OSTRAVA"]

    but_sklad = {"HALADA AVION BRATISLAVA": "H7O", "HALADA AVION OSTRAVA": "H7P", "HALADA BRNO": "H74",
                 "HALADA EUROVEA BRATISLAVA": "H7N", "HALADA PARIZSKA": "H71", "HALADA PRIKOPY": "H72"}

    butiky_slabe = ["HALADA AVION BRATISLAVA", "HALADA AVION OSTRAVA"]

    id_dodavatelov = {4279: 'Heinrich Lausch GmbH & Co.KG', 4246: 'Hans Rivoir GmbH', 4273: 'Capolavoro',
                      4285: 'DiamondGroup GmbH', 4243: 'Burkhardt + Bischoff GmbH & Co.', 4282: 'FOPE S.P.A.',
                      4242: 'Jörg Heinz GmbH & Co.', 6340: 'LIAPIS DIMITRIOS Co. LP', 5700: 'Roberto Coin S.p.A.',
                      4283: 'Niessing Manufaktur GmbH & Co. KG', 6298: 'Marco Gerbella Orafo srl',
                      4248: 'Miriam Marietta Halada-Mirisign', 4697: 'Jennifer Halada', 4918: 'Gellner GmbH',
                      4280: 'Wurster Diamonds GmbH', 6308: 'Burato Gioielli', 4276: 'Pomellato Spa',
                      4788: 'Leo Wittwer GmbH&Co.KG', 4272: 'K. Mikimoto & Co., LTD', 6559: 'Rusconi s.r.l.',
                      4495: 'Scheffel Schmuck', 4482: 'Monika Seitter', 4275: 'Artur Scholl GmbH',
                      4483: 'Victor Mayer GmbH', 4247: 'Euripides Taloumis & Co. O.E.', 4414: 'Eugen Rühle GmbH + Co. KG',
                      4278: 'Pearl Style GmbH', 4277: 'August Gerstner GmbH & Co.KG', 5525: 'Autore Europe GmbH',
                      4244: 'J. Köhle Schmuck-Vertriebs GmbH', 4286: 'Richard Hans Becker GmbH & Co.KG',
                      4488: 'R. BRON B.V.', 4413: 'Andreas Daub GmbH', 4274: 'Crivelli gioielli s.r.',
                      4281: 'Schoeffel GmbH', 4481: 'Christian Bauer Schmuck GmbH', 4407: 'Hans D. Krieger KG',
                      2379: 'Falcoral snc di Falanga', 4494: 'A.M.C.', 4493: 'FACCO Corporation S.r.l.',
                      4490: 'OROGEM Jewelers', 4492: 'CP s.n.c. di Pomi Claudio', 4335: 'Breuning GmbH',
                      4487: 'Damaso Martinez, S.L.', 4412: 'Ruppenthal', 4240: 'Friedrich Binder GmbH & Co. KG',
                      4411: 'Quinn Scheurle GmbH', 4489: 'Garschal GmbH', 4480: 'Patrick Meyer',
                      4477: 'WAI YIP Pearl Company LTD', 2493: 'RMC Gems HK CO.', 4484: 'Pranda and Kroll GmbH',
                      6236: 'Brigitte Bergelt', 0: 'nemam'}

    dodavatel_na_id = {'Heinrich Lausch GmbH & Co.KG': 4279, 'Hans Rivoir GmbH': 4246, 'Capolavoro': 4273,
                       'DiamondGroup GmbH': 4285, 'Burkhardt + Bischoff GmbH & Co.': 4243, 'FOPE S.P.A.': 4282,
                       'Jörg Heinz GmbH & Co.': 4242, 'LIAPIS DIMITRIOS Co. LP': 6340, 'Roberto Coin S.p.A.': 5700,
                       'Niessing Manufaktur GmbH & Co. KG': 4283, 'Marco Gerbella Orafo srl': 6298,
                       'Miriam Marietta Halada-Mirisign': 4248, 'Jennifer Halada': 4697, 'Gellner GmbH': 4918,
                       'Wurster Diamonds GmbH': 4280, 'Burato Gioielli': 6308, 'Pomellato Spa': 4276,
                       'Leo Wittwer GmbH&Co.KG': 4788, 'K. Mikimoto & Co., LTD': 4272, 'Rusconi s.r.l.': 6559,
                       'Scheffel Schmuck': 4495, 'Monika Seitter': 4482, 'Artur Scholl GmbH': 4275,
                       'Victor Mayer GmbH': 4483, 'Euripides Taloumis & Co. O.E.': 4247, 'Eugen Rühle GmbH + Co. KG': 4414,
                       'Pearl Style GmbH': 4278, 'August Gerstner GmbH & Co.KG': 4277, 'Autore Europe GmbH': 5525,
                       'J. Köhle Schmuck-Vertriebs GmbH': 4244, 'Richard Hans Becker GmbH & Co.KG': 4286, 'R. BRON B.V.': 4488,
                       'Andreas Daub GmbH': 4413, 'Crivelli gioielli s.r.': 4274, 'Schoeffel GmbH': 4281,
                       'Christian Bauer Schmuck GmbH': 4481, 'Hans D. Krieger KG': 4407, 'Falcoral snc di Falanga': 2379,
                       'A.M.C.': 4494, 'FACCO Corporation S.r.l.': 4493, 'OROGEM Jewelers': 4490,
                       'CP s.n.c. di Pomi Claudio': 4492, 'Breuning GmbH': 4335, 'Damaso Martinez, S.L.': 4487,
                       'Ruppenthal': 4412, 'Friedrich Binder GmbH & Co. KG': 4240, 'Quinn Scheurle GmbH': 4411,
                       'Garschal GmbH': 4489, 'Patrick Meyer': 4480, 'WAI YIP Pearl Company LTD': 4477, 'RMC Gems HK CO.': 2493,
                       'Pranda and Kroll GmbH': 4484, 'Brigitte Bergelt': 6236, 'nemam': 0}


    def __init__(self):
        self.zdroj_data_butiky = Data(druhy_dat=["HALADA"], brandy=["H"], butiky=True)
        self.data_halada = self.zdroj_data_butiky.upravene_data()
        self.na_butikoch = self.data_halada.loc[self.data_halada["datum_prodej"].isna()].copy()

        self.dnes = pd.to_datetime(datetime.date.today())

        self.povodne_data_distribucia = self.nacitaj_distribuciu() #sem zapisem vysledky len
        #self.povodne_data_distribucia = self.nacitaj_distribuciu_alt()
        #self.data_distribucia = self.uprav_data_alt(self.povodne_data_distribucia.copy())
        self.data_distribucia = self.uprav_data(self.povodne_data_distribucia.copy())

        print(self.data_distribucia)

        self.zdroj_data_ostatne = Data(butiky=False)

        self.butiky_skladove_limity = self.vytvor_limity_skladov()

        #info subory
        self.udaje_o_distribucii = pd.DataFrame(columns = ["dodavatel", "typ_sperku", "butik", "prav_skup",
                                                           "pocet_skup_na_butiku", "rozdel_pocet_skup", "model",
                                                           "na_rozdel", "prav_model", "pocet_model_butik", "final_rozdelenie"])

        self.udaje_o_prideleni = pd.DataFrame(columns = ["index_celkovy", "ID", "model", "cenkat", "kamen",
                                                         "zlato", "prideleny_butik", "butik_pred_manipulaciou","manipulacia"])


    def nacitaj_distribuciu_alt(self):
        data = pd.read_excel(r"C:\Users\martin.minarik\OneDrive - ALO jewelry CZ, s.r.o\Desktop\data k distr.Halada 23.5..xlsx", header=0,
                             sheet_name = "List2")

        data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        return data

    def uprav_data_alt(self, data: pd.DataFrame) -> pd.DataFrame:
        data.rename(columns={"Šarže": "zaruky", "Zboží": "ID",
                             "CenKat": "Ex_CenKat", "Brand": "Ex_Brand",
                             "Komodita": "Ex_Komodita", "Velikost": "Ex_Velikost",
                             "Kam. briliant": "Ex_KBriliant", "Kam. přírodní": "Ex_KPrirod",
                             "Kamenovost": "Ex_Kamenovost", "Barva prir kamene": "Ex_BarvaPrirKam",
                             "Barva": "Ex_Barva", "Barva kovu": "Ex_BarvaKovu",
                             }, inplace = True)

        data = self.zdroj_data_butiky.uprav_data_alo(data, typ="distribucia")

        # pridam stlpec 9 znakov
        data["9_znakov"] = data["ID"].str.slice(0, 9).copy()
        data["Butik"] = None

        return data

    def vytvor_limity_skladov(self):
        """
        od predom urcenych limitov odpocitame aktualne stavy na butikoch, a to budu nase vysledne limity

        po novom sme sa rozhodli ze limity butikov mat nebudeme, tak ich akurat nastavim na neprekrocitelne hodnoty
        :return:
        """
        limity = {"HALADA AVION BRATISLAVA": 10000, "HALADA AVION OSTRAVA": 10000, "HALADA BRNO": 10000,
                 "HALADA EUROVEA BRATISLAVA": 10000, "HALADA PARIZSKA": 10000, "HALADA PRIKOPY": 10000}
        for butik in self.butiky:
            #zistim pocty na butikoch a odratam
            na_butiku = self.na_butikoch.loc[self.na_butikoch["butik"] == butik].shape[0]
            limity[butik] =  max(0, limity[butik] - na_butiku)


        return limity

    def nacitaj_distribuciu(self):
        """
        nacita distribucne data a upravi o medzery na zaciatku a konci slov
        :return:
        """
        with open(r"\\10.10.10.3\data\99_AI\K2 OUT\DistribuceOUTHalada.csv", "r", encoding="cp1250") as src_file, open(
                r"C:\Users\Public\Projekty\HALADA\HALADA_distribucia\DistribuceOUTHalada_bez_uvodzoviek.csv", 'w',
                encoding="cp1250") as dst_file:
            for line in src_file.read().split('\n'):
                line = line.strip(",")

                dst_file.write(line.replace('"', '') + '\n')

        data = pd.read_csv(r"C:\Users\Public\Projekty\HALADA\HALADA_distribucia\DistribuceOUTHalada_bez_uvodzoviek.csv", header = 0,
                           sep = "\t", encoding = "cp1250")

        data = data.applymap(lambda x: x.strip() if isinstance(x, str) else x)

        return data

    def uprav_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        upravime stlpce, tak aby sme mohli upravit data rovnako ako klasicke data a urobime tak
        :param data:
        :return:
        """
        #upravime nazvy stlpcov
        data.rename(columns = {"DruhSperku": "Ex_Komodita", "BarvaKovu": "Ex_BarvaKovu",
                               "KamenBril": "Ex_KBriliant", "KamenPrir": "Ex_KPrirod",
                               "BarvaPrirKam": "Ex_BarvaPrirKam", "BarvaCentrBril": "Ex_Barva",
                               "Kamenovost": "Ex_Kamenovost", "CenKat": "Ex_CenKat"}, inplace = True)
        #upravime data podla standardu
        data = self.zdroj_data_butiky.uprav_data_alo(data, typ = "distribucia")

        #pridam stlpec 9 znakov
        data["9_znakov"] = data["ID"].str.slice(0, 9).copy()
        return data

    def pridaj_info(self, typ: str, pravdepod: pd.Series,
                    pocty_na_but: pd.Series, final_rozdelenie: pd.Series, modely: list,
                    dodavatel: str, typ_sperku: str, na_rozdelenie: int = 100):
        """
        prideli info o priradeni poctu na butiky pre skupinu a pre jednotlive modely v skupinach
        zalezi na parametre 'typ'

        :param typ: ci pridelujem skupinove data alebo modelove
        :param pravdepod: pravdepodobnosti
        :param pocty_na_but: pocty bud modelu alebo skupiny nachadzajucich sa na butiku
        :param final_rozdelenie: pre skupinu je to rozdelenie skupiny a pre model rozdelenie modelu na butiky
        :param modely: pre skupinu to udava modely a pre 'model' to udava presny model pre lokalizaciu v dataframe
        :param dodavatel:
        :param typ_sperku:
        :param na_rozdelenie: kolko sperkov idem rozdelit z daneho modelu
        :return:
        """

        if typ == "skupina":
            #budeme chciet pridat tabulku pre kazdy model
            for model in modely:
                for butik in self.butiky:
                    indexy_priradenych_butikov = list(final_rozdelenie.index)
                    if butik in indexy_priradenych_butikov:
                        final = final_rozdelenie.loc[butik]

                    else:
                        final = 0
                    self.udaje_o_distribucii.loc[self.udaje_o_distribucii.shape[0]] = [dodavatel, typ_sperku, butik,
                                                                                       pravdepod.loc[butik],pocty_na_but.loc[butik],
                                                                                       final, model, 0, 0, 0, 0]

        elif typ == "model":
            search = ((self.udaje_o_distribucii["dodavatel"] == dodavatel) &
                      (self.udaje_o_distribucii["typ_sperku"] == typ_sperku) &
                      (self.udaje_o_distribucii["model"] == modely[0]))
            priradenie = self.udaje_o_distribucii.loc[search].copy()

            for index, row in priradenie.iterrows():
                self.udaje_o_distribucii.loc[index,
                ["na_rozdel", "prav_model", "pocet_model_butik", "final_rozdelenie"]] = \
                    [na_rozdelenie, pravdepod.loc[row["butik"]], pocty_na_but.loc[row["butik"]],
                     final_rozdelenie.loc[row["butik"]]]

        else:
            raise Exception("povoleny typ je len 'skupina' alebo 'model'.")

    def distribution(self):
        """

        :return:
        """

        #rozdelim skupiny sperkov (dodavatel - typ) na butiky (z tohoto vytvorim dalsi kontrolny subor a potom pridam vysledne rozdelenie podla finalneho rozdelenia)
        zoskupene_data_distribucia = self.data_distribucia.groupby(by=["Ex_Komodita", "Dodavatel"])
        for kat, data_kat in zoskupene_data_distribucia:
            butiky_s_poctami, modely = self.rozdel_skupinu_na_butiky(kategoria= kat,
                                                                     data_kat= data_kat)
            # vypocitam pravdepodobnosti jednotlivych modelov a butikov
            # usporiadam modely podla suctovej pravdepodobnosti
            zoradene_modely, pravdepodobnosti_dict = self.zorad_modely(modely = modely,
                                                                       dodavatel= self.id_dodavatelov[kat[1]])
            #pravdepodobnosti zatial nebudeme potrebovat ale mozno sa bude nieco menit

            for model in zoradene_modely:

                data_na_pridelenie_model = data_kat.loc[data_kat["ID"].str.slice(0,9) == model].copy()
                pocet_kusov_modelu_na_rozdelenie = data_kat.loc[data_kat["ID"].str.slice(0,9) == model].copy().shape[0]

                modely_na_butiky, butiky_s_poctami, pocty_modelu_na_butikoch = self.rozdel_modely_na_butiky(model= model,
                                                                  butikove_obmedzenia= butiky_s_poctami,
                                                                  pravdepod_butikov= pravdepodobnosti_dict[model],
                                                                  pocet_na_rozdelenie= pocet_kusov_modelu_na_rozdelenie)

                #pridelim informacie o prideleni modelu na butiky
                self.pridaj_info(typ= "model",
                                 pravdepod= pravdepodobnosti_dict[model],
                                 pocty_na_but= pocty_modelu_na_butikoch,
                                 final_rozdelenie= modely_na_butiky,
                                 modely= [model],
                                 dodavatel= self.id_dodavatelov[kat[1]],
                                 typ_sperku= kat[0],
                                 na_rozdelenie= pocet_kusov_modelu_na_rozdelenie)

                #pridelim konkretne sperky
                pravdepodobnosti_model = pravdepodobnosti_dict[model]
                # spravim usporiadany zoznam butikov aby som vedel naskladnovat podla pravdepodobnosti
                pravdepodobnosti_model.sort_values(inplace=True, ascending=False)
                zoradene_butiky = list(pravdepodobnosti_model.index)

                self.pridel_konkretne_sperky(model= model,
                                             zoradene_butiky=zoradene_butiky,
                                             butiky_s_poctami=modely_na_butiky,
                                             data_na_rozdelenie= data_na_pridelenie_model)
                # udaje z tohoto kroku su v self.data_info  (toto sa ubdatuje pre kazdu skupinu modelu)

                # zapisem udaje o prideleni konkretnych sperkov
                self.udaje_o_prideleni = pd.concat([self.udaje_o_prideleni, self.data_info], ignore_index=True)

                # priradim do povodneho suboru
                for index, riadok in self.data_info.iterrows():
                    povodny_index = riadok["index_celkovy"]
                    self.povodne_data_distribucia.loc[povodny_index, "Butik"] = self.but_sklad[
                        riadok["prideleny_butik"]]


        #pridame do finalneho pridelenia informaciu o type sperku
        self.udaje_o_prideleni["typ_sperku"] = None
        print(list(self.povodne_data_distribucia.columns))
        for index, row in self.udaje_o_prideleni.iterrows():
            self.udaje_o_prideleni.loc[index, "typ_sperku"] = list(self.povodne_data_distribucia.loc[self.povodne_data_distribucia["ID"] == row["ID"], "DruhSperku"])[0]

    def rozdel_skupinu_na_butiky(self, kategoria: tuple, data_kat: pd.DataFrame) -> tuple:
        """
        dostanem na vstupe specifikacie skupiny a data skupiny na rozdelenie. Ku kazdemu butiku pridelim
        pocty kolko na neho chcem naskladnit zo skupiny. Pridelujem podla pravdepodobnosti predaja a prihliadam na pocet
        sperkov z danej skupiny na butikoch. Priradim info o rozdeleni do suboru.
        :param kategoria: (typ_sperku, dodavatel)
        :param data_kat: data na rozdelenie z tejto kategorie
        :return: pocty kusov na butiky zo skupiny
        """

        butiky_s_pravdepodobnostami = self.butiky_pravdepodobnosti(info=list(kategoria),
                                                                   typ="skupina")
        butiky_s_pravdepodobnostami = self.uprav_pravdepodobnosti(butiky_s_pravdepodobnostami,
                                                                  dodavatel=self.id_dodavatelov[kategoria[1]])

        butiky_znormovave_prav = butiky_s_pravdepodobnostami * (1 / sum(butiky_s_pravdepodobnostami))

        ID_zo_skupiny_na_butikoch = self.zisti_pocty_na_butikoch(info = list(kategoria),
                                                                 typ= "skupina")

        rozdelena_skupina = self.pridel_pocty_na_vyrobu(data_rozdelenie = data_kat,
                                                        znormovane_prav = butiky_znormovave_prav,
                                                        modely_na_butikoch = ID_zo_skupiny_na_butikoch)

        modely_v_skupine = list(data_kat["ID"].str.slice(0,9).unique())

        self.pridaj_info(typ = "skupina",
                         pravdepod= butiky_s_pravdepodobnostami,
                         pocty_na_but= ID_zo_skupiny_na_butikoch,
                         final_rozdelenie= rozdelena_skupina,
                         modely= modely_v_skupine,
                         dodavatel= self.id_dodavatelov[kategoria[1]],
                         typ_sperku= kategoria[0])

        return rozdelena_skupina, modely_v_skupine

    def zorad_modely(self, modely: list, dodavatel: str) -> tuple:
        """
        zoradi vlozene modely podla suctovej pravdepodobnosti cez vsetky butiky

        :param modely: modely, ktore chem zoradit
        :param dodavatel:
        :return: usporiadane modely, slovnik s pd.Series obsahujucimi pravdepodobnosti modelv, kluce su cisla modelov
        """
        modely_sum = pd.Series([0]* len(modely), index=modely)
        modely_prav = {}
        for model in modely:
            model_pravdepodobnosti = self.butiky_pravdepodobnosti(info= [model],
                                                                  typ= "model")
            model_pravdepodobnosti = self.uprav_pravdepodobnosti(butiky_s_pravdepodobnostami= model_pravdepodobnosti,
                                                                 dodavatel= dodavatel)
            modely_prav[model] = model_pravdepodobnosti

            modely_sum.loc[model] = sum(model_pravdepodobnosti)

        #zoradime podla suctovej pravdepodobnosti
        modely_sum.sort_values(ascending=False, inplace=True)
        poradie_modelov = list(modely_sum.index)

        return poradie_modelov, modely_prav

    def rozdel_modely_na_butiky(self, model: list, butikove_obmedzenia: pd.Series,
                                pravdepod_butikov: pd.Series, pocet_na_rozdelenie: int) -> pd.Series:
        """
        rozdeli pozadovany pocet sperkov na butiky. bude priradovat v poradi urcenom pravdepodobnostami predaja
        na butiky s najmenej sperkami z daneho modelu. bude obmedzovana butikovymi obmedzeniami

        :param model: cislo modelu
        :param butikove_obmedzenia: dotacie kolko mozem dat dokopy zo vsetkych modelov patracich danej skupine na butiky
        :param pravdepod_butikov: pravdepodobnosti predaja modelu na danych butikoch
        :param pocet_na_rozdelenie:kolko mam pridelit z danoho modelu sperkov
        :return:
        """
        #budem chcet returnovat rozdelene pocty na butiky a upravene limity

        #zistim pocty modelu na butikoch
        butiky_s_poctami = self.zisti_pocty_na_butikoch(info= [model],
                                                        typ = "model")

        #zoradime butiky pre model podla uspesnosti

        model_pravdepod = pravdepod_butikov.loc[pravdepod_butikov != 0].copy()
        model_pravdepod.sort_values(ascending= False, inplace = True)
        zoradene_butiky = list(model_pravdepod.index)

        #vytvorim pd.Series na priradovanie
        priradene_na_butiky = pd.Series([0]*len(self.butiky), index= self.butiky)

        # priradim na butiky pocty v poradi zoradenia
        najmensi_pocet = 0

        while najmensi_pocet < 30:

            #ukoncim priradovanie, ked priradim kolko som chcel priradit

            if sum(priradene_na_butiky) == pocet_na_rozdelenie:
                return priradene_na_butiky, butikove_obmedzenia, butiky_s_poctami

            # najdem butiky s najmesim poctom sperkov z daneho modelu
            modely_na_butikoch = butiky_s_poctami + priradene_na_butiky
            modely_na_butikoch = modely_na_butikoch.loc[modely_na_butikoch == najmensi_pocet]
            butiky_s_najmenej_modelmi = list(modely_na_butikoch.index)

            for butik in zoradene_butiky:


                if (butik in butiky_s_najmenej_modelmi):
                    if butik in list(butikove_obmedzenia.index):
                        if butikove_obmedzenia.loc[butik] > 0:
                            #pridelim sperk na butik a znizim povoleny pocet v butikovych limitoch
                            priradene_na_butiky.loc[butik] += 1
                            butikove_obmedzenia.loc[butik] -= 1
                            break

            else:
                najmensi_pocet +=1



        else:
            print("priradene na butiky")
            print(priradene_na_butiky)
            print("butikove obmedzenia")
            print(butikove_obmedzenia)
            print("butiky s poctami")
            print(butiky_s_poctami)
            print(pravdepod_butikov)
            print(model)
            raise Exception("Zevraj je pocet modelov na butiku vacsi ako 30")


    def uprav_pravdepodobnosti(self, butiky_s_pravdepodobnostami: pd.Series, dodavatel: str) -> pd.Series:
        """
        upravi pravdepodobnosti tak aby sme nenaskladnili na butik, kde sa nemoze predavat dany dodavatel
        :param model:
        :param butiky_s_pravdepodobnostami:
        :return:
        """

        #stanovim, ktore na ktore butiky nemozem posielat dodavatela
        if dodavatel == "Pomellato Spa": #ide len na cesko
            butiky_kam_nie = ["HALADA EUROVEA BRATISLAVA",
                                "HALADA AVION BRATISLAVA"]

        elif dodavatel == "K. Mikimoto & Co., LTD": #nejde na aviony
            butiky_kam_nie = ["HALADA AVION BRATISLAVA", "HALADA AVION OSTRAVA"]

        elif dodavatel == "Roberto Coin S.p.A.": #ide len na slovensko
            butiky_kam_nie = ["HALADA PRIKOPY", "HALADA PARIZSKA",
                              "HALADA BRNO", "HALADA AVION OSTRAVA"]
        else:
            butiky_kam_nie = []

        # nastavim pravdepodobnost na 0
        for butik in butiky_kam_nie:
            butiky_s_pravdepodobnostami.loc[butik] = 0
            # print(butik)
            # print(butiky_s_pravdepodobnostami)

        return butiky_s_pravdepodobnostami



    def pridel_pocty_na_vyrobu(self, data_rozdelenie: pd.DataFrame, znormovane_prav: pd.Series,
                               modely_na_butikoch: pd.Series) -> pd.Series:
        """
        zistim pre kazdy butik kolko na neho chceme naskladnit. rozdelim pocet podla vah a zaokruhlim.
        odpocitam od tohoto aktualny pocet daneho modelu na butikoch, nasledne sa pozrem ci pridelenym poctom
        nepresahujem sklady. ak presahujem, tak znizim v danom butiku aby som nepresahoval.
        Pozdrem sa ci sucet, co sa mi podelilo po upravach pridelit sedi s poctom co som chcel pridelit.
        Ak sedi vratim konkretne rozdelenie.
        Ak nesedi, tak rozdelim o jeden sperk viacej a pozrem sa ci sedi vysledny pocet co co rozdelil s tym kolko som chcel rozdelit
        :param data_rozdelenie:
        :param znormovane_prav:
        :param modely_na_butikoch:
        :return:
        """

        povodny_pocet_na_rozdelenie = data_rozdelenie.shape[0]

        rozdelovany_pocet = data_rozdelenie.shape[0]

        butiky_final_rozdelenie = pd.Series([0 for butik in self.butiky], index=self.butiky)

        while rozdelovany_pocet < 500:  # podmienka je len aby sme mali osetreny krajny pripad
            # rozdelim aktualny pocet na butiky podla vah
            butiky_s_poctami = znormovane_prav * rozdelovany_pocet

            # zaokruhlim na celociselne hodnoty
            butiky_s_poctami = self.zaokruhli(butiky_s_poctami, rozdelovany_pocet)

            # vyberiem butiky, na ktore som pridelil
            butiky_priradene = list(butiky_s_poctami.loc[butiky_s_poctami != 0].index)
            butiky_s_poctami = butiky_s_poctami.loc[butiky_s_poctami != 0]

            modely_na_priradenych_butikoch = modely_na_butikoch.loc[modely_na_butikoch.index.isin(butiky_priradene)]

            # odcitam sperky aktualne na butikoch v danom modeli
            butiky_final_rozdelenie = butiky_s_poctami - modely_na_priradenych_butikoch

            butiky_final_rozdelenie = butiky_final_rozdelenie.apply(lambda x: max(0, x))


            # pozriem sa ci som neprekrocil skladove limity (ak by som mal prekrocit limit, tak namiesto vypocitaneho cisla dam hodnotu limitu)
            for butik in butiky_priradene:
                butik_pocet = butiky_final_rozdelenie[butik]
                if butik_pocet > self.butiky_skladove_limity[butik]:
                    butiky_final_rozdelenie[butik] = self.butiky_skladove_limity[butik]

            if sum(butiky_final_rozdelenie) > povodny_pocet_na_rozdelenie:
                #mozno poupravit vyberanie

                najhorsi_butik = list(butiky_final_rozdelenie.index)[0]
                butiky_final_rozdelenie.loc[najhorsi_butik] -= 1

            if sum(butiky_final_rozdelenie) == povodny_pocet_na_rozdelenie:
                # znizim limity butikov, na ktore som priradil
                for butik in butiky_priradene:
                    self.butiky_skladove_limity[butik] -= butiky_final_rozdelenie[butik]
                break

            else:
                rozdelovany_pocet += 1

        if sum(butiky_final_rozdelenie) != povodny_pocet_na_rozdelenie:

            print("stala sa chyba")
            print(sum(butiky_final_rozdelenie))
            print(povodny_pocet_na_rozdelenie)
            print(data_rozdelenie)
            raise Exception

        return butiky_final_rozdelenie

    def pridel_konkretne_sperky(self, model: str, zoradene_butiky: list, butiky_s_poctami: pd.Series, data_na_rozdelenie: pd.DataFrame):
        """
        zoberie sperky, co ma priradit a priradi ich na butiky, v predom urcenych poctoch. Bude primarne priradovat na butiky,
        s najvacsou pravdepodobnostou pre dany model a bude sa snazit zaplnit kamene a farby zlata co nemam na butikoch
        :param model:
        :param zoradene_butiky:
        :param butiky_s_poctami:
        :param data_na_rozdelenie:
        :return:
        """
        self.data_info = self.sperky_info(data_na_rozdelenie)
        #print(self.data_info)
        #slovnik butikov, kde kazdy butik ma podslovnik pre farby zlata a farby kamenov na danom butiku
        self.co_je_na_butikoch = self.zisti_co_je_na_butikoch(model, zoradene_butiky)

        while self.data_info.loc[self.data_info["prideleny_butik"].isna()].copy().shape[0] > 0: #teda dokedy mam co rozdelovat
        #for i in range(self.data_info.shape[0]):
            sperky_na_priradenie = self.data_info.loc[self.data_info["prideleny_butik"].isna()].copy()
            #print(f"sperky na pridelenie {self.data_info.loc[self.data_info['prideleny_butik'].isna()].copy().shape[0]}")

            priradil_som = self.najdi_konkretnu_kategoriu(model = model, sperky_na_priradenie = sperky_na_priradenie,
                                                          zoradene_butiky = zoradene_butiky, butiky_s_poctami = butiky_s_poctami)

            if not priradil_som:
                #teda som nepriradil sperk a mozem priradit na najlepsi butik sperk aky chcem podla pravidiel
                #ak som sa dostal sem, tak mam na rozdelenie len sperky, ktorych farba kamena a zlata sa nachadza na vsetkych butikoch kam chcem rozdelovat
                butik_najlepsi = ""
                for butik in zoradene_butiky:
                    if butiky_s_poctami.loc[butik] > 0:
                        butik_najlepsi = butik
                        break

                self.najdi_a_prirad_sperk(sperky_na_priradenie, butik_najlepsi, model,"nic")

        #spravim post manipulaciu ID, takze ak by som mal dat rovnake 2 rovnake ID na jeden butik, tak premiestnim na najlepsie butik
        self.finalna_manipulacia_ID(zoradene_butiky)

    def finalna_manipulacia_ID(self, zoradene_butiky: list):
        """
        pozrem sa ci som v danom ID nenaskladnil na jeden butik viacej rovnakych ID. Ak hej, tak zoberiem
        prebytocne ID a naskladnim na butiky v poradi urcenom predajnostou a budem naskladnovat na tie co maju najmenej rovnakych ID
        :param zoradene_butiky:
        :return:
        """

        #pridam aby som sa vedel pozret kam som chcel priradit najprv
        self.data_info["butik_pred_manipulaciou"] = self.data_info["prideleny_butik"]
        self.data_info["manipulacia"] = False  # tu budem znacit ci som zmenil butik

        #rozdelim po IDckovych skupinach
        data_po_ID = self.data_info.groupby("ID")
        for ID, data_ID in data_po_ID:


            #pridame nazov dodavatela
            dodavatel = self.id_dodavatelov[list(self.data_distribucia.loc[self.data_distribucia["ID"] == ID, "Dodavatel"])[0]]

            zoradene_butiky_pre_dodavatela = self.butiky_pre_dodavatela(dodavatel, zoradene_butiky)

            ID_rozdelene_na_butiky = pd.Series([data_ID.loc[(data_ID["ID"] == ID) &
                                                            (data_ID["prideleny_butik"] == butik)].shape[0] for butik in
                                                zoradene_butiky_pre_dodavatela],
                                               index=zoradene_butiky_pre_dodavatela)

            if ID == "PESOMOBL7-7,5BU":
                print("rozdelene na butiky")
                print(ID_rozdelene_na_butiky)

            for butik in zoradene_butiky_pre_dodavatela:
                if (n := ID_rozdelene_na_butiky.loc[butik]) > 1: #ak som na butik priradil viacej rovnakych ID ako jedno, tak musim premenit
                    pridelene_data_indexy = list(self.data_info.loc[(self.data_info["ID"] == ID) &
                                                                    (self.data_info["prideleny_butik"] == butik)].index) #aby som vedel kde su dane priradenia
                    na_rozdelenie = n - 1

                    # pridam aj pocty konkretneho ID uz naskladnene na butikoch
                    ID_na_butikoch = pd.Series([self.na_butikoch.loc[(self.na_butikoch["zkr"] == ID) &
                                                                     (self.na_butikoch["butik"] == butik)].shape[0] for butik in
                                                zoradene_butiky_pre_dodavatela],
                                               index=zoradene_butiky_pre_dodavatela)

                    # idem prerozdelit pocet naskladnenych rovnakych ID - 1 (takze upravim pocty najprv)
                    ID_rozdelene_na_butiky.loc[butik] = 1
                    #tam kde mam najmenej a zaroven je to najlepsi butik, tak pridelim
                    najmensi_pocet = 0
                    pocty_dokopy = ID_rozdelene_na_butiky + ID_na_butikoch

                    if ID == "PESOMOBL7-7,5BU":
                        print("vnutro")
                        print(pocty_dokopy)
                        print(f"zoradene butiky su {zoradene_butiky_pre_dodavatela}")

                    while na_rozdelenie > 0:
                        for butik_naj in zoradene_butiky_pre_dodavatela:
                            #najlepsi butik s najmensim poctom rovnakych ID
                            if pocty_dokopy.loc[butik_naj] == najmensi_pocet:
                                #priradim na dany butik
                                ID_rozdelene_na_butiky.loc[butik_naj] += 1
                                #musim pridat aj sem lebo z tymto pracujem ale dalsie butiky to neovplyvni ,pretoze sa to potom resetuje
                                pocty_dokopy.loc[butik_naj] += 1
                                self.data_info.loc[pridelene_data_indexy[0], ["prideleny_butik", "manipulacia"]] = [butik_naj, True]
                                #odstranim sperk z premiestnovania, ktory som uz premiestnil
                                pridelene_data_indexy = pridelene_data_indexy[1:]
                                na_rozdelenie -= 1
                                break

                        else:
                            najmensi_pocet += 1

    def butiky_pre_dodavatela(self, dodavatel: str, zoradene_butiky: list) -> list:
        """
        zo zoznamu so zoradenymi butikmi odstrani butiky kam nemozem umiestnit daneho dodavatela
        :param dodavatel:
        :param zoradene_butiky:
        :return: zoradeny zoznam len s butikmi kam mozem naskladnit dodavatela
        """

        # stanovim, ktore na ktore butiky nemozem posielat dodavatela
        if dodavatel == "Pomellato Spa":  # ide len na cesko
            butiky_kam_nie = ["HALADA EUROVEA BRATISLAVA",
                              "HALADA AVION BRATISLAVA"]

        elif dodavatel == "K. Mikimoto & Co., LTD":  # nejde na aviony
            butiky_kam_nie = ["HALADA AVION BRATISLAVA", "HALADA AVION OSTRAVA"]

        elif dodavatel == "Roberto Coin S.p.A.":  # ide len na slovensko
            butiky_kam_nie = ["HALADA PRIKOPY", "HALADA PARIZSKA",
                              "HALADA BRNO", "HALADA AVION OSTRAVA"]
        else:
            butiky_kam_nie = []

        for butik in butiky_kam_nie:
            if butik in zoradene_butiky:
                zoradene_butiky.remove(butik)

        return zoradene_butiky

    def najdi_konkretnu_kategoriu(self, model: str, sperky_na_priradenie: pd.DataFrame, zoradene_butiky: list, butiky_s_poctami: pd.Series) -> bool:
        """
        skusi najst najlepsi butik podla pravdepodobnosti, ktoremu bude chybat but nejaky sperk s kamenom, co mozem
        priradit. Ak mam vsetky kamene (co mozem priradit) na vsetkych butikoch, tak to iste skusim pre farbu zlata.
        ak mam na vsetkych butikoch vsetky farby zlata a kamena (co by som mohol priradit) tak vratim False
        :param model:
        :param sperky_na_priradenie:
        :param zoradene_butiky:
        :param butiky_s_poctami:
        :return:
        """
        for kategoria in ["kamen", "zlato"]:

            # budem pridelovat najprv na najlepsie butiky
            for butik in zoradene_butiky:
                if butik in list(butiky_s_poctami.index):  # teda ak mu chcem nieco este priradit a mam butik v zozname
                    if butiky_s_poctami.loc[butik] > 0:
                        mam_na_butiku = self.co_je_na_butikoch[butik][kategoria]
                        mam_na_rozdelenie = list(sperky_na_priradenie[kategoria].unique())

                        # pozrem sa ci mam nejaky typ co sa nenachadza na butiku
                        for typ in mam_na_rozdelenie:
                            if typ not in mam_na_butiku:
                                if kategoria == "kamen":
                                    #priradim sperk a vratim True, ze som priradil
                                    self.najdi_a_prirad_sperk(sperky_na_priradenie, butik, model, "kamen", typ,
                                                              mam_na_butiku)
                                    return True
                                else:  # zlato
                                    # priradim sperk a vratim True, ze som priradil
                                    self.najdi_a_prirad_sperk(sperky_na_priradenie, butik, model, "zlato", typ)
                                    return True
        else:
            #ked sa dostanem do tohoto elsu, tak to znamena, ze mi dobehly cykly a nepriradil som, takze vratim False
            return False

    def najdi_a_prirad_sperk(self, sperky_na_vyber: pd.DataFrame, butik: str, model: str, typ: str,
                             konkretny: str = "", veci_na_butiku: dict = {}):
        """
        priradim najlepsi sperk na vybrany butik
        ak mam typ nic, znamena, ze vsetky kategorie sperkov na rozdelenie uz mam na vsetkych butikoch, takze nemusim filtorvat a priradim
        ten sperk, ktoreho kamen sa predal na butiku ako posledny (ak taky mam) ak nie tak sa pozrem na predposledny predaj,...   Ak budem mat stale na vyber,
        tak zoradim sperky podla ceny a na aviony davam od najlacnejsich a na ostatne od najdrahsich
        ak mam typ zlato, tak mam na vsetkych butikoch kam chcem priradit uz vsetky kamene a vyselektujem konkretny typ zlata, ak este mam nejake na vyber, tak
        pokracujem systemom popisanym vyssie
        ak mam typ kamen, tak skusim zistit ci mi z vybranych sperkov na rozdelenie danej farby kamena chyba ne jake zlato na butiku, ak ano tak ho vyberem a
        pokracujem v rozdeleni systemom popisanym vyssie.
        ked priradim sperk pripisem priradenie na potrebne miesta. (je to popisane vo funkcii "self.prirad_sperk_na_butik")

        :param sperky_na_vyber:
        :param butik:
        :param model:
        :param typ:
        :param konkretny:
        :param veci_na_butiku:
        :return:
        """

        if typ != "nic":
            sperky_na_vyber = sperky_na_vyber.loc[sperky_na_vyber[typ] == konkretny].copy()

        else:
            sperky_na_vyber = sperky_na_vyber.copy()

        # pozrem sa ci mam nejaku este vacsiu specifikaciu pomocou zlata
        if typ == "kamen":
            #mam_na_butiku = veci_na_butiku[butik]["zlato"]
            na_rozdelenie = list(sperky_na_vyber["zlato"].unique())
            for zlato in na_rozdelenie:
                if zlato not in veci_na_butiku:
                    sperky_na_vyber = sperky_na_vyber.loc[sperky_na_vyber["zlato"] == zlato].copy()
                    break #teda vyberiem len jedno

        #mam vybraty subor sperkov

        print(f"mam sperkov na vyber {sperky_na_vyber.shape[0]}")
        if sperky_na_vyber.shape[0] == 1: #ak som odstranil dostatok sperkov
            #priradim sperku butik
            index = list(sperky_na_vyber["index_celkovy"])[0]
            self.prirad_sperk_na_butik(index, butik, sperky_na_vyber)

        #mam viacej sperkov v zozname
        else:
            # pozrem sa na posledny sperk z daneho modelu, co sa predal a vyberem podla jeho kamena

            sperky_na_vyber = self.vyber_podla_kamena(sperky_na_vyber, model, butik)

            if sperky_na_vyber.shape[0] == 1:  # ak som odstranil dostatok sperkov
                # priradim sperku butik
                index = list(sperky_na_vyber["index_celkovy"])[0]
                self.prirad_sperk_na_butik(index, butik, sperky_na_vyber)

            #ak mam stale vyber z viacerych alebo sa dany kamen na butiku nepredal, tak dam na aviony ten najlacnejsi z vyberu
            #a na ostatne ten najdrahsi
            else:
                poradie_cien = ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9"] #pre drahe obratim poradie
                if butik in self.butiky_slabe:
                    sperky_na_vyber["zoradene"] = pd.Categorical(sperky_na_vyber["cenkat"].copy(), categories = poradie_cien, ordered = True)
                    sperky_na_vyber = sperky_na_vyber.sort_values('zoradene').drop(columns='zoradene')
                    #priradim najlacnejsi sperk
                    index = list(sperky_na_vyber["index_celkovy"])[0]
                    self.prirad_sperk_na_butik(index, butik, sperky_na_vyber)

                else: #zoradim od najdrahsieho
                    sperky_na_vyber["zoradene"] = pd.Categorical(sperky_na_vyber["cenkat"].copy(),
                                                                 categories= reversed(poradie_cien), ordered=True)
                    sperky_na_vyber = sperky_na_vyber.sort_values('zoradene').drop(columns='zoradene')
                    # priradim najlacnejsi sperk
                    index = list(sperky_na_vyber["index_celkovy"])[0]
                    self.prirad_sperk_na_butik(index, butik, sperky_na_vyber)

    def vyber_podla_kamena(self, sperky_na_vyber: pd.DataFrame, model: str, butik: str) -> pd.DataFrame:
        """
        pozriem sa na sperky, co sa predali y daneho modelu na danom butiku za poslednych 5 rokov
        a pozeram sa na kamene, co sa predali ako posledne. Pozeram sa ci mam v datach na rozdelovanie
        kamen, co sa predal ako posledny ak nie, tak sa pozrem na predposledne predany atd.
        :param sperky_na_vyber:
        :param model:
        :param butik:
        :return:
        """

        #za poslendych 5 rokov
        data_model_butik_predane = self.data_halada.loc[(self.data_halada["butik"] == butik) &
                                                        (self.data_halada["zkr"].str.slice(0,9) == model) &
                                                        ((self.dnes - self.data_halada["datum_prodej"]).dt.days <= 5 * 365)].copy()
        if data_model_butik_predane.shape[0] > 0:
            #zoradim podla predaja
            data_model_butik_predane.sort_values(by = "datum_prodej", ascending = False, inplace = True)

            #skusim ci nejaky z predanych kamenov mam v zozname ak hej tak vyberem tie sperky
            for index, riadok in data_model_butik_predane.iterrows():
                kamen = riadok["Ex_Barva"]
                sperky_s_kamenom = sperky_na_vyber.loc[sperky_na_vyber["kamen"] == kamen].copy()
                if sperky_s_kamenom.shape[0] > 0:
                    return sperky_s_kamenom
            else:
                return sperky_na_vyber

        else:
            return sperky_na_vyber

    def prirad_sperk_na_butik(self, index, butik: str, sperk_info: pd.DataFrame):
        """
        priradi sperk na vybrany butik, oznaci naskladnenie na sklad butiku do celkoveho distribucneho suboru,
        do dataframu so sperkami konkretneho modelu tiez oznaci nazov butiku aby som vedel ze je uz sperk prideleny,
        a aby som vedel urobit post manipulaciu ID.
        Do suboru veci co je na danom butiku priradi farbu zlata a kamena ak sa v nom este nenachadzaju
        :param index:
        :param butik:
        :param sperk_info:
        :return:
        """
        #sem priradime az po vyslednej manipulacii
        #self.data_distribucia.loc[index, "Butik"] = self.but_sklad[butik]

        # oznacim sperk v rozdelovani
        self.data_info.loc[list(sperk_info.index)[0], "prideleny_butik"] = butik

        # priradim butiku kategorie priradeneho sperku
        zlato = list(sperk_info["zlato"])[0]
        kamen = list(sperk_info["kamen"])[0]
        if zlato not in self.co_je_na_butikoch[butik]["zlato"]:
            self.co_je_na_butikoch[butik]["zlato"].append(zlato)

        if kamen not in self.co_je_na_butikoch[butik]["kamen"]:
            self.co_je_na_butikoch[butik]["kamen"].append(kamen)


    def zisti_co_je_na_butikoch(self, model: str, butiky: list) -> dict:
        """
        spravi slovnik s butikmi, kde pre kazdy butik budem vediet ake farkby zlata a farby kamenov sa na nom nachadzaju z
        daneho modelu
        :param model:
        :param butiky:
        :return:
        """
        butiky_s_vlastnostami = {}
        for butik in butiky:
            butiky_s_vlastnostami[butik] = {}
            podoba_9_na_butiku = self.na_butikoch.loc[(self.na_butikoch["butik"] == butik) &
                                                      (self.na_butikoch["zkr"].str.slice(0, 9) == model)].copy()
            zlato_na_butiku = list(podoba_9_na_butiku["Ex_BarvaKovu"].unique())
            butiky_s_vlastnostami[butik]["zlato"] = zlato_na_butiku

            kamene_na_butiku = list(podoba_9_na_butiku["Ex_Barva"].unique())
            butiky_s_vlastnostami[butik]["kamen"] = kamene_na_butiku

        return butiky_s_vlastnostami

    def sperky_info(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        zoskupi potrebne udaje ku sperkom
        :param data:
        :return:
        """
        data_info = pd.DataFrame(columns = ["index_celkovy", "ID", "model", "cenkat", "kamen", 'zlato', "prideleny_butik", "dodavatel"])
        for index, riadok in data.iterrows():
            data_info.loc[data_info.shape[0]] = [index, riadok["ID"], riadok["9_znakov"], riadok["Ex_CenKat"],
                                                 riadok["Ex_Barva"], riadok["Ex_BarvaKovu"], None,
                                                 self.id_dodavatelov[riadok["Dodavatel"]]]

        return data_info

    def butiky_pravdepodobnosti(self, info: list, typ: str) -> pd.Series:
        """
        vytvori pravdepodobnosti predaja do 3 rokov pre butiky (z dat naskladneni za poslednych 5 rokov)
        bud pre skupinu kategorii alebo model,
        nevytvori ich pre butiky, kde sa model nenaskladnil za poslednych 5 rokov

        :param info:
        :param typ: moze byt "model" alebo "skupina"
        :return: pd.Series s butikmi a pravdepodobnostami
        """

        #vyberem naskladnene sperky za poslednych 5 rokov
        self.za_5_rokov = self.data_halada.loc[(self.dnes - self.data_halada["datum_naskladneni"]).dt.days <= 365 * 5].copy()

        butiky_prav = pd.Series([float(0)]*len(self.butiky), index = self.butiky)
        #vytvorim konkretne pravdepodobnosti ze sa model preda na danom butiku do 3 rokov (data naskladneni za poslednych 5 rokov)
        for butik in self.butiky:

            if typ == "model":
                data_butik = self.za_5_rokov.loc[(self.za_5_rokov["butik"] == butik) &
                                                   (self.za_5_rokov["zkr"].str.slice(0,9) == info[0])].copy()


            elif typ == "skupina":
                data_butik = self.za_5_rokov.loc[(self.za_5_rokov["Ex_Komodita"] == info[0]) &
                                                 (self.za_5_rokov["dodavatel_jmeno"] == self.id_dodavatelov[info[1]]) &
                                                 (self.za_5_rokov["butik"] == butik)].copy()
            else:
                raise Exception("Povoleny typ je len skupina alebo model")

            data_info = self.separacia_na_predajne_skupiny(data_butik)
            if data_info[0] > 0: # ked je 0, tak na butik sa este model nenaskladnil, takze nechceme naskladnovat

                if (data_info[1] + data_info[2] + data_info[4]) > 0:
                    pravdepod = data_info[1] / (data_info[1] + data_info[2] + data_info[4])
                else: #moze byt rovne nule, ked tam je len jeden sprek a ten sa vratil v rovnaky den ako sa naskladnil
                    pravdepod = 0

                if pravdepod == 0:
                    pravdepod = 0.05

                butiky_prav.loc[butik] = pravdepod
            else:
                butiky_prav.loc[butik] = 0.1

            if typ == "skupina":
                butiky_prav.loc[butik] = data_info[1]

        return butiky_prav


    def separacia_na_predajne_skupiny(self, data):
        """
        Zoberie data, ktore mu dame
        rozdeli ich na kategorie:

        - alfa =  pocet naskladnenych
        - beta = predane do 3 rokov
        - gama = nepredane do 3 roky a predavaju sa 3 roky   (cast nepredanych, predali sa za viac ako 3 roky a sperky vratene za viac ako 3 roky)
        - delta = nepredane a este sa nepredavaju 3 roky (asi skoro vsetky preskladnenia a z nepredanych)
        - nepredajny_index = udaje z delta (cas delta na butiku)/ (365 *3)

        vrati - [alfa,beta,gama,delta,nepredajny_index]

        return: list
        """

        nepredane = data.loc[data['datum_vraceni'].isna()].copy()
        ostatne = data.loc[data['datum_vraceni'].notna()].copy()

        alfa = len(data)  # pocet naskladnenych
        beta = 0  # predane do 3 rokov
        gama = 0  # nepredane do 3 roky a predavaju sa 3 roky   (cast nepredanych, predali sa za viac ako 3)
        delta = 0  # nepredane a este sa nepredavaju 3 roky (asi skoro vsetky preskladnenia a z nepredanych)
        nepredajny_index = 0

        for index, riadok in nepredane.iterrows():

            if (self.dnes - riadok['datum_naskladneni']).days > 365 * 3:  # nepredali sa a uz su tam 3 a viac rokov
                gama += 1
            else:  # nepredavaju sa 3 a viac rokov a neboli predane
                delta += 1

                nepredajny_index += (self.dnes - riadok['datum_naskladneni']).days / (365 * 3)

        for index, riadok in ostatne.iterrows():

            if riadok['datum_vraceni'] == pd.to_datetime("1900-01-01"):  # predane
                if (riadok['datum_prodej'] - riadok['datum_naskladneni']).days < 365 * 3:  # predane do 3 rokov
                    beta += 1
                else:  # predane za viac ako 3 roky
                    gama += 1

            else:  # boli preskladnene

                if (riadok['datum_vraceni'] - riadok[
                    'datum_naskladneni']).days > 365 * 3:  # boli preskladnene po 3 a viac rokov,takze sa nepredali do 3 rokov
                    gama += 1
                else:  # boli preskladnene po menej ako 3 rokoch takze este zapocitavam pravdepodobnost ze by sa mohli predat
                    delta += 1

                    nepredajny_index += (riadok['datum_vraceni'] - riadok['datum_naskladneni']).days / (365 * 3)

        lala = [alfa, beta, gama, delta, nepredajny_index]

        return lala


        #kazdemu butiku pripocitam pravdepod. 0.1 a zastropujem na 1

    def zisti_pocty_na_butikoch(self, info: list, typ: str) -> pd.Series:
        """
        priradi kazdemu halada butiku pocet sperkov ak je typ: "model", tak pocet z daneho modelu, ak je typ: "skupina",
        tak pocet sperkov na butikoch z danej skupiny
        :param info: informacia pre filtraciu
        :param typ: "model" ak chcem pocty pre model "skupina" ak chcem pocty pre skupinu
        :return: butiky s pocetami v pd.Series
        """
        pocty_butiky = pd.Series([0 for lala in self.butiky], index=self.butiky)

        if typ == "skupina":
            for butik in self.butiky:
                skupina_na_butiku = self.na_butikoch.loc[(self.na_butikoch["Ex_Komodita"] == info[0]) &
                                                         (self.na_butikoch["dodavatel_jmeno"] == self.id_dodavatelov[info[1]]) &
                                                         (self.na_butikoch["butik"] == butik)].copy()

                pocty_butiky.loc[butik] += skupina_na_butiku.shape[0]

        elif typ == "model":
            for butik in self.butiky:
                # priradim pocty
                model_na_butiku = self.na_butikoch.loc[(self.na_butikoch["butik"] == butik) &
                                                       (self.na_butikoch["zkr"].str.slice(0, 9) == info[0])].copy()

                pocty_butiky.loc[butik] += model_na_butiku.shape[0]
        else:
            raise Exception("Zatial viem zistit pocty iba pre model a skupinu")

        return pocty_butiky

    @staticmethod
    def zaokruhli(pocty: pd.Series, vyrobit_dokopy) -> pd.Series:
        """
        zoberie pocty na rozdelenie (float) a zaokruhli ich pomocou klasickej python funkcie a potom dorozdeli zbytok
        sperkov:
        - ak ubralo (celkovo) -> prida tam kde najviac ubralo (konkretne zlozky)
        - ak pridalo (celkovo) -> uberie tam kde najviac pridalo(konkretne zlozky)

        :param pocty: pd.Series s butikmi a poctami, co na ne chcem priradit
        :param vyrobit_dokopy: int
        :return: zaokruhlene pocty na cele cisla pd.Series
        """

        pocty_po_prvom_kroku_zaokruhlenia = pocty.apply(round)

        rozdiely_po_zaokruhleni = pocty - pocty_po_prvom_kroku_zaokruhlenia

        pocet_po_zaokruhleni = pocty_po_prvom_kroku_zaokruhlenia.sum()

        if pocet_po_zaokruhleni < vyrobit_dokopy:
            kolko_dorozdelit = vyrobit_dokopy - pocet_po_zaokruhleni
            roztriedene_rozdely_po_zaokruhleni = rozdiely_po_zaokruhleni.copy().sort_values(ascending=False)

            for i in list(roztriedene_rozdely_po_zaokruhleni.index):
                if kolko_dorozdelit == 0:
                    break
                pocty_po_prvom_kroku_zaokruhlenia[i] += 1
                kolko_dorozdelit -= 1

            if kolko_dorozdelit != 0:
                print(kolko_dorozdelit)
                print(pocty_po_prvom_kroku_zaokruhlenia)

        elif pocet_po_zaokruhleni > vyrobit_dokopy:
            kolko_ubrat = pocet_po_zaokruhleni - vyrobit_dokopy
            roztriedene_rozdely_po_zaokruhleni = rozdiely_po_zaokruhleni.copy().sort_values(ascending=True)
            for i in list(roztriedene_rozdely_po_zaokruhleni.index):
                if kolko_ubrat == 0:
                    break
                pocty_po_prvom_kroku_zaokruhlenia[i] += -1
                kolko_ubrat -= 1

            if kolko_ubrat != 0:
                print("treba ubrat este" + " " + str(kolko_ubrat))

        return pocty_po_prvom_kroku_zaokruhlenia


if __name__ == "__main__":

    time.sleep(30)

    dist = Distribucia_brand_HALADA()

    #dist.distribuj()
    dist.distribution()

    vystupne_rozdelenie = dist.povodne_data_distribucia

    info_rozdelenie = dist.udaje_o_distribucii
    info_konkretne_pridelenie = dist.udaje_o_prideleni

    print(info_rozdelenie)
    print(info_konkretne_pridelenie)
    print(vystupne_rozdelenie)

    #info o distribucii
    info_rozdelenie.to_excel(r"\\10.10.10.3\data\99_AI\Inputy\data_nacitavanie\HALADA_distribucia_info_1.xlsx", index = False)
    info_konkretne_pridelenie.to_excel(r"\\10.10.10.3\data\99_AI\Inputy\data_nacitavanie\HALADA_distribucia_info_2.xlsx", index = False)
    vystupne_rozdelenie.to_excel(r"\\10.10.10.3\data\99_AI\Inputy\data_nacitavanie\HALADA_distribucia.xlsx", index = False)

    #zapis do K2 IN
    vystupne_rozdelenie.to_csv(r"\\10.10.10.3\data\99_AI\K2 IN\DistribuceOUTHalada.csv",
                                         index=False, sep="\t", quoting = csv.QUOTE_NONNUMERIC)
