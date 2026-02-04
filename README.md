# The Ultimate AI Prompt Library (20,000 Prompts)

Welcome to the Ultimate AI Prompt Library, a comprehensive collection of 20,000 high-quality, structured prompts designed to cover every imaginable use case for Large Language Models (LLMs).

This repository is designed for developers, writers, marketers, entrepreneurs, students, and anyone looking to harness the full power of AI for life, career, and business.

## Features

- **Massive Collection:** 20,000 prompts, meticulously organized.
- **Google's Prompt Format:** Each prompt follows a structured format (Task, Context, Input, Instructions, Constraints, Output Format) for clarity and effectiveness.
- **Comprehensive Coverage:** Spans 85 categories across all major industries, professions, and life domains.
- **Ready to Use:** Copy and paste prompts directly into your favorite LLM.
- **Extensible:** Includes the scripts and framework for you to generate even more prompts.

## Getting Started

1.  **Browse the Categories:** Navigate to the `prompts/` directory to explore the 85 categories.
2.  **Find Your Prompt:** Open the Markdown file for a category to view the prompts.
3.  **Copy & Paste:** Copy the entire prompt text (starting from `### P-ID...`) and paste it into your LLM of choice.
4.  **Fill in the Inputs:** Replace the `{placeholder}` variables in the `Input:` section with your specific details.
5.  **Get Results:** Let the AI work its magic!

## Repository Structure

```
ultimate-ai-prompt-library/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── generation_scripts/
│   ├── generate_prompts.py
│   ├── category_plan.json
│   └── prompt_inputs.json
└── prompts/
    ├── category_1/
    │   └── category_1.md
    ├── category_2/
    │   └── category_2.md
    └── ... (85 total categories)
```

## Full Category List (85 Categories)

*This repository is a work in progress. The first category, "Writing & Content Creation," contains 1,500 prompts. The remaining categories are placeholders ready for generation using the provided scripts.*

*   **Marketing & Growth** (7 categories)
*   **Sales & Revenue** (6 categories)
*   **Business & Entrepreneurship** (6 categories)
*   **Agencies & Service Businesses** (5 categories)
*   **Creator Economy & Content** (7 categories)
*   **Careers & Professional Development** (6 categories)
*   **Personal Development & Life** (7 categories)
*   **Learning & Education** (4 categories)
*   **Writing & Communication** (5 categories)
*   **Technology & Development** (5 categories)
*   **Creative & Design** (4 categories)
*   **Finance & Money** (4 categories)
*   **Health & Wellness** (4 categories)
*   **Legal & Compliance** (2 categories)
*   **Real Estate & Property** (2 categories)
*   **Customer Service & Support** (2 categories)
*   **HR & People Management** (2 categories)
*   **Specialized Industries** (4 categories)
*   **General & Utility** (3 categories)

## How to Generate More Prompts

This repository includes everything you need to generate the remaining 18,500 prompts.

1.  **Install Dependencies:** `pip install openai`
2.  **Set API Key:** Make sure your `OPENAI_API_KEY` environment variable is set.
3.  **Run the Script:** Navigate to the `generation_scripts/` directory and run the `generate_prompts.py` script.

```bash
cd generation_scripts
python3.11 generate_prompts.py
```

The script will automatically pick up where it left off and generate prompts for the remaining categories, saving them to the correct directories.

## Contribution

We welcome contributions! Please see `CONTRIBUTING.md` for guidelines on how to add new prompts, suggest new categories, or improve existing content.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
