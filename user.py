class User():
    def __init__(self, first_name, last_name, email, age, is_rewards_member = False, gold_card_points = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        # default atributes
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points

    # print all of the users' details on separate lines
    def display_info(self):
        print(f'{self.first_name}\n{self.last_name}\n{self.email}\n{self.age}\n{self.is_rewards_member}\n{self.gold_card_points}')

    # change user's member status to True and set their gold card points to 200
    def enroll(self):
        if self.is_rewards_member == True:
            print(f'{self.first_name} is already a member.')
            return False
        else:
            print(f'{self.first_name} is enrolled into Rewards Membership!')
            self.is_rewards_member = True
            self.gold_card_points += 200

    # decrease user's points by the amount specified
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print(f'{self.first_name} does not enough points!')
        else:
            self.gold_card_points = self.gold_card_points - amount
            print(f'{self.first_name} spent {amount} points,\n{self.gold_card_points} points remaining!')

user_1 = User('John', 'Doe', 'john@halo.com', 42)
user_2 = User('Jane', 'Doe', 'jane@mystery.com', 25, True, 500)
user_1.spend_points(50)
user_2.enroll()
user_2.spend_points(80)
user_1.display_info()
user_2.display_info()
user_3 = User('Jack', 'Daniels', 'jack@daniels.com', 999)
user_3.spend_points(100)