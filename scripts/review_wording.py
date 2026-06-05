"""
Lightweight wording review script for science communication content.

This script helps identify potentially risky wording in medical, health,
skincare, biotechnology, and public-facing science communication drafts.

It is a support tool only. It does not provide legal, regulatory, or medical advice.
"""

from typing import Dict, List


RISKY_WORDS: Dict[str, Dict[str, str]] = {
    "cure": {
        "risk": "high",
        "note": "May imply a disease cure claim.",
        "suggestion": "Consider: may help explain / public education only",
    },
    "treat": {
        "risk": "high",
        "note": "May imply a medical treatment claim.",
        "suggestion": "Consider: discuss / support understanding / explain mechanisms",
    },
    "guaranteed": {
        "risk": "high",
        "note": "May imply guaranteed results.",
        "suggestion": "Consider: individual situations vary",
    },
    "works for everyone": {
        "risk": "high",
        "note": "May overstate effect and ignore individual differences.",
        "suggestion": "Consider: results may vary",
    },
    "no side effects": {
        "risk": "high",
        "note": "May imply absolute safety.",
        "suggestion": "Consider: tolerance may vary",
    },
    "clinically proven": {
        "risk": "medium",
        "note": "Requires strong supporting evidence and category-appropriate context.",
        "suggestion": "Consider: supported by available evidence / observed in a study",
    },
    "doctor-developed": {
        "risk": "medium",
        "note": "May imply expert endorsement or medical authority.",
        "suggestion": "Consider: developed with reference to expert insights",
    },
    "medical-grade": {
        "risk": "medium",
        "note": "May imply medical-level performance.",
        "suggestion": "Consider: professional-inspired / research-informed",
    },
    "eliminates inflammation": {
        "risk": "high",
        "note": "May sound like a drug-like mechanism claim.",
        "suggestion": "Consider: inflammation-related pathways may be involved",
    },
    "repairs completely": {
        "risk": "medium",
        "note": "May imply complete and guaranteed repair.",
        "suggestion": "Consider: supports barrier care communication",
    },
}


def review_text(text: str) -> List[Dict[str, str]]:
    """Review text and return matched risky wording items."""
    results = []
    lower_text = text.lower()

    for word, info in RISKY_WORDS.items():
        if word in lower_text:
            results.append(
                {
                    "matched_word": word,
                    "risk": info["risk"],
                    "note": info["note"],
                    "suggestion": info["suggestion"],
                }
            )

    return results


def print_review(results: List[Dict[str, str]]) -> None:
    """Print review results in a readable format."""
    if not results:
        print("No risky wording found based on the current word list.")
        print("Manual review is still recommended.")
        return

    print("Potential risky wording found:\n")

    for index, item in enumerate(results, start=1):
        print(f"{index}. Matched wording: {item['matched_word']}")
        print(f"   Risk level: {item['risk']}")
        print(f"   Note: {item['note']}")
        print(f"   Safer suggestion: {item['suggestion']}")
        print()


if __name__ == "__main__":
    print("Paste content for wording review.")
    print("Press Enter twice to finish input.\n")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    content = "\n".join(lines)
    review_results = review_text(content)
    print()
    print_review(review_results)
