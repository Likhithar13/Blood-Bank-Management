# Module E – Quality, privacy and ethics

## Quality attributes
- Reliability: validate input and test main workflows.
- Security: use Django CSRF protection and built-in ORM; keep secret keys out of public repositories in real deployments.
- Usability: simple navigation and readable tables/forms.
- Maintainability: separate models, forms, views and templates.
- Efficiency: retrieve only recent requests on the dashboard.

## SonarQube
The included sonar-project.properties gives a basic project configuration. Run a SonarQube server/scanner according to your lab setup and capture the analysis result.

## Ethical and safety limitations
- Use fictional data in the student demonstration.
- Protect donor contact details; restrict access in a real system.
- Do not use this demo to decide blood compatibility or issue blood.
- Stock count is not proof of suitability, screening, cross-matching, expiry or availability.
- Qualified blood-bank professionals must verify every clinical and emergency decision.
- AI-generated code and test cases require human review.
