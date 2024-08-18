pipeline {
    // The agent requires docker to be installed on it. as this code is run on a single node and WILL NOT be run in any other location, the is real need to specify agents.1
    agent any

    triggers {
        pollSCM('H * * * *')
    }

    environment {
        IMAGE_NAME = 'mattisafur/wog'
        IMAGE_TAG = 'latest'
        DOCKER_REGISTRY = 'docker.io'
    }

    stages {
        stage('Build') {
            steps{
                // check if docker is installled
                script {
                    def dockerStatus = sh(script: 'docker --version', returnStatus: true)
                    if(dockerStatus != 0) {
                        error('Docker is not installed on the node')
                    }
                }

                dir('src/score_site') {
                    // build docker container
                    script {
                        docker.build('mattisafur/wog:latest')
                    }
                }
            }
        }
        stage('Run') {
            steps {
                dir('src/score_site')
                {
                    // start web server
                    sh 'docker compose up -d'
                }
            }
        }
        stage('Test') {
            steps {
                // check if python3 is installed on the system
                script {
                    def pythonState = sh(script: 'python3 --version', returnStatus: true)
                    if(pythonState != 0) {
                        error('Python 3 is not installed on the node')
                    }
                }

                // create and activate venv, install requirements
                // run end to end test

                sh '''
                python3 -m venv .venv
                . ./.venv/bin/activate
                pip install -r requirements.txt

                python3 ./src/e2e/e2e.py
                
                deactivate
                '''
            }
        }
        stage('Finalize') {
            steps {
                dir('src/score_site')
                {
                // stop web server
                sh 'docker compose down'
                }

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