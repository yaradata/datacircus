pipeline {
    agent any 

    stages {
        stage('Build') {
            steps{
                sh "pwd"
                sh "ls -la"
                sh "cd backend/auth"
                sh "docker build -t auth ."
            }
        }

        stage('Test') {
            steps{
                sh "docker images"
                sh "docker ps -a"
            }
        }
        
        stage('Deploy') {
            steps{
                echo "deploy"
            }
        }
    }
    
}

