import time
while True:
    print("""
                              WELCOME TO

                        ♫★YEAR END FESTIVAL 2026★♫
                            CIS COMPANY © 2026
""")
    print("         SOOBIN HOANG SON - 7UPPERCUTS - PHUNG KHANH LINH - DAM VINH HUNG")
    print("""
                         ------------------------------

                    30 DEC 2026 | START FROM 19.00 - 23.00

                    NONE STADIUM 123 ANYWHERE ST., ABC CITY

""")
    print("    |                    |                      |                   |")
    print("    |  1 - CHECK TICKET  |  2 - GET TICKET NOW  |     3 - STAFF     |")
    print("    |                    |                      |                   |")
    
    print()
    
    choice = input("ENTER NUMBER TO SELECT AN OPTION: ")

#----------------------------------------------------------------------------------------------------------------------------#

    if choice == "1":
        
        print("\n========== CHECK TICKET ==========")

        ticket = input("ENTER TICKET ID: ").upper()
        seat = input("ENTER SEAT NUMBER: ").upper()
        print("\nCHECKING TICKET...")
        time.sleep(2)

        available_seats = [
            "A1", "A2", "A3", "A4", "A5",
            "B1", "B2", "B3", "B4", "B5",
            "C1", "C2", "C3", "C4", "C5"
        ]
        
        if ticket.startswith("CIS1702") and seat in available_seats:

            print("\n========== TICKET VERIFIED ==========")
            print("TICKET ID:", ticket)
            print("SEAT:", seat)
            print("STATUS: VALID")
            print("WELCOME TO YEAR END FESTIVAL 2026!")
            print("=====================================")

        else:
            print("\nINVALID TICKET!")
            print("WRONG TICKET ID OR SEAT NUMBER.")
            print("RETURNING TO MAIN MENU...")
            time.sleep(2)
        
#----------------------------------------------------------------------------------------------------------------------------#

    elif choice == "2":
        print("GET TICKET NOW")

        name = input("ENTER YOUR NAME: ").upper()
        print("""==============================================================
              
---------------------------SEAT MAP---------------------------

                         STAGE

       VVIP ( $99 )     A1   A2   A3   A4   A5       G
       FAN  ( $69 )     B1   B2   B3   B4   B5       A
       FUN  ( $49 )     C1   C2   C3   C4   C5       T
                                                     E

----------------------- TICKET PRIVILEGES --------------------

VVIP - Very Important Person
• Exclusive event access card provided by the organizer.
• Receive 20 bonus points upon registration.

FAN - Festival Fan
• Official event access card provided by the organizer.
• Receive 5 bonus points upon registration.


FUN - Festival Explorer
• Official event access card provided by the organizer.
• Receive a 5% discount voucher on your first purchase at any
  participating vendor.


==============================================================
""")
        seat = input(("                Input Your Comfort Seat: ")).upper()
        available_seats = [
            "A1", "A2", "A3", "A4", "A5",
            "B1", "B2", "B3", "B4", "B5",
            "C1", "C2", "C3", "C4", "C5"
        ]
        if seat in available_seats:
            if seat.startswith("A"):
                price = 99
                ticket_type = "VVIP"
                
            if seat.startswith("B"):
                price = 69
                ticket_type = "FAN"
                
            else:
                price = 49
                ticket_type = "FUN"
                
            print("\n========== CONFIRM YOUR SEAT ==========")
            print("NAME:", name)
            print("SEAT:", seat)
            print("TICKET TYPE:", ticket_type)
            print("PRICE: $", price)
            print("=======================================")
            
            confirm = input("CONFIRM YOUR SEAT? (Y/N): ").upper()
            
            if confirm == "Y":
                print("\n========== PAYMENT METHOD ==========")
                print("1 - CASH")
                print("2 - CARD")
                print("====================================")
                
                payment = input("SELECT PAYMENT METHOD: ").upper()
                if payment == 1:
                    print("\n========== CASH PAYMENT ==========")
                    print("TOTAL PRICE: $", price)
                    
                    cash = float(input("ENTER CASH RECEIVED: $"))
                    
                    if cash < price:
                        print("\nINSUFFICIENT CASH!")
                        print("YOU STILL NEED: $", price - cash)
                        print("RETURNING TO MAIN MENU...")
                        time.sleep(2)
                        continue

                    change = cash - price

                    print("\nPAYMENT SUCCESSFUL!")
                    print("CASH RECEIVED: $", cash)
                    print("TOTAL PRICE: $", price)
                    print("YOUR CHANGE: $", change)

                    payment_method = "CASH"
                    payment_status = "PAID"
                
                elif payment == "2":

                    card_number = input("ENTER 8-DIGIT CARD NUMBER: ")

                    if len(card_number) != 8:
                        print("INVALID CARD NUMBER!")
                        print("RETURNING TO MAIN MENU...")
                        time.sleep(2)
                        continue

                    card_name = input("ENTER NAME ON CARD: ").strip()

                    if card_name.lower() != name.strip().lower():
                        print("CARDHOLDER NAME DOES NOT MATCH TICKET NAME!")
                        print("PAYMENT FAILED.")
                        time.sleep(2)
                        continue

                    payment_method = "CARD"
                    payment_status = "PAID"

                else:
                    print("INVALID PAYMENT METHOD!")
                    continue
                      
            elif confirm == "N":
                print("SEAT SELECTION CANCELLED.")
            else:
                print("INVALID CONFIRMATION.")
        else:
            print("INVALID SEAT! PLEASE SELECT A SEAT FROM THE SEAT MAP.")
            
#----------------------------------------------------------------------------------------------------------------------------#

    elif choice == "3":
        print("\n========== STAFF LOGIN ==========")

        password = input("ENTER STAFF PASSWORD: ")

        if password == "tton-dangcaps1tg":
            print("\nACCESS GRANTED!")
            print("WELCOME TO STAFF MANAGEMENT SYSTEM")