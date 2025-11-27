def call(config) {

    stage("External Pipeline") {
        echo "External pipeline received this:"
        echo "Provision Windows? ${config.provision_win}"
        echo "Credentials: ${config.credentials}"
    }
	
	stage('Build') {
		// Clean workspace before build
		cleanWs()
		// Explicitly checkout source code
		checkout scm
		echo "Building ${env.JOB_NAME}..."
	}
}

return this
