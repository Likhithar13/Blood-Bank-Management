# Module C – AI prompt, Git, Jenkins and Docker

## Example AI coding prompt
"Create a Django view and form for recording an emergency blood request. Use Django ORM and server-side validation. Do not implement blood compatibility rules or authorize issue of blood. Explain the code and provide tests."

## Git commands
```bash
git init
git add .
git commit -m "Initial Blood Bank Management System"
```
Create a GitHub repository, then follow GitHub's displayed instructions to add its remote and push.

## Jenkins
The included Jenkinsfile installs dependencies, runs Django checks, and runs unit tests.

## Docker
The included Dockerfile packages the Django demo application. Run:
```bash
docker build -t bloodbank-demo .
docker run -p 8000:8000 bloodbank-demo
```
