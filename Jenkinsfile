@'
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'py --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'if not exist .venv-ci py -m venv .venv-ci'
                bat '.venv-ci\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'Flask application tests passed!'
        }
        failure {
            echo 'Pipeline failed. Check the console output.'
        }
    }
}
'@ | Set-Content -Encoding UTF8 Jenkinsfile