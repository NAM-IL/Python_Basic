
import os
import platform
import psutil

class CoffeeMachineNew(Exception):
    def __init__(self):
        self.ordered_menu_name = ""
        self.ordered_menu_ingredients = {}
        self.cost = 0
        self.profit_old = 0
        self.order_command = ""
        self.order_set = {"에스프레소", "espresso", "라떼", "latte", "카푸치노", "cappuccino"}
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
        self.cost = (self.MENU[self.ordered_menu_name])["cost"]
        
        if(self.ordered_menu_name == "espresso"):
            water = order_ingredients["water"]
            coffee = order_ingredients["coffee"]
            print(f"water: {water}")
            print(f"coffee: {coffee}")
            if(self.resources["water"] < water):
                 print(f"죄송합니다. 물이 충분하지 않습니다.")
                 is_possible = False
            if(self.resources["coffee"] < coffee):
                 print(f"죄송합니다. 커피가 충분하지 않습니다.")
                 is_possible = False
            else:
                is_possible = True 
        elif(self.ordered_menu_name == "latte" or self.ordered_menu_name == "cappuccino"):
            water = order_ingredients["water"]
            milk = order_ingredients["milk"]
            coffee = order_ingredients["coffee"]
            print(f"water: {water}")
            print(f"milk: {milk}")
            print(f"coffee: {coffee}")
            
            if(self.resources["water"] < water):
                 print(f"죄송합니다. 물이 충분하지 않습니다.")
                 is_possible = False
                 
            if(self.resources["milk"] < milk):
                 print(f"죄송합니다. 우유가 충분하지 않습니다.")
                 is_possible = False
                 
            if(self.resources["coffee"] < coffee):
                 print(f"죄송합니다. 커피가 충분하지 않습니다.")
                 is_possible = False
                 
            if(self.resources["water"] >= water and \
                self.resources["milk"] >= milk and \
                self.resources["coffee"] >= coffee):
                is_possible = True
        
        return is_possible

    def process_coins(self):
        """투입된 동전으로 계산된 총액을 반환한다.
        """
        print("<<< process_coins 함수 >>>>>")
        quarters = 0
        dimes = 0
        nickels = 0
        pennies = 0
        received_coin = 0
        
        cmd_insert_coin_quarters = input("Insert coin(quarters) >>>")
        cmd_insert_coin_dimes = input("Insert coin(dimes) >>>")
        cmd_insert_coin_nickels = input("Insert coin(nickels) >>>")
        cmd_insert_coin_pennies = input("Insert coin(pennies) >>>")
        print(f"quarters: {cmd_insert_coin_quarters}")
        print(f"dimes: {cmd_insert_coin_dimes}")
        print(f"nickels: {cmd_insert_coin_nickels}")
        print(f"pennies: {cmd_insert_coin_pennies}")
        
        try:    
            quarters = int(cmd_insert_coin_quarters)
        except Exception as ex:
            print(f"Error: {ex}")
            
        try:    
            dimes = int(cmd_insert_coin_dimes)
        except Exception as ex:
            print(f"Error: {ex}")
            
        try:    
            nickels = int(cmd_insert_coin_nickels)
        except Exception as ex:
            print(f"Error: {ex}")
            
        try:    
            pennies = int(cmd_insert_coin_pennies)
        except Exception as ex:
            print(f"Error: {ex}")
        
        print(f"""
                quarters($0.25): {quarters} 개,
                dimes($0.10): {dimes} 개,
                nickels($0.05): {nickels} 개,
                pennies($0.01): {pennies} 개,
               """)
        
        received_coin = round(quarters*0.25 + \
                                dimes*0.10 + \
                                nickels*0.05 + \
                                pennies*0.01, 3)
                
        print(f"received_coin: {received_coin:.2f}")
        return received_coin

    def is_transaction_successful(self, money_received, drink_cost):
        """지불이 승인되면 True를 반환하고, 금액이 부족하면 False를 리턴

        Args:
            money_received (_type_): _description_
            drink_cost (_type_): _description_
        """
        print("<<< is_transaction_successful 함수 >>>>>")
        # print(f"money_received: {money_received}, drink_cost: {drink_cost}")
        is_tr_success = False
        
        if(money_received < drink_cost):
            if (money_received > 0):
                print(f"죄송합니다. 금액이 부족합니다. 돈이 환불되었습니다.")
            else:
                print(f"죄송합니다. 금액이 부족합니다.")
        elif(money_received > drink_cost):
            print(f"거스름돈 ${round(money_received - drink_cost, 3):.2f}를 돌려드립니다.")
            is_tr_success = True
        else:
            is_tr_success = True
            
        if(is_tr_success):
            # 6.b 거래 성공 시, 음료 가격이 머신의 수익으로 추가가
            self.profit_old = self.profit
            self.profit += drink_cost
            
        return is_tr_success
        
    def make_coffee(self, drink_name, order_ingredients):
        """자원(resources)에서 필요한 재료(ingredients)를 차감한다

        Args:
            drink_name (_type_): _description_
            order_ingredients (_type_): _description_
        """
        print("\n<<< make_coffee 함수 >>>>>")
        
        water = order_ingredients["water"]
        coffee = order_ingredients["coffee"]
        cost = (self.MENU[drink_name])["cost"]
            
        # 구매 전 자원 보고서 출력
        msg = f"{drink_name} 구매 전"
        self.print_report_ext(self.profit_old, msg)
        
        if(drink_name == "espresso"):
            self.resources["water"] -= water
            self.resources["coffee"] -= coffee
            # self.profit += cost
            print(f"{drink_name}==> water: {water}, coffee: {coffee}, cost: {cost}")
        elif(drink_name == "latte" or drink_name == "cappuccino"):
            milk = order_ingredients["milk"]
            self.resources["water"] -= water
            self.resources["milk"] -= milk
            self.resources["coffee"] -= coffee
            # self.profit += cost
            print(f"{drink_name}==> water: {water}, milk: {milk}, coffee: {coffee}, cost: {cost}\n")

        # 구매 후 자원 보고서 출력
        msg = f"{drink_name} 구매 후"
        self.print_report_ext(self.profit, msg)
        
        
    def print_report_ext(self, profit, ext_msg):
        """보고서 출력
        """
        print(f""">>> {ext_msg} 보고서:
                - 물: {self.resources["water"]}ml,
                - 우유: {self.resources["milk"]}ml,
                - 커피: {self.resources["coffee"]}g,
                - 돈: ${profit}
                """.strip())
        
    def print_report(self):
        """보고서 출력
        """
        print(f""">>> 보고서:
                - 물: {self.resources["water"]}ml,
                - 우유: {self.resources["milk"]}ml,
                - 커피: {self.resources["coffee"]}g,
                - 돈: ${self.profit}
                """.strip())
        
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
    
    # 자판기에 입력한 명령어
    ordered_command = ""

    # 커피머신 클래스 인스턴스 생성
    my_coffee_machine = CoffeeMachineNew()
    
    try:
        print("----------[ 주 문 ]------------")
        # 1. 자판기에서 음료를 주문한다. (에스프레소, 라떼, 카푸치노)
        ordered_command = input("어떤 음료를 원하시나요? (에스프레소/라떼/카푸치노) >>>").strip().lower()
    except Exception as ex:
        print(f"Error: {ex}")
        
    print(f"ordered_command: {ordered_command}")
    
    # 2. "off/OFF"를 입력하면 머신은 종료됨
    while(ordered_command != "off"):
        is_order_possible = False
        is_transaction_successful = False
        ordered_menu_name = ""
        ordered_menu_cost = 0.00
        ordered_menu_ingredients = {}
        is_valid_oredred_menu = ordered_command in my_coffee_machine.order_set
        received_coin = 0.0
        
        print(f"order_set: {my_coffee_machine.order_set}")
        print(f"주문메뉴 유효성 체크(is_valid_oredred_menu): {is_valid_oredred_menu}")
    
        if(ordered_command == "report"):
            # 3. 자판기 보고서 출력
            my_coffee_machine.print_report()
        elif(ordered_command == "에스프레소" or ordered_command == "espresso"):
            ordered_menu_name = "espresso"
        elif(ordered_command == "라떼" or ordered_command == "latte"):
            ordered_menu_name = "latte"
        elif(ordered_command == "카푸치노" or ordered_command == "cappuccino"):
            ordered_menu_name = "cappuccino"
        
        if(is_valid_oredred_menu):
            ordered_menu_cost = (my_coffee_machine.MENU[ordered_menu_name])["cost"]
            ordered_menu_ingredients = (my_coffee_machine.MENU[ordered_menu_name])["ingredients"]
            my_coffee_machine.ordered_menu_name = ordered_menu_name
            my_coffee_machine.ordered_menu_ingredients = ordered_menu_ingredients
            
            # 4. 자원 충분 여부 확인 메서드 콜 - 주문한 음료를 만들기 위한 자원이 충분한지 확인한다
            is_order_possible = my_coffee_machine.is_resource_sufficient(ordered_menu_ingredients)
        else:
            if(ordered_command != "report"):
                print(f"주문메뉴가 유효하지 않습니다. 다시 입력하세요.")
        
        if(not is_order_possible and is_valid_oredred_menu):
            my_coffee_machine.print_report()
            break
        
        if(is_order_possible and is_valid_oredred_menu):
            # 5. 동전 처리 함수 콜 - 자원이 충분하면, 동전 투입을 요청한다
            received_coin = my_coffee_machine.process_coins()
            
            # 6. 거래 성공여부 확인 메서드 콜 - 주문이 가능할 경우, 결제 처리 함수 콜
            is_transaction_successful = my_coffee_machine.is_transaction_successful(received_coin, ordered_menu_cost)
            
        print(f"is_transaction_successful: {is_transaction_successful}")
        
        if(is_order_possible and is_transaction_successful):
            print(f"주문하신 음료는 {ordered_menu_name}입니다.")
            # 7. 커피 만들기 메서드 콜 - 주문한 음료의 재료를 커피 머신의 자원에서 차감한다
            my_coffee_machine.make_coffee(ordered_menu_name, ordered_menu_ingredients)
            print(f"여기 {ordered_menu_name}가 나왔습니다. 즐기세요!\n")
        
        # 1.b 음료가 제공된 후, 항상 프롬프트가 다시 표시되어 다음 고객을 받을 수 있도록 기능구현현
        try:
            # 1. 자판기에서 음료를 주문한다. (에스프레소, 라떼, 카푸치노)
            print("----------[ 주 문 ]------------")
            ordered_command = input("어떤 음료를 원하시나요? (에스프레소/라떼/카푸치노) >>>").strip().lower()
        except Exception as ex:
            print(f"Error: {ex}")
            ordered_command = ""
            
        print(f"order_command: {ordered_command}")
        
    print("see you!!")