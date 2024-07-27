properties([pipelineTriggers([pollSCM('H * * * *')])])

pipeline {
    // The agent requires docker to be installed on it. as this code is run on a single node and WILL NOT be run in any o0ther location, the is real need to specify agents.1
    agent any

    stages {
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
                // create and activate venv
                sh '''
                python3 -m venv .venv
                source .venv/Scripts/activate
                pip install -r requirements.txt
                '''

                // run end to end test
                sh 'python3 e2e.py'

                // deactivate and remove venv
                sh '''
                deactivate
                rm -r .venv
                '''
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