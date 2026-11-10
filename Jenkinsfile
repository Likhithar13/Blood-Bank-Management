pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Django checks') {
            steps {
                bat 'python manage.py check'
            }
        }
        stage('Unit tests') {
            steps {
                bat 'python manage.py test'
            }
        }
    }
}
