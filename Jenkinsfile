pipeline {
    agent any 

    environment {
        auth_folder = "${WORKSPACE}/backend/auth"
        project_folder = "${WORKSPACE}/backend/project"
    }

    stages {
        stage('Build') {
            steps{
                // build docker image
                sh "cd  $auth_folder && docker build -t auth ."
                // clean docker dangling image
                sh "docker rmi $(docker images -f 'dangling=true' -q)"
            }
        }

        stage('Test') {
            steps{
                // run container 
                sh "docker run -itd --name auth -p 5577:8080 auth:latest"
            }
        }
        
        stage('Deploy') {
            steps{
                echo "deploy"
            }
        }
    }
    
}

