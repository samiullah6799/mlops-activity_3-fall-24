pipeline {
    agent any
    stages {
        stage ('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops-activity_3-fall-24.git/']])
            }
        }

        stage ('Build') {
            steps {
                sh 'make install'
            }
        }

        stage ('Test') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    def branchName = '${env.BRANCH_NAME}'
                    println('BRANCH NAME: ${branchName}')
                    deploy(branchName)
                }
            }
        }
    }
}

def void deploy(String branchName) {
    println(branchName)
}