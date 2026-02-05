### P-01323 - Comprehensive Technical Documentation for Software APIs

**Category:** Writing & Content Creation  
**Subcategory:** Technical Writing  
**Difficulty:** Advanced  
**Tags:** `technical-writing` `API-documentation` `software-engineering` `professional`

#### Prompt:

**Task:**  
Create a detailed, clear, and well-structured technical documentation for a software API that effectively communicates its functionality, usage, and integration guidelines to software developers.

**Context:**  
You are a professional technical writer with expertise in software engineering and API documentation. Your goal is to produce content that helps developers quickly understand how to implement and use the API, reducing onboarding time and minimizing usage errors.

**Input:**  
- **API Overview and Purpose**: {{api_name}}, {{api_description}} (name of the API and brief high-level description of its purpose)  
- **Endpoint Details**: {{endpoints}} (a list of API endpoints including HTTP methods, URL paths, and brief descriptions)  
- **Request and Response Specifications**: {{request_spec}}, {{response_spec}} (data formats, parameters, headers, example requests and responses for each endpoint)  
- **Authentication and Error Handling**: {{authentication_method}}, {{common_errors}} (authentication mechanism used and descriptions of common error codes with troubleshooting tips)

**Instructions:**  
1. Introduce the API by summarizing {{api_name}} and its core functionality based on {{api_description}}.  
2. Document each endpoint from {{endpoints}}, including HTTP method, URL path, and a concise description of its purpose.  
3. Detail the request and response structure for each endpoint using {{request_spec}} and {{response_spec}}, providing clear examples and parameter explanations.  
4. Explain the authentication process in depth using {{authentication_method}} and incorporate best practices for secure usage.  
5. List and describe common error responses found in {{common_errors}}, alongside guidance on how developers should handle these errors effectively.

**Constraints:**  
- Length: 500-750 words  
- Format: Use clear section headings, bullet points for lists, and code blocks for examples  
- Style: Professional, precise, and accessible to intermediate to advanced developers  
- Structure: Logical flow starting from overview, then endpoints, request/response details, authentication, and error handling

**Output Format:**  
A polished, ready-to-publish technical API documentation in markdown format including headings, bullet lists, and code sample blocks.

#### Use Case:  
Use this prompt when creating or updating API documentation to ensure clarity and completeness. Ideal for technical writers, software engineers, or product managers tasked with producing developer-focused documentation that accelerates integration and reduces support requests.