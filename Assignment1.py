# Base class for Transactions (like buying or returning)
class TransactionWizard:
    def __init__(self, magic_shelf):
        self.magic_shelf = magic_shelf  # Inventory (aka magic shelf of products)
        self.bag_of_loot = []           # Items selected for purchase/return

    # Try to find the product by name and add it to the cart
    def summon_item(self, scroll_of_item_name):
        for thing in self.magic_shelf:
            if thing['name'].lower() == scroll_of_item_name.lower():
                self.bag_of_loot.append(thing)
                return True
        return False

    # Add up the price of all selected items
    def count_gold(self):
        return sum(thing['price'] for thing in self.bag_of_loot)


# Buying stuff
class TreasureHunt(TransactionWizard):
    def complete(self):
        shiny_gold = self.count_gold()
        print(f"Your Total is ${shiny_gold:.2f}.")
        print("Thank you for adventuring at Target!")
        return shiny_gold


# Returning stuff
class GuiltTrip(TransactionWizard):
    def complete(self):
        refund_gold = self.count_gold()
        print(f"Your Refund total is ${refund_gold:.2f}.")
        print("Sorry to see you go. Take your gold back!")
        return -refund_gold


# The main POS (Point of Silly) system
class SassyPOS:
    def __init__(self):
        # Our magic shelf starts with these mystical items
        self.magic_shelf = [
            {'name': 'Lego Star Wars', 'price': 25},
            {'name': 'Cookie', 'price': 5}
        ]
        self.scroll_of_legend = []  # History of treasure gained/lost (a.k.a. receipts)

    # The Great Hall of Choices
    def enter_portal(self):
        while True:
            print("\n🏰 Welcome to the Land of Target! Choose your quest:")
            print("1) Embark on a Treasure Hunt (Make a Purchase)")
            print("2) Return from a Failed Quest (Make a Return)")
            print("3) Manage the Magic Shelf (Inventory)")
            print("4) Summon the Scroll of Legends (Reports)")
            choice_of_destiny = input("What do you seek, brave one? ")

            if choice_of_destiny == '1':
                self.begin_quest(TreasureHunt)
            elif choice_of_destiny == '2':
                self.begin_quest(GuiltTrip)
            elif choice_of_destiny == '3':
                self.organize_shelf()
            elif choice_of_destiny == '4':
                self.unroll_scroll()
            else:
                print("A mysterious force whispers: 'Try again, mortal.'")

    # Handle purchase or return
    def begin_quest(self, quest_type):
        quest = quest_type(self.magic_shelf)
        while True:
            self.show_magic_shelf()
            item_choice = input("Name the item of destiny: ").strip()
            if not quest.summon_item(item_choice):
                print("That item does not exist in this realm.")
                continue
            continue_journey = input("Would you like to grab more loot? (Y/N): ").strip().lower()
            if continue_journey != 'y':
                break
        total_loot = quest.complete()
        self.scroll_of_legend.append(total_loot)

    # Add or remove items from the shelf
    def organize_shelf(self):
        while True:
            print("\n🧙 Magic Shelf Management")
            self.show_magic_shelf()
            print("1) Conjure New Item")
            print("2) Banish an Item")
            print("3) Return to the Great Hall")
            shelf_choice = input("Choose wisely: ")

            if shelf_choice == '1':
                item_name = input("Name your new enchanted item: ").strip()
                try:
                    item_price = float(input("Set its gold value: "))
                    self.magic_shelf.append({'name': item_name, 'price': item_price})
                    print("The item has been conjured!")
                except ValueError:
                    print("That's not a valid number, wizard.")
            elif shelf_choice == '2':
                banish_name = input("Name the item to banish: ").strip()
                banished = False
                for thing in self.magic_shelf:
                    if thing['name'].lower() == banish_name.lower():
                        self.magic_shelf.remove(thing)
                        banished = True
                        print("The item has been banished!")
                        break
                if not banished:
                    print("That item isn't on the shelf!")
            elif shelf_choice == '3':
                break
            else:
                print("The crystal ball didn't understand you.")

    # Show available products
    def show_magic_shelf(self):
        print("\n📦 Items on the Magic Shelf:")
        print("Item Name\tPrice")
        for thing in self.magic_shelf:
            print(f"{thing['name']}\t${thing['price']:.2f}")

    # Display report of all transactions
    def unroll_scroll(self):
        number_of_heroes = len(self.scroll_of_legend)
        total_gold = sum(self.scroll_of_legend)
        print("\n📜 Scroll of Legends:")
        print(f"Total Adventurers: {number_of_heroes}")
        print(f"Total Gold Collected: ${total_gold:.2f}")
        input("Press Enter to return to the Great Hall.")


# Begin the magical journey
magic_machine = SassyPOS()
magic_machine.enter_portal()


