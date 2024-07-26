properties([pipelineTriggers([pollSCM('H * * * *')])])

pipeline {
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            docker build
        }
    }
}