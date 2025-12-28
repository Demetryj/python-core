"""Find numbers in text with a generator and sum them via a higher-order function."""

import re
from typing import Callable, Generator

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    

def generator_numbers(text: str) -> Generator[float, None, None]:
    """Yield each real number found in the input text as a float."""
    pattern = r"\d+(?:\.\d+)?"
    # Find all numeric substrings (integers or decimals) and iterate through them.
    number_list = re.findall(pattern, text)
    for number in number_list:
        yield float(number)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """Sum all numbers produced by the provided generator function."""
    # Use the passed generator function to iterate over numbers and sum them.
    return sum(func(text))

def main() -> None:
    # Compute total income by summing all numbers in the text.
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    

    

if __name__ == "__main__":
    main()
