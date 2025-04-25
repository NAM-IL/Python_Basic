import os
import platform
import psutil
class CoffeeMachine:
    def __init__(self):
        self.ordered_menu_name = ""
        self.ordered_menu_ingredients = {}
        self.cost = 0
        self.order_command = ""
        self.order_set = {"에스프레소", "라떼", "카푸치노"}
        self.received_coin = 0
        self.MENU = {
            "espresso": {
                "ingredients": {
                    "water": 50,
                    "coffee": 18,
                },
                "cost": 1.5,
            },
            "latte": {
                "ingredients": {
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
                "cost": 2.5,
            },
            "cappuccino": {
                "ingredients": {
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
                "cost": 3.0,
            },
        }

        self.profit = 0
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }



    def is_resource_sufficient(self, order_ingredients):
        """주문을 만들 수 있을 때는 True를 반환하고, 재료가 부족할 경우에는 False를 리턴

        Args:
            order_ingredients (_type_): _description_
        """
        print("<<< is_resource_sufficient 함수 >>>>>")
        # print(f"order_ingredients: {order_ingredients}")
        is_possible = False
        if(self.order_command == "에스프레소"):
            self.ordered_menu_name = "espresso"
            self.ordered_menu_ingredients = order_ingredients
            water = self.ordered_menu_ingredients["water"]
            coffee = self.ordered_menu_ingredients["coffee"]
            print(f"water: {water}")
            print(f"coffee: {coffee}")
            if(self.resources["water"] < water):
                 print(f"죄송합니다. 물이 충분하지 않습니다.")
                 is_possible = False
            elif(self.resources["coffee"] < coffee):
                 print(f"죄송합니다. 커피가 충분하지 않습니다.")
                 is_possible = False
            else:
                self.cost = (self.MENU["espresso"])["cost"]
                is_possible = True
                 
        elif(self.order_command == "라떼"):
            self.ordered_menu_name = "latte"
            self.ordered_menu_ingredients = order_ingredients
            # self.ordered_menu_ingredients = (self.MENU["latte"])["ingredients"]
            water = self.ordered_menu_ingredients["water"]
            milk = self.ordered_menu_ingredients["milk"]
            coffee = self.ordered_menu_ingredients["coffee"]
            print(f"water: {water}")
            print(f"milk: {milk}")
            print(f"coffee: {coffee}")
            if(self.resources["water"] < water):
                 print(f"죄송합니다. 물이 충분하지 않습니다.")
                 is_possible = False
            elif(self.resources["milk"] < milk):
                 print(f"죄송합니다. 우유가 충분하지 않습니다.")
                 is_possible = False
            elif(self.resources["coffee"] < coffee):
                 print(f"죄송합니다. 커피가 충분하지 않습니다.")
                 is_possible = False
            else:
                self.cost = (self.MENU["latte"])["cost"]
                is_possible = True
        elif(self.order_command == "카푸치노"):
            self.ordered_menu_name = "cappuccino"
            self.ordered_menu_ingredients = order_ingredients
            water = self.ordered_menu_ingredients["water"]
            milk = self.ordered_menu_ingredients["milk"]
            coffee = self.ordered_menu_ingredients["coffee"]
            print(f"water: {water}")
            print(f"milk: {milk}")
            print(f"coffee: {coffee}")
            
            if(self.resources["water"] < water):
                 print(f"죄송합니다. 물이 충분하지 않습니다.")
                 is_possible = False
            elif(self.resources["milk"] < milk):
                 print(f"죄송합니다. 우유가 충분하지 않습니다.")
                 is_possible = False
            elif(self.resources["coffee"] < coffee):
                 print(f"죄송합니다. 커피가 충분하지 않습니다.")
                 is_possible = False
            else:
                self.cost = (my_coffee_machine.MENU["cappuccino"])["cost"]
                is_possible = True
        else:
            return False
        
        return is_possible

    def process_coins(self):
        """투입된 동전으로 계산된 총액을 반환한다.
        """
        print("<<< process_coins 함수 >>>>>")
        self.received_coin = 0
        cmd_insert_coin_quarters = input("Insert coin(quarters) >>>")
        cmd_insert_coin_dimes = input("Insert coin(dimes) >>>")
        cmd_insert_coin_nickels = input("Insert coin(nickels) >>>")
        cmd_insert_coin_pennies = input("Insert coin(pennies) >>>")
        print(f"quarters: {cmd_insert_coin_quarters}")
        print(f"dimes: {cmd_insert_coin_dimes}")
        print(f"nickels: {cmd_insert_coin_nickels}")
        print(f"pennies: {cmd_insert_coin_pennies}")
        
        if(cmd_insert_coin_quarters == ""):
            cmd_insert_coin_quarters = 0
        if(cmd_insert_coin_dimes == ""):
            cmd_insert_coin_dimes = 0
        if(cmd_insert_coin_nickels == ""):
            cmd_insert_coin_nickels = 0
        if(cmd_insert_coin_pennies == ""):
            cmd_insert_coin_pennies = 0
            
        quarters = int(cmd_insert_coin_quarters)
        dimes = int(cmd_insert_coin_dimes)
        nickels = int(cmd_insert_coin_nickels)
        pennies = int(cmd_insert_coin_pennies)
        
        print(f"""
              quarters($0.25): {cmd_insert_coin_quarters},
              dimes($0.10): {cmd_insert_coin_dimes},
              nickels($0.05): {cmd_insert_coin_nickels},
              pennies($0.01): {cmd_insert_coin_pennies},
               """)
        self.received_coin = round(quarters*0.25 + \
                        dimes*0.10 + \
                        nickels*0.05 + \
                        pennies*0.01, 2)
                
        print(f"received_coin: {self.received_coin}")

    def is_transaction_successful(self, money_received, drink_cost):
        """지불이 승인되면 True를 반환하고, 금액이 부족하면 False를 리턴

        Args:
            money_received (_type_): _description_
            drink_cost (_type_): _description_
        """
        print("<<< is_transaction_successful 함수 >>>>>")
        # print(f"money_received: {money_received}, drink_cost: {drink_cost}")
        ret = False
        
        if(money_received < drink_cost):
            print(f"죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다.")
            ret = False
        elif(money_received > drink_cost):
            print(f"거스름돈 ${round(money_received - drink_cost, 2)}를 돌려드립니다.")
            ret = True
        else:
            ret = True
        return ret
        
    def make_coffee(self, drink_name, order_ingredients):
        """자원(resources)에서 필요한 재료(ingredients)를 차감한다

        Args:
            drink_name (_type_): _description_
            order_ingredients (_type_): _description_
        """
        print("\n<<< make_coffee 함수 >>>>>")
        print(f""">>>{drink_name} 구매 전 보고서:
              - 물: {self.resources["water"]}ml,
              - 우유: {self.resources["milk"]}ml,
              - 커피: {self.resources["coffee"]}g,
              - 돈: ${self.profit}
              """)
        
        if(drink_name == "espresso"):
            water = order_ingredients["water"]
            coffee = order_ingredients["coffee"]
            cost = (self.MENU[drink_name])["cost"]
            self.resources["water"] -= water
            self.resources["coffee"] -= coffee
            self.profit += cost
            print(f"{drink_name}==> water: {water}, coffee: {coffee}, cost: {cost}")
        elif(drink_name == "latte"):
            water = order_ingredients["water"]
            milk = order_ingredients["milk"]
            coffee = order_ingredients["coffee"]
            cost = (self.MENU[drink_name])["cost"]
            self.resources["water"] -= water
            self.resources["milk"] -= milk
            self.resources["coffee"] -= coffee
            self.profit += cost
            print(f"{drink_name}==> water: {water}, milk: {milk}, coffee: {coffee}, cost: {cost}\n")
        elif(drink_name == "cappuccino"):
            water = order_ingredients["water"]
            milk = order_ingredients["milk"]
            coffee = order_ingredients["coffee"]
            cost = (self.MENU[drink_name])["cost"]
            self.resources["water"] -= water
            self.resources["milk"] -= milk
            self.resources["coffee"] -= coffee
            self.profit += (self.MENU[drink_name])["cost"]
            print(f"{drink_name}==> 물: {water}, 우유: {milk}, 커피: {coffee}, 가격: {cost}\n")

        print(f""">>>{drink_name} 구매 후 보고서:
              - 물: {self.resources["water"]}ml,
              - 우유: {self.resources["milk"]}ml,
              - 커피: {self.resources["coffee"]}g,
              - 돈: ${self.profit}
              """)


# [ex0424_coffee_machine_new.py](https://github.com/NAM-IL/Python_Basic/blob/main/code/ex0424_coffee_machine_new.py)

if __name__ == "__main__":
    # Terminal을 clear(macOS, Linux) 또는 cls(Windows) 명령어로 초기화
    # os.name: posix (macOS, Linux), nt (Windows)
    # [How to identify which OS Python is running on](https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on)
    if(psutil.WINDOWS):
        os.system("cls")
    else:
        os.system("clear")
    
    print(f"os.name: {os.name}")
    print(f"psutil: {psutil.WINDOWS}")
    print(f"system: {platform.system()}")
    print(f"platform: {platform.platform()}")

    my_coffee_machine = CoffeeMachine()
    
    my_coffee_machine.order_command = input("어떤 음료를 원하시나요? (에스프레소/라떼/카푸치노) >>>")
    # print(f"order_command: {order_commandf}")
    print(f"order_set: {my_coffee_machine.order_set}")
    
    while(my_coffee_machine.order_command != "off"):
        is_order_possible = False
        is_transaction_successful = False
        ordered_menu_name = ""
        ordered_menu_cost = 0.00
        ordered_menu_ingredients = {}
        
        if(my_coffee_machine.order_command == "report"):
            print(f"{my_coffee_machine.resources}")
        elif(my_coffee_machine.order_command == "에스프레소"):
            ordered_menu_name = "espresso"
            ordered_menu_cost = (my_coffee_machine.MENU[ordered_menu_name])["cost"]
            ordered_menu_ingredients = (my_coffee_machine.MENU[ordered_menu_name])["ingredients"]
            is_order_possible = my_coffee_machine.is_resource_sufficient(ordered_menu_ingredients)
        elif(my_coffee_machine.order_command == "라떼"):
            ordered_menu_name = "latte"
            ordered_menu_cost = (my_coffee_machine.MENU[ordered_menu_name])["cost"]
            ordered_menu_ingredients = (my_coffee_machine.MENU[ordered_menu_name])["ingredients"]
            is_order_possible = my_coffee_machine.is_resource_sufficient(ordered_menu_ingredients)
        elif(my_coffee_machine.order_command == "카푸치노"):
            ordered_menu_name = "cappuccino"
            ordered_menu_cost = (my_coffee_machine.MENU[ordered_menu_name])["cost"]
            ordered_menu_ingredients = (my_coffee_machine.MENU[ordered_menu_name])["ingredients"]
            is_order_possible = my_coffee_machine.is_resource_sufficient(ordered_menu_ingredients)
        else:
            is_order_possible =  False
        
        if(is_order_possible):
            # 동전 처리 함수 콜
            my_coffee_machine.process_coins()
        
        if(not is_order_possible and my_coffee_machine.order_command in my_coffee_machine.order_set):
            print(f"{my_coffee_machine.resources}")
            break
        
        if(is_order_possible):
            is_transaction_successful = my_coffee_machine.is_transaction_successful(money_received=my_coffee_machine.received_coin,
                                                    drink_cost=ordered_menu_cost)
            
        print(f"is_transaction_successful: {is_transaction_successful}")
        
        if(is_order_possible and is_transaction_successful):
            my_coffee_machine.make_coffee(ordered_menu_name, ordered_menu_ingredients)
        
        my_coffee_machine.order_command = input("어떤 음료를 원하시나요? (에스프레소/라떼/카푸치노) >>>")
        
        
    print("see you!!")