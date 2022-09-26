pipeline {
    agent any 


    environment {
        IMAGE_TAG_NAME = "dss"
        // BUILD_NUMBER = $BUILD_NUMBER
        IMAGE_VULNERABILITY = "medium"

        // IMAGE_TAG_NAME = "dss"

        CTN_INTERNAL_PORT = 8080
        CTN_EXTERNAL_PORT = 7997
    }


    stages {
            
        stage('Build') {
            steps{
                script {
                    try {
                        sh "docker rmi -f $IMAGE_TAG_NAME:$BUILD_NUMBER"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    sh "docker build -t $IMAGE_TAG_NAME:$BUILD_NUMBER ."
                }
            }
        }


        stage('Run and Unit Test') {
            steps{
                script {
                    try {
                        sh "docker rm -f $IMAGE_TAG_NAME"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    
                    sh "docker run -it -d -p $CTN_EXTERNAL_PORT:$CTN_INTERNAL_PORT --name $IMAGE_TAG_NAME $IMAGE_TAG_NAME:$BUILD_NUMBER"
                    
                    sh "docker exec $IMAGE_TAG_NAME pytest --verbose --junit-xml=reports/results.xml tests/ && ls"
                    
                    sh "docker cp $IMAGE_TAG_NAME:/usr/src/app/reports \$(pwd)"

                    
                    try {
                        sh "docker rm -f $IMAGE_TAG_NAME"
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    
                    // junit "reports/*.xml"
                    junit "reports/results.xml"
                }
            }
        }


        stage('Analyze') {
            when {
                environment(name: "ENV", value: "prod")
            }
            steps {
                script {
                    // Scan all library vuln levels
                    try {
                        sh 'mkdir \$(pwd)/vuln-scan'
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }
                    // html output for mail
                    sh 'docker run --rm -v "//var/run/docker.sock:/var/run/docker.sock" --mount type=bind,source="\$(pwd)"/vuln-scan,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-ci-report-library#$BUILD_NUMBER.html --timeout 25m --exit-code 0 --vuln-type library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER'
                    // xml output for junit
                    // sh 'docker run --rm -v "//var/run/docker.sock:/var/run/docker.sock" --mount type=bind,source="\$(pwd)"/reports,target=/home aquasec/trivy:0.18.3 image --format template --template "@contrib/junit.tpl" -o ./home/trivy-ci-report-library#$BUILD_NUMBER.xml --timeout 25m --exit-code 0 --vuln-type library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER'
                                    
                    // junit "reports/trivy-ci-report-library#$BUILD_NUMBER.xml"
                }
            }
        }
        

        stage('Push image') {
            steps {
                echo 'Starting to build docker image'

                script {
                    // my-image:${env.BUILD_ID}
                    sh 'echo "70077007/$IMAGE_TAG_NAME:$BUILD_NUMBER"'
                    docker.withRegistry('', 'dockerHub-access' ) {
                        def customImage = docker.build("70077007/$IMAGE_TAG_NAME:$BUILD_NUMBER")
                        customImage.push()
                     }
                }
            }
        }
        

        // stage('Deploy') {
        //     steps{
        //         script {
        //             sh 'kubectl version'
        //             // sh 'kubectl apply -f \$(pwd)/k8s/ --recursive'
        //         }
        //     }
        // }

        stage('Deploy') {
            steps{
                script {                   
                    try {
                        sh 'docker rm -f ansible-deploy'
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    } 

                    sh 'my_image="70077007/$IMAGE_TAG_NAME:$BUILD_NUMBER" envsubst < k8s/deploy.yml.tmpl > k8s/k8s-deploy.yml'
                    

                    // sh 'docker run --name ansible-deploy -d -v "$WORKSPACE/playbooks:/home" ansible:1.0 ansible-playbook -i ./home/hosts ./home/deploy.yml -v'

                    // kubernetesDeploy(configs:"$WORKSPACE/mydeploy.yml", kubeconfigId: "mykubeconfig")
                    withKubeConfig([credentialsId: 'mykubeconfig', serverUrl: 'https://kubernetes.docker.internal:6443']) {
                        sh 'kubectl apply -f $WORKSPACE/k8s/k8s-deploy.yml'
                    }

                }
            }
        }

        

        // stage('analyze code') {
        //     steps {
        //         // Scan all library vuln  levels        
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-library.html --ignore-unfixed --exit-code 0 --vuln-type library  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER
        //         // Scan all os vuln  levels 
        //         docker run --rm -v '//var/run/docker.sock:/var/run/docker.sock' --mount type=bind,source="$(pwd)"/root,target=/home aquasec/trivy:0.18.3 image --format template --template @contrib/html.tpl -o ./home/trivy-dc-report-os.html --ignore-unfixed --exit-code 0 --vuln-type os  --severity CRITICAL,HIGH $IMAGE_TAG_NAME:$BUILD_NUMBER
            
        //     }
        // }


    }

    // post {
	// 	always {
	// 		echo 'The pipeline completed'
	// 		junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
	// 	}
	// 	success {				
	// 		echo "Flask Application Up and running!!"
	// 	}
	// 	failure {
	// 		echo 'Build stage failed'
	// 		error('Stopping earlyâ€¦')
	// 	}
	// }   
    post{
        always{
            mail to: "yaradatateam@gmail.com",
            subject: "App Deploy - $BUILD_NUMBER",
            body: "Hello, this is the end pipeline"
            //dir ("tmp"){
            //  emailext attachLog: true, attachmentsPattern: "**/*$BUILD_NUMBER-build.diff.html"
            //}
            //cleanWs()
        }
    }
}

