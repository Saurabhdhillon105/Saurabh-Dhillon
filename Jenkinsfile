pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t yolo-fastapi .'
            }
        }

        stage('Stop Old Container') {
            steps {
                sh 'docker stop yolo || true'
                sh 'docker rm yolo || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 8000:8000 --name yolo yolo-fastapi'
            }
        }
    }
}