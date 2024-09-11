pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops-activity_3-fall-24.git/']])
            }
        }

        stage('Installing Dependencies') {
            steps {
                sh 'make install'
            }
        }

        stage('Testing') {
            steps {
                sh 'make test'
                script {
                    def branchName = "${env.BRANCH_NAME}"
                    echo "BRANCH NAME: ${branchName}"
                }
            }
        }
    }
}