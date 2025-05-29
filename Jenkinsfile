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
