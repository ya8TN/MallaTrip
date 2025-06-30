pipeline {
    agent any

    // --ou--
    // agent {
    //     node {
    //         label 'build'
    //     }
    // }

    tools {
        maven 'MAVEN_HOME'
    }

    options {
        // Timeout counter starts after agent is allocated
        timeout(time: 30, unit: 'SECONDS')
    }

    environment {
        APP_ENV = "DEV"
    }

    stages {
        stage('Code Checkout') {
            steps {
                git branch: 'spring-boot',
                    url: 'https://github.com/ya8TN/MallaTrip.git',
                    credentialsId: 'jenkins-example-github-pat'
            }
        }

        stage('Code Build') {
            steps {
                sh 'mvn install -Dmaven.test.skip=true'
            }
        }
    }

    post {
        always {
            echo "======always======"
        }
        success {
            echo "=====pipeline executed successfully ====="
        }
        failure {
            echo "======pipeline execution failed======"
        }
    }
}
