# Research to Content Kit

An open-source toolkit for transforming research materials into structured science communication content.

This project provides templates, examples, and lightweight workflows for converting research papers, expert interviews, clinical education materials, and technical notes into formats that are easier to communicate to the public.

It is especially designed for Chinese-language science communication, medical education, expert content production, and research-to-public-content workflows.

## Why this project exists

Researchers, clinicians, and science communicators often face the same problems:

- Research materials are complex and scattered.
- Scientific ideas are difficult to convert into public-facing content.
- Short videos, slides, articles, and social posts need different structures.
- Medical and health communication requires careful wording.
- Teams need repeatable templates instead of rewriting from zero every time.

This project aims to provide a practical open-source workflow for organizing research materials into clear, structured, and reusable content formats.

## What this toolkit includes

The toolkit will include:

- Research paper summary templates
- Science communication video script templates
- Slide outline templates
- Expert interview structuring templates
- Xiaohongshu / Douyin content planning templates
- Compliance-aware wording checklists
- Example workflows for medical and health communication
- Lightweight scripts for generating structured Markdown drafts

## Intended users

This project may be useful for:

- Researchers who want to explain their work to the public
- Clinicians creating patient education content
- Science communicators
- Medical content teams
- Health product education teams
- Students learning how to translate research into public-facing content
- Open-source contributors interested in research communication workflows

## Example use cases

### 1. Research paper to short video script

Input:

- Paper title
- Abstract
- Key findings
- Target audience
- Communication goal

Output:

- Hook
- Core message
- 3-part script structure
- Visual suggestions
- Risky wording checklist

### 2. Expert interview to structured content

Input:

- Transcript
- Expert background
- Main topic
- Audience pain points

Output:

- Expert profile summary
- Key talking points
- Short video topics
- Slide outline
- Article structure

### 3. Medical education content checklist

Input:

- Draft content
- Topic category
- Product or non-product context

Output:

- Scientific claims check
- Risk wording check
- Safer alternative wording
- Content structure suggestions

## Project structure

```text
research-to-content-kit/
├── README.md
├── LICENSE
├── templates/
│   ├── paper-to-video-script.md
│   ├── expert-interview-structure.md
│   ├── slide-outline.md
│   ├── medical-content-checklist.md
│   └── social-post-template.md
├── examples/
│   ├── acne-science-communication.md
│   ├── sleep-and-skin-barrier.md
│   └── sugar-and-acne.md
├── scripts/
│   └── generate_content_outline.py
└── docs/
    └── roadmap.md  Current status

This project is in early development.

The first milestone is to build a practical set of templates and examples for transforming medical and research materials into structured public education content.

Roadmap
v0.1.0
Add core README
Add initial template structure
Add examples for medical science communication
Add compliance-aware wording checklist
Add simple Markdown outline generator
v0.2.0
Add more examples for health, skincare, nutrition, and biotechnology topics
Add bilingual template support
Improve script generation workflow
Add contributor guide
v0.3.0
Add automated checklist tools
Add prompt templates for AI-assisted science communication
Add release workflow
Add test examples for different content types
Important note

This project is for education, documentation, and communication workflow purposes only.

It does not provide medical diagnosis, treatment advice, regulatory advice, or legal advice. Users should follow applicable laws, platform rules, and professional standards when creating medical or health-related content.

Contributing

Contributions are welcome.

You can contribute by:

Improving templates
Adding examples
Reporting unclear wording
Suggesting new workflows
Creating scripts for content structuring
Improving documentation
License

This project is licensed under the MIT License.
