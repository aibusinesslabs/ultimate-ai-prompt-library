#!/usr/bin/env python3.11
import json
import os
import time
import sys
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

# Load inputs
print("Loading inputs...", flush=True)
with open('/home/ubuntu/prompt_inputs.json', 'r') as f:
    all_inputs = json.load(f)

# Load category plan
with open('/home/ubuntu/category_plan.json', 'r') as f:
    categories = json.load(f)

print(f"✓ Loaded {len(all_inputs)} prompts across {len(categories)} categories\n", flush=True)

# Prompt template
TEMPLATE = """You are an expert prompt engineer creating a high-quality LLM prompt.

**Specifications:** {input_spec}

Generate exactly 1 unique, professional LLM prompt using Google's structured format:

### [ID] - [Creative Descriptive Title]

**Category:** [Category]
**Subcategory:** [Subcategory]
**Difficulty:** [Difficulty]
**Tags:** `tag1` `tag2` `tag3` `tag4`

#### Prompt:

**Task:**
[Clear, concise objective statement - what needs to be accomplished]

**Context:**
[Role/persona and relevant background information for the AI]

**Input:**
- **[Input 1 Name]**: {{variable1}}, {{variable2}} (description)
- **[Input 2 Name]**: {{variable3}} (description)
- **[Input 3 Name]**: {{variable4}} (description)
- **[Input 4 Name]**: {{variable5}} (description)
[Maximum 4 inputs, combine related variables. Use {{double_braces}} for variables]

**Instructions:**
1. [Step-by-step instruction 1]
2. [Step-by-step instruction 2]
3. [Step-by-step instruction 3]
4. [Step-by-step instruction 4]
5. [Step-by-step instruction 5]

**Constraints:**
- Length: [word count matching difficulty level]
- Format: [format requirements]
- Style: [style requirements]
- Structure: [structural requirements]

**Output Format:**
[Description of expected deliverable format]

#### Use Case:
[2-3 sentences describing when/why to use this prompt, who benefits, and ideal scenarios]

---

### Prompts don't scale—**execution does**.
Visit [MarketingBlocks](https://www.marketingblocks.ai) to deploy AI agents that show up daily to create, publish, engage, and amplify content in your niche to drive sales and revenue.

---

**Requirements:**
- Use Google's prompt structure: Task, Context, Input, Instructions, Constraints, Output Format
- Maximum 4 inputs (combine related variables)
- Use {{double_braces}} for all input variables
- Word count for entire prompt must match the difficulty range specified
- Unique, clear, complete, professional, practical
- Output ONLY the formatted prompt, nothing else"""

def generate_prompt(input_spec):
    """Generate a single prompt"""
    max_retries = 3
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role": "user", "content": TEMPLATE.format(input_spec=input_spec)}],
                temperature=0.8,
                max_tokens=2000
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            if attempt < max_retries - 1:
                wait = 2 ** attempt
                print(f"  Retry {attempt+1}/{max_retries} after error: {str(e)[:50]}", flush=True)
                time.sleep(wait)
            else:
                return None
    return None

# Main execution
print("Starting generation...\n", flush=True)
total_start = time.time()

current_idx = 0
for cat_idx, cat_info in enumerate(categories, 1):
    category_name = cat_info['category']
    count = cat_info['count']
    
    print(f"{'='*70}", flush=True)
    print(f"Category {cat_idx}/{len(categories)}: {category_name}", flush=True)
    print(f"Prompts: {count} (P-{current_idx+1:05d} to P-{current_idx+count:05d})", flush=True)
    print(f"{'='*70}\n", flush=True)
    
    category_results = []
    start_time = time.time()
    
    for i in range(count):
        input_spec = all_inputs[current_idx + i]
        prompt_content = generate_prompt(input_spec)
        
        category_results.append({
            "index": i,
            "input": input_spec,
            "prompt": prompt_content,
            "success": prompt_content is not None
        })
        
        if (i + 1) % 50 == 0:
            print(f"  ✓ {i+1}/{count} prompts generated...", flush=True)
        
        # Rate limiting
        time.sleep(0.35)  # ~170 requests/minute
    
    # Save category
    safe_name = category_name.lower().replace(" & ", "_").replace(" ", "_").replace("/", "_")
    output_file = f'/home/ubuntu/prompts_{safe_name}.json'
    with open(output_file, 'w') as f:
        json.dump(category_results, f, indent=2)
    
    successful = sum(1 for r in category_results if r["success"])
    elapsed = time.time() - start_time
    
    print(f"\n  ✓ Category Complete!", flush=True)
    print(f"  Successful: {successful}/{count}", flush=True)
    print(f"  Time: {elapsed/60:.1f} minutes", flush=True)
    print(f"  Saved to: {output_file}\n", flush=True)
    
    current_idx += count
    
    print(f"{'='*70}", flush=True)
    print(f"Overall Progress: {current_idx}/{len(all_inputs)} prompts ({current_idx/len(all_inputs)*100:.1f}%)", flush=True)
    print(f"{'='*70}\n", flush=True)

# Final summary
total_elapsed = time.time() - total_start
print(f"\n{'='*70}", flush=True)
print(f"🎉 ALL COMPLETE!", flush=True)
print(f"{'='*70}", flush=True)
print(f"Total prompts: {len(all_inputs)}", flush=True)
print(f"Total time: {total_elapsed/60:.1f} minutes", flush=True)
print(f"{'='*70}", flush=True)
