from langchain_core.prompts import PromptTemplate

improvement_prompt_template = PromptTemplate.from_template(
    """
# Instructions
---
Update technologies.md to fully satisfy the user's request.

# Constraints
---
Must always fulfill the user's request exactly.

# Request
---
```plaintext
{request}
```

# Current Situation
---

## Application Specifications to be met
```technologies.md
{technologies}
```
"""
)
