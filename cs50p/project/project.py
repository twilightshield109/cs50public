from faker import Faker
import time
import sys
from rich import print

def main():
    print("[magenta]Welcome to Typing Test![/magenta]")
    generated_text = (Faker().text()).replace(".", "")
    input("Press Enter to start typing...")
    sys.stdout.write(f"\n{generated_text}\n")

    user_input, time_taken = get_timed_input()
    wpm, time_in_min = calculate_wpm(user_input, time_taken)
    accuracy, match, no_match, total_words = chara_accuracy(generated_text, user_input)
    if accuracy < 30:
        wpm = 0

    actual_wpm = wpm - no_match

    print("\nResults:")
    print(f"\nGenerated Text: {generated_text}")
    print("User Input:", end = " ")
    colour_words(generated_text, user_input)
    print(f"\nTime Taken: {time_taken:.2f} seconds ({time_in_min:.2f} minutes)")
    print(f"Correct Words: {match}/{total_words}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"Words Per Minute (WPM): {actual_wpm:.2f} ({wpm} - {no_match})")

    if accuracy <= 50 or wpm < 40:
        print("[red]Do better next time :([/red]")
    elif accuracy >= 95 and wpm >= 60:
        print("[green]Good job! :D [/green]")
    else:
        print("Not bad! :)")

def get_timed_input():
    # record start time, capture input and record end time
    start_time = time.time()
    user_input = input("Type here: ")
    end_time = time.time()
    time_taken = end_time - start_time
    return user_input, time_taken

def calculate_wpm(typed_text, time_taken):
    word_count = len(typed_text.split())
    time_in_min = time_taken / 60
    if time_in_min > 0:
        wpm = word_count / time_in_min
    else:
        wpm = 0
    return wpm, time_in_min

# detect accuracy of user input
def chara_accuracy(gen_text, user_input):
    gen_text = gen_text.split()
    user_input = user_input.split()
    match = 0
    no_match = 0
    total_words = len(gen_text)

# Pair up characters from both strings using zip
    for g, u in zip(gen_text, user_input):
        if g == u:
            match += 1
        else:
            no_match += 1

    accuracy = (match / total_words) * 100
    return accuracy, match, no_match, total_words

def colour_words(gen_text, user_input):
    gen_text = gen_text.split()
    user_input = user_input.split()
    for g, u in zip(gen_text, user_input):
        if g == u:
            print(f"[green]{u}[/green]", end = " ")
        else:
            print(f"[red]{u}[/red]", end = " ")

if __name__ == "__main__":
    main()
