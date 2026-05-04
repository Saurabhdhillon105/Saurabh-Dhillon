pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git 'https://github.com/your-repo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t yolo-fastapi .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop yolo-container || true'
                sh 'docker rm yolo-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name yolo-container yolo-fastapi'
            }
        }
    }
}