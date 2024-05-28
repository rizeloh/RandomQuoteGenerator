import random

def get_random_quote():
    """
    Get a random quote from a predefined list of quotes.

    Returns:
    str: A randomly selected quote.
    """
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "If you look at what you have in life, you'll always have more. - Oprah Winfrey",
        "If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. - James Cameron",
        "Life is what happens when you're busy making other plans. - John Lennon"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    # Get a random quote
    quote = get_random_quote()
    print(f"Random Quote: {quote}")
