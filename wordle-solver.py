import random

# Load words from file or list
with open("word_list.txt") as f:
    word_list = [word.strip().lower() for word in f if len(word.strip()) == 5]

def get_feedback(secret, guess):
    feedback = [''] * 5
    used = [False] * 5

    # First pass - correct place
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = 'G'
            used[i] = True

    # Second pass - wrong place
    for i in range(5):
        if feedback[i] == '':
            for j in range(5):
                if not used[j] and guess[i] == secret[j]:
                    feedback[i] = 'Y'
                    used[j] = True
                    break
            if feedback[i] == '':
                feedback[i] = 'B'

    return ''.join(feedback)

def eliminate_words(word_pool, guess, feedback):
    new_pool = []
    for word in word_pool:
        if get_feedback(word, guess) == feedback:
            new_pool.append(word)
    return new_pool

def ai_solver(secret_word, verbose=True):
    attempts = 0
    word_pool = word_list.copy()
    guess = "arise" if "arise" in word_pool else random.choice(word_pool)

    while True:
        attempts += 1
        feedback = get_feedback(secret_word, guess)
        if verbose:
            print(f"Attempt {attempts}: {guess.upper()} → {feedback}")

        if feedback == "GGGGG":
            break

        word_pool = eliminate_words(word_pool, guess, feedback)
        guess = random.choice(word_pool) if word_pool else None

        if not guess:
            print("❌ No words left in pool. Solver failed.")
            return attempts

    print(f"✅ Solved in {attempts} attempts.")
    return attempts

if __name__ == "__main__":
    secret = input("Enter a 5-letter secret word (or press Enter for random): ").lower()
    if secret == "":
        secret = random.choice(word_list)
    ai_solver(secret)
