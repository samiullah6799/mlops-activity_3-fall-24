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
                sh 'source venv/bin/activate'
                sh 'make install'
            }
        }

        stage('Testing') {
            steps {
                sh 'source venv/bin/activate'
                sh 'python3 test.py'
                script {
                    def branchName = "${env.BRANCH_NAME}"
                    echo "BRANCH NAME: ${branchName}"
                }
            }
        }
    }
}