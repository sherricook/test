pipeline {
    agent { label 'linux' } // Use the label of your Linux agent

    environment {
        // Optional: define environment variables here
        REPO_URL = 'https://github.com/sherricook/test.git'
        BRANCH = 'main'
    }

    stages {

        stage('Checkout') {
            steps {
                // Use the Git plugin and specify the Git tool
                checkout([$class: 'GitSCM',
                    branches: [[name: "*/${BRANCH}"]],
                    userRemoteConfigs: [[
                        url: "${REPO_URL}",
                        credentialsId: 'Git' // Make sure this matches your Jenkins credential
                    ]],
                    gitTool: 'Default' // Name of Git installation in Global Tool Configuration
                ])
            }
        }

        stage('Build / Test') {
            steps {
                // Use Linux shell commands safely
                sh '''
                    echo "Running on Linux agent: $(hostname)"
                    echo "Workspace path: $WORKSPACE"
                    # Add more build/test commands here
                '''
            }
        }

        stage('Post-Build Cleanup') {
            steps {
                sh '''
                    echo "Build complete. Cleaning temporary files if needed."
                    # Example: rm -rf tmp/*
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished!"
        }
        success {
            echo "Build succeeded!"
        }
        failure {
            echo "Build failed!"
        }
    }
}
