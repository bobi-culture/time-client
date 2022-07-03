
pipeline{

	agent any

	environment {
		IMAGE_ID = "achilles1024/time-client:latest"
		//IMAGE_ID = "achilles1024/time-client:1.${BUILD_NUMBER}"
		DOCKERHUB_CREDENTIALS=credentials('farhang.babak-dockerhub')
	}

	stages {

		stage('Build') {
			steps {
				sh "docker build -t ${IMAGE_ID} ."
			}
		}

		stage('Login') {
			steps {
				sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
			}
		}

		stage('Push') {
			steps {
				sh "docker push ${IMAGE_ID}"
			}
		}
		stage('Clean') {
         steps{
           sh "docker rmi ${IMAGE_ID}"
         }
       }

	}

	post {
		always {
			sh "docker logout"
		}
	}

}