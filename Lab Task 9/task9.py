from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def sentiment_scores(sentence):

    scores = analyzer.polarity_scores(sentence)

    print("\nSentence:", sentence)
    print("Negative:", scores['neg'] * 100, "%")
    print("Neutral :", scores['neu'] * 100, "%")
    print("Positive:", scores['pos'] * 100, "%")

    if scores['compound'] >= 0.05:
        print("Overall Sentiment: Positive")
    elif scores['compound'] <= -0.05:
        print("Overall Sentiment: Negative")
    else:
        print("Overall Sentiment: Neutral")


def demo():
    print("\n--- Demo Sentences ---")

    sentences = [
        "Geeks For Geeks is an excellent platform for CSE students.",
        "Shweta played well in the match as usual.",
        "I am feeling sad today.",
        "Artificial Intelligence is changing the world in amazing ways.",
        "The movie was terrible and I regret watching it.",
        "Today is Monday and I have a class at 9 AM.",
        "I absolutely love this new phone, it works perfectly!",
        "The service was slow and the staff were very rude."
    ]

    for s in sentences:
        sentiment_scores(s)


def user_mode():
    print("\n--- User Input Mode ---")

    while True:
        text = input("\nEnter a sentence (type 'exit' to stop): ")

        if text.lower() == "exit":
            break

        sentiment_scores(text)


def main():

    while True:
        print("\nSentiment Analysis using VADER")
        print("1. Run Demo")
        print("2. Analyze Your Own Text")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            demo()
        elif choice == "2":
            user_mode()
        elif choice == "3":
            print("Program ended.")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()