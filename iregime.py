from datetime import datetime, timedelta

class Player:
    RANK_THRESHOLDS = {
        "Omega": 5000000,
        "Infinity": 4000000,
        "Mu": 3000000,
        "Delta": 600000,
        "Supreme-Commander": 580000,
        "Supreme-General": 530000,
        "Supreme-Colonel": 480000,
        "Supreme-Major": 470000,
        "Supreme-Captain": 460000,
        "Supreme-Lieutenant": 455000,
        "Supreme-Sergeant": 450000,
        "Supreme-Corporal": 445000,
        "Special Supreme": 440000,
        "Supreme Soldier": 430000,
        "Arch-Commander": 420000,
        "Arch-General": 380000,
        "Arch-Colonel": 340000,
        "Arch-Major": 310000,
        "Arch-Captain": 300000,
        "Arch-Lieutenant": 295000,
        "Arch-Sergeant": 290000,
        "Arch-Corporal": 285000,
        "Special Arch": 280000,
        "Arch Soldier": 270000,
        "Mega-Commander": 260000,
        "Mega-General": 220000,
        "Mega-Colonel": 180000,
        "Mega-Major": 160000,
        "Mega-Captain": 155000,
        "Mega-Lieutenant": 150000,
        "Mega-Sergeant": 145000,
        "Mega-Corporal": 140000,
        "Special Mega": 135000,
        "Mega Soldier": 130000,
        "Vector-Commander": 120000,
        "Vector-General": 110000,
        "Vector-Colonel": 90000,
        "Vector-Major": 70000,
        "Vector-Captain": 60000,
        "Vector-Lieutenant": 55000,
        "Vector-Sergeant": 50000,
        "Vector-Corporal": 45000,
        "Special Vector": 40000,
        "Vector Soldier": 35000,
        "Recruit-Commander": 34000,
        "Recruit-General": 30000,
        "Recruit-Colonel": 24000,
        "Recruit-Major": 20000,
        "Recruit-Captain": 15000,
        "Recruit-Lieutenant": 12000,
        "Recruit-Sergeant": 7000,
        "Recruit-Corporal": 5000,
        "Special Recruit": 3000,
        "Recruit Soldier": 1000,
    }

    SLIP_FACTOR = 0.01  # 1% slip factor

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.rank = None
        self.log = []
        self.last_slip_time = datetime.now()

    def _get_current_time(self):
        return datetime.now()

    def _log_activity(self, message):
        timestamp = self._get_current_time().strftime('%Y-%m-%d %H:%M:%S')
        self.log.append(f"{timestamp} - {message}")

    def _check_promotion(self):
        for rank, threshold in self.RANK_THRESHOLDS.items():
            if self.points >= threshold:
                self.promote(rank)
                break

    def _apply_slip_factor(self):
        current_time = self._get_current_time()
        time_difference = current_time - self.last_slip_time
        hours_difference = time_difference.total_seconds() / 3600  # Convert time difference to hours

        if hours_difference >= 1:  # Apply slip factor only if at least one hour has passed
            slip_amount = self.points * self.SLIP_FACTOR
            if slip_amount != 0:
                slip_amount = round(slip_amount, 2)  # Round slip amount to 2 decimal places
                self.lose_points(abs(slip_amount), "Slip factor")
                self.last_slip_time = current_time

    def promote(self, new_rank):
        self.rank = new_rank
        self._log_activity(f"Congratulations, {self.name}! You've been promoted to {new_rank}.")

    def update_rank(self):
        self._check_promotion()

    def earn_points(self, points, reason):
        self.points += points
        self._log_activity(f"Earned {points:.2f} points via {reason}.")
        print(f"{self.name} earned {points:.2f} points via {reason}.")
        self.update_rank()

    def lose_points(self, points, reason):
        self.points -= points
        self._log_activity(f"Lost {points:.2f} points via {reason}.")
        print(f"{self.name} lost {points:.2f} points via {reason}.")
        self.update_rank()

    def display_log(self):
        print("Activity Log:")
        for entry in self.log:
            print(entry)

    def display_rank(self):
        print(f"Current rank of {self.name}: {self.rank}")
        print(f"Current points: {self.points:.2f}")

    def update(self):
        self._apply_slip_factor()

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(f"{self.name},{self.points},{self.rank}\n")
            for entry in self.log:
                file.write(entry + '\n')


def load_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        name, points, rank = lines[0].strip().split(',')
        player = Player(name, float(points))
        player.rank = rank
        for line in lines[1:]:
            player.log.append(line.strip())
    return player


def main():
    player_name = input("Enter your name: ")
    try:
        player = load_from_file(f"{player_name}.txt")
        print("Welcome back,", player.name)
    except FileNotFoundError:
        player = Player(player_name, 1000.0)

    while True:
        print("\nOptions:")
        print("1. Credit")
        print("2. Display Log")
        print("3. Display Rank")
        print("4. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            points_change = float(input("Enter points earned/lost: "))
            reason = input("Enter the reason: ")
            if points_change >= 0:
                player.earn_points(points_change, reason)
            else:
                player.lose_points(-points_change, reason)
        elif choice == "2":
            player.display_log()
        elif choice == "3":
            player.display_rank()
        elif choice == "4":
            player.save_to_file(f"{player.name}.txt")
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

        player.update()


if __name__ == "__main__":
    main()
