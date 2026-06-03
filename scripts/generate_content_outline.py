"""
Generate a simple Markdown outline for science communication content.

This script is designed for early-stage workflow testing.
It helps turn a topic into a structured content outline for public education,
short videos, slides, or social posts.
"""

from datetime import datetime


def generate_outline(topic, audience="general public", content_type="short video"):
    today = datetime.now().strftime("%Y-%m-%d")

    outline = f"""# Content Outline

Generated on: {today}

## Topic

{topic}

## Target audience

{audience}

## Content type

{content_type}

## Core message

Write the main message of this topic in one sentence.

## Public-facing question

Convert the topic into a simple question that the audience may care about.

Example:

- Why does this happen?
- What does this mean in daily life?
- What is commonly misunderstood about this topic?

## Suggested structure

### 1. Opening hook

Start with a relatable problem, question, or misunderstanding.

### 2. Background

Explain why this topic matters.

### 3. Scientific explanation

Explain the key mechanism or research finding in simple language.

### 4. Public education interpretation

Translate the scientific idea into practical understanding.

### 5. Risk wording review

Check whether the content includes:

- Diagnosis claims
- Treatment claims
- Guaranteed results
- Overstated scientific claims
- Product effect claims without proper support

### 6. Safer wording

Use careful expressions such as:

- May be related to
- May help explain
- Is associated with
- Individual situations vary
- This content is for education only

### 7. Closing

End with a clear summary or reminder.

## Notes

Add references, reviewer comments, and future revisions here.
"""
    return outline


if __name__ == "__main__":
    topic = input("Enter topic: ").strip()

    if not topic:
        topic = "Example science communication topic"

    audience = input("Enter target audience, or press Enter for default: ").strip()
    if not audience:
        audience = "general public"

    content_type = input("Enter content type, or press Enter for default: ").strip()
    if not content_type:
        content_type = "short video"

    result = generate_outline(topic, audience, content_type)

    print("\n" + result)
