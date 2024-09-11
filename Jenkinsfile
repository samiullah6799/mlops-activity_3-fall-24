pipeline {
    agent any
    stages {
        stage ('checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/dev']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/samiullah6799/mlops-activity_3-fall-24.git/']])
            }
        }

        stage ('Build') {
            steps {
                sh 'make install'
            }
        }

        stage ('Testing') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage ('Deploy') {
            steps {
                script {
                    def branchName = "${env.BRANCH_NAME}"
                    println("BRANCH NAME : ${branchName}")
                    println("MLOps Batch 21")
                }
            }
        }
    }
}