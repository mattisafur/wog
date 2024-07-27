properties([pipelineTriggers([pollSCM('H * * * *')])])

pipeline {
    stages {
        stage('Checkout') {
            // checkout SCM
            steps {
                checkout scm
            }
        }
        stage('Build') {
            // build docker container
            script {
                docker.build('wog:latest')
            }
        }
        stage('Run') {
            // start web server
            sh 'docker compose up -d'
        }
        stage('Test') {
            // run end to end test
            sh 'python e2e.py'
        }
        stage('Finalize') {
            // stop web server
            sh 'docker compose down'

            // TODO push to dockerhub
        }
    }
}