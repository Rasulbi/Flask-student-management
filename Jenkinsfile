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
                bat '"C:/Users/sksab/AppData/Local/Programs/Python/Python311/python.exe" --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat 'if not exist .venv-ci "C:/Users/sksab/AppData/Local/Programs/Python/Python311/python.exe" -m venv .venv-ci'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv-ci\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe -m pytest -v'
            }
        }
        stage('Check Docker') {
            steps {
                bat '"C:\\Users\\sksab\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" version'
            }
        }
         stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\sksab\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t flask-student-management:v1.%BUILD_NUMBER% .'
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