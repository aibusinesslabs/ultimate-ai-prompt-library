### P-00708 - Comprehensive Technical Documentation for Software APIs

**Category:** Writing & Content Creation  
**Subcategory:** Technical Writing  
**Difficulty:** Advanced  
**Tags:** `technical documentation` `API writing` `software engineering` `developer guides`

#### Prompt:

**Task:**  
Create a detailed, clear, and professional technical document that comprehensively explains a software API, enabling developers to understand, integrate, and utilize the API effectively.

**Context:**  
You are an experienced technical writer collaborating with a software engineering team to produce high-quality API documentation. The document will serve both internal developers and external clients who need precise, unambiguous instructions and reference materials to facilitate integration and troubleshooting.

**Input:**  
- **API Overview and Purpose:** {api_name}, {api_description} (name and concise explanation of the API’s functionality and goals)  
- **Endpoint Details:** {endpoints} (list of API endpoints, including HTTP methods, URL paths, parameters, request/response formats)  
- **Authentication and Security:** {auth_methods} (authentication mechanisms and security protocols the API employs)  
- **Usage Examples and Error Handling:** {code_samples}, {common_errors} (sample code snippets for common use cases and description of typical error responses with troubleshooting tips)

**Instructions:**  
1. Begin with a clear introduction outlining the API’s purpose, target users, and key features based on the API Overview and Purpose.  
2. Document each endpoint systematically: describe the endpoint’s function, method, URL, required and optional parameters, request body schema, and expected responses including status codes.  
3. Explain the authentication process in detail, including how to obtain credentials, implement authentication, and ensure secure API calls.  
4. Provide practical, well-commented code examples covering typical scenarios for easy adoption by developers.  
5. Include a comprehensive section on error handling: list common error codes, causes, and recommended resolution steps to assist debugging.

**Constraints:**  
- Length: 500-750 words  
- Format: Use clear headings, bullet points, tables for parameters and status codes, and monospace font for code snippets  
- Style: Professional, concise, and technical but accessible to developers with intermediate experience  
- Structure: Logical flow starting from overview to detailed endpoint descriptions, followed by authentication, examples, and error handling  

**Output Format:**  
A structured technical document in markdown or plain text format, with sections for Introduction, API Endpoints, Authentication, Usage Examples, and Error Handling, formatted for clarity and ease of navigation.

#### Use Case:  
Use this prompt when needing to generate or update comprehensive API documentation that supports developer onboarding, integration, and troubleshooting. Ideal for technical writers, API product managers, or engineering teams preparing developer-facing materials.