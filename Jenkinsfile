pipeline {
    agent any
    stages {
        stage('Install dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Django checks') {
            steps {
                sh 'python manage.py check'
            }
        }
        stage('Unit tests') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
