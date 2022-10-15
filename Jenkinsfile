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
                script {
                    try {
                        sh "docker rmi $(docker images -f 'dangling=true' -q)"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString() 
                    } 
                } 
            }
        }

        stage('Test') {
            steps{
                // run container 
                script {
                    try {
                        sh "docker rm -f auth"
                        sh "docker run -itd --name auth -p 5577:8080 auth:latest"
                    } catch (Exception e) {
                        sh "docker run -itd --name auth -p 5577:8080 auth:latest"
                    }
                } 
                
            }
        }
        
        stage('Deploy') {
            steps{
                echo "deploy" 
            }
        }
    }
    
}

