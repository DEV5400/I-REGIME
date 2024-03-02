# I-REGIME: Player Ranking and Activity Logging System

I-REGIME is a Python script that implements a simple player ranking and activity logging system. It allows players to earn or lose points, get promoted to different ranks based on their points, log their activities, and save their progress to a file for future use.

## Features

- **Ranking System**: Players are assigned ranks based on the points they accumulate. Each rank has a predefined threshold, and when a player's points exceed a threshold, they are promoted to the corresponding rank.

- **Activity Logging**: All player activities, such as earning or losing points and promotions, are logged with timestamps.

- **Slip Factor**: Implemented to gradually decrease points over time, simulating a decay or loss of points if the player is not active.

- **Data Persistence**: Player data is saved to a file with the player's name as the filename. This allows players to continue their progress from where they left off in subsequent sessions.

## Usage

1. **Installation**: No installation is required. Simply download or clone the provided Python script.

2. **Running the Script**: Execute the script using Python. It will prompt the user to enter their name and provide options to perform various actions such as crediting points, displaying logs, displaying rank, and saving data.

3. **Interacting with the System**: Follow the on-screen prompts to interact with the system. Players can earn or lose points, view their activity log, check their current rank, and save their progress before exiting the program.

## Example

```bash
$ python I-REGIME.py
Enter your name: Alice
Welcome back, Alice

Options:
1. Credit
2. Display Log
3. Display Rank
4. Save and Exit
Enter your choice: 1
Enter points earned/lost: 100
Enter the reason: Daily login bonus
Alice earned 100.00 points via Daily login bonus.

Options:
1. Credit
2. Display Log
3. Display Rank
4. Save and Exit
Enter your choice: 3
Current rank of Alice: Recruit Soldier
Current points: 1100.00

Options:
1. Credit
2. Display Log
3. Display Rank
4. Save and Exit
Enter your choice: 4
Data saved. Exiting...
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

