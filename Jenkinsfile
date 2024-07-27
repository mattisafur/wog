properties([pipelineTriggers([pollSCM('H * * * *')])])

pipeline {
    stages {
        stage('Checkout') {
            steps {
                // checkout SCM
                checkout scm
            }
        }
        stage('Build') {
            steps{
                // build docker container
                script {
                    docker.build('mattisafur/wog:latest')
                }
            }
        }
        stage('Run') {
            steps {
                // start web server
                sh 'docker compose up -d'
            }
        }
        stage('Test') {
            steps {
                // run end to end test
                sh 'python e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                // stop web server
                sh 'docker compose down'

                // TODO push to dockerhub
            }
        }
    }
}