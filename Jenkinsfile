pipeline {
    agent any 

    environment {
        auth_folder = "${WORKSPACE}/backend/auth"
        project_folder = "${WORKSPACE}/backend/project"
    }

    stages {
        stage('Build') {
            steps{
                sh "pwd"
                sh "ls -la"
                echo "${WORKSPACE}/backend/auth"
                sh "cd  $auth_folder && docker build -t auth ."
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

