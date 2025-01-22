# Prime Game

`Algorithm`
`Python`


The Prime Game is a simple yet fun number game often used in programming problems or competitive coding challenges. Here's a breakdown of a basic version of the game:

**Rules:**
1. Two players, say Alice and Bob, take turns choosing numbers from a given list.
2. A chosen number must be a prime number, and once a number is chosen, it is removed from the list.
3. The player who cannot make a valid move loses the game.

## Objective:
Determine the winner of the game given a list of numbers and assuming both players play optimally.

### Steps to Solve:
1. **Identify the Primes**: Use a prime-checking algorithm (like the Sieve of Eratosthenes for efficiency) to identify all the prime numbers in the given list.
2. **Count the Primes**: The winner often depends on how many primes are present since the players take turns.
	- If the count of primes is odd, the first player (Alice) wins.
	- If the count is even, the second player (Bob) wins.
3. **Simulate the Game** (optional for more advanced cases): If there are additional rules, simulate the entire game to determine the winner.
