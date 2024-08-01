properties([pipelineTriggers([pollSCM('H * * * *')])])

pipeline {
    // The agent requires docker to be installed on it. as this code is run on a single node and WILL NOT be run in any other location, the is real need to specify agents.1
    agent any

    environment {
        IMAGE_NAME = 'mattisafur/wog'
        IMAGE_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
    }

    stages {
        stage('Build') {
            steps{
                // check is docker is installled
                def dockerVersion = sh 'docker --version'
                if(!dockerVersion) {
                    error('Docker is not installed on the node')
                }

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
                // check if python3 is installed on the system
                def pythonVersion = sh 'python3 --version'
                if(!pythonVersion) {
                    error('Python 3 is not installed on the node')
                }

                // create and activate venv, install requirements
                // run end to end test
                sh '''
                python3 -m venv .venv
                . ./.venv/bin/activate
                pip install -r requirements.txt

                python3 e2e.py
                
                deactivate
                '''
            }
        }
        stage('Finalize') {
            steps {
                // stop web server
                sh 'docker compose down'

                // push image to dockerhub
                withDockerRegistry([credentialsId: 'dockerhub-mattisafur', url: '']) {
                    sh 'docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
                }
            }
        }
    }
    post {
        always {
            // delete venv
            sh 'rm -r .venv'

            // prune docker
            sh 'docker system prune -af'
        }
    }
}