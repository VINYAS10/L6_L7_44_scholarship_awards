
import math


def parse_applicant(text):
    if not isinstance(text, str) or ":" not in text:
        return None

    category, marks = text.split(":", 1)
    category = category.strip()

    if not category:
        return None

    try:
        marks = float(marks.strip())
        if not math.isfinite(marks) or not 0 <= marks <= 100:
            return None
        return category.title(), marks
    except ValueError:
        return None


def marks_average(marks_csv):
    if not isinstance(marks_csv, str) or not marks_csv.strip():
        return None

    try:
        values = [float(r.strip()) for r in marks_csv.split(",")]

        if not all(math.isfinite(v) and 0 <= v <= 100 for v in values):
            return None

        return sum(values) / len(values)
    except ValueError:
        return None


def payable_award(text):
    if not isinstance(text, str) or "|" not in text:
        return None

    try:
        award, deduction = text.split("|", 1)
        award = float(award.strip())
        deduction = float(deduction.strip())

        if not all(math.isfinite(v) and v >= 0 for v in (award, deduction)):
            return None

        return max(award - deduction, 0)
    except ValueError:
        return None


def main():
    print("==== Running parse_applicant ====")
    user_input = input("Enter category:marks (e.g. merit:82): ")
    result = parse_applicant(user_input)
    print("Category and Marks:", result)

    print("\n==== Running marks_average ====")
    user_input = input("Enter marks as CSV (e.g. 72,85,90): ")
    result = marks_average(user_input)
    print("Average Marks:", result)

    print("\n==== Running payable_award ====")
    user_input = input("Enter award|deduction (e.g. 5000|500): ")
    result = payable_award(user_input)
    print("Payable Award:", result)


if __name__ == "__main__":
    main()

