/*
    Jenkins Pipeline for QuickCalc App

    This declarative pipeline performs the following stages:

    1. Clone Repo:
        - Simulates cloning the source code repository (placeholder echo used here).

    2. Build Docker Image:
        - Builds a Docker image from the application's Dockerfile.
        - The image is tagged as 'quickcalc-app'.

    3. Run Unit Tests:
        - Executes Python unit tests inside a temporary Docker container based on the image built in the previous stage.

    4. Deploy (Local):
        - Ensures no other container is using port 5000.
        - Stops and removes any running container occupying that port.
        - Runs a new container named 'quickcalc-app' on port 5000 for local deployment/testing.

    Post Actions:
        - Always runs after the pipeline, cleaning up any container named 'quickcalc-app' to avoid resource conflicts in future runs.
*/
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build('quickcalc-app')
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'docker run --rm quickcalc-app python -m unittest discover -s .'
            }
        }

        stage('Deploy (Local)') {
            steps {
                echo 'Running container...'
                sh '''
                    PORT=5000
                    CID=$(docker ps -q --filter "publish=${PORT}")
                    if [ ! -z "$CID" ]; then
                      echo "Stopping container using port ${PORT} (ID: $CID)"
                      docker stop $CID
                      docker rm $CID
                    fi
                '''
                sh 'docker run -d -p 5000:5000 --name quickcalc-app quickcalc-app'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker rm -f quickcalc-app || true'
        }
    }
}
