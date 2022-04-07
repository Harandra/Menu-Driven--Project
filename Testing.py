import unittest

from Sports.Bill import bill
from Sports.Sportsthings import table


class MyTestCase(unittest.TestCase):
    def test_something(self):
        global s1, s2, s3, s4
        op = table()
        print("Welcome to Sports World center")
        for j in range(0, 5):
            print("CHOICE\n1.Cricket product\n2.Football Products\n3.Badminton products\n4.Indoor Games "
                  "products\n5.Bill\n6.Exit\n\033[34m\33[1mNOTE:IF YOU CLICK ANY NUMBER OTHER THAN 1-6 THE SHOP "
                  "EXITS")
            a = int(input("Enter your choice\n"))
            if a == 1:
                lst1 = []
                a1 = op.cricketproducts()
                print(a1)
                s1, s2, s3, s4 = 0, 0, 0, 0
                self.assertTrue(a1, "Cricket")
                for i in range(0, 6):
                    x = 1
                    if x == 1:
                        opp = bill()
                        f1 = 2
                        x1 = opp.cricket_bat(f1)
                        self.assertTrue(x1, 1200)
                        lst1.append(x1)
                    elif x == 2:
                        opp = bill()
                        f2 = 2
                        x2 = opp.cricket_ball(f2)
                        self.assertTrue(x2, 80)
                        lst1.append(x2)
                    elif x == 3:
                        opp = bill()
                        f3 = 2
                        x3 = opp.cricket_Gloves(f3)
                        self.assertTrue(x3, 500)
                        lst1.append(x3)
                    elif x == 4:
                        opp = bill()
                        f4 = 2
                        x4 = opp.cricket_helmet(f4)
                        self.assertTrue(x4, 600)
                        lst1.append(x4)
                    elif x == 5:
                        opp = bill()
                        f5 = 2
                        x5 = opp.cricket_Stumps(f5)
                        self.assertTrue(x5, 160)
                        lst1.append(x5)
                    elif x==6:
                        opp = table()
                        r = opp.thank2()
                        print(r)
                        break
                    else:
                        opp = table()
                        z = opp.thank()
                        print(z)
                        break
                s1 = sum(lst1)
            elif a == 2:
                lst2 = []
                a2 = op.Football()
                print(a2)
                self.assertTrue(a2, "Football")
                for i in range(0, 4):
                    x = 2
                    if x == 1:
                        opp = bill()
                        f1 = 2
                        x1 = opp.football_ball(f1)
                        self.assertTrue(x1, 1400)
                        lst2.append(x1)
                    elif x == 2:
                        opp = bill()
                        f2 = 2
                        x2 = opp.football_shoes(f2)
                        self.assertTrue(x2, 1000)
                        lst2.append(x2)
                    elif x == 3:
                        opp = bill()
                        f3 = 2
                        x3 = opp.football_gloves(f3)
                        self.assertTrue(x3, 800)
                        lst2.append(x3)
                    elif x==4:
                        opp = table()
                        r = opp.thank2()
                        print(r)
                        break
                    else:
                        opp = table()
                        z = opp.thank()
                        print(z)
                        break
                s2 = sum(lst2)
            elif a == 3:
                lst3 = []
                a3 = op.Badminton()
                print(a3)
                self.assertTrue(a3, "Badminton")
                for i in range(0, 5):
                    x = 3
                    if x == 1:
                        opp = bill()
                        f1 = 2
                        x1 = opp.racquets_bdmtn(f1)
                        self.assertTrue(x1, 1200)
                        lst3.append(x1)
                    elif x == 2:
                        opp = bill()
                        f2 = 2
                        x2 = opp.shuttlecocks_bdmtn(f2)
                        self.assertTrue(x2, 80)
                        lst3.append(x2)
                    elif x == 3:
                        opp = bill()
                        f3 = 2
                        x3 = opp.shoes_bdmtn(f3)
                        self.assertTrue(x3, 1100)
                        lst3.append(x3)
                    elif x == 4:
                        opp = bill()
                        f4 = 2
                        x4 = opp.net_bdmtn(f4)
                        self.assertTrue(x4, 600)
                        lst3.append(x4)
                    elif x == 5:
                        opp = table()
                        r = opp.thank2()
                        print(r)
                        break
                    else:
                        opp = table()
                        z = opp.thank()
                        print(z)
                        break
                    s3 = sum(lst3)
            elif a == 4:
                lst4 = []
                a4 = op.indoorgames()
                print(a4)
                self.assertTrue(a4, "Indoor game")
                for i in range(0, 5):
                    x = 4
                    if x == 1:
                        opp = bill()
                        f1 = 2
                        x1 = opp.Indoor_Carrom(f1)
                        self.assertTrue(x1, 800)
                        lst4.append(x1)
                    elif x == 2:
                        opp = bill()
                        f2 = 2
                        x2 = opp.Indoor_Chess(f2)
                        self.assertTrue(x2, 700)
                        lst4.append(x2)
                    elif x == 3:
                        opp = bill()
                        f3 = 2
                        x3 = opp.Indoor_Monopoly(f3)
                        self.assertTrue(x3, 900)
                        lst4.append(x3)
                    elif x == 4:
                        opp = bill()
                        f4 = 2
                        x4 = opp.Indoor_Snake(f4)
                        self.assertTrue(x4, 300)
                        lst4.append(x4)
                    elif x == 5:
                        opp=table()
                        r=opp.thank2()
                        print(r)
                        break
                    else:
                        opp = table()
                        z = opp.thank()
                        print(z)
                        break
                s4 = sum(lst4)
            elif a == 6:
                a5 = op.exit()
                print(a5)
                self.assertTrue(a5, "Thank")
                break
            elif a == 5:
                print("\n\033[34m*******************************************************")
                print("\n\033[34m\t\t\t\t\tSports World")
                print("\033[34m-------------------------------------------------------")
                print("\033[33m\t\tProducts\t\t\t\t\t\t\tPrice")
                if s1 > 0:
                    print("\033[34m\tCricket Products\t\t\t\t\t\t", s1)
                if s2 > 0:
                    print("\033[34m\tFootball Products\t\t\t\t\t\t", s2)
                if s3 > 0:
                    print("\033[34m\tBadminton Products\t\t\t\t\t\t", s3)
                if s4 > 0:
                    print("\033[34m\tIndoor Game Products\t\t\t\t", s4)
                print("\033[34m-------------------------------------------------------")
                print("\033[33m\t\tTotal\t\t\t\t\t\t\t    ", s1 + s2 + s3 + s4)
                print("\033[34m-------------------------------------------------------")
                print("\033[34m\n*******************************************************")
                break
            elif a > 6:
                break


if __name__ == '__main__':
    unittest.main()
