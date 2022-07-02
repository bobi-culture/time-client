
pipeline{

	agent any

	environment {
		DOCKERHUB_CREDENTIALS=credentials('farhang.babak-dockerhub')
	}

	stages {

		stage('Build') {
			steps {
				sh 'docker build -t achilles1024/time-client:latest .'
			}
		}

		stage('Login') {
			steps {
				sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}

		stage('Push') {
			steps {
				sh 'docker push achilles1024/time-client:latest'
			}
		}
	}

	post {
		always {
			sh 'docker logout'
		}
	}

}