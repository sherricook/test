import groovy.json.JsonSlurper
import org.jenkinsci.plugins.workflow.steps.FlowInterruptedException
import hudson.tasks.junit.TestResultAction
import hudson.tasks.Mailer

def call(config) {
	
	stage('Prepare Workspace') {
		// Clean workspace
		cleanWs()
		
		// Checkout source code
		checkout scm
		
		// Setup Config
		def job_config = readYaml(file: config)
        echo "Provision Windows? ${job_config.provision_win}"
        echo "Credentials: ${job_config.credentials}"
		
		WORKSPACE = "${WORKSPACE}"
		echo "WORKSPACE ${WORKSPACE}"
	}
	
	stage("Run") {
		echo "Building ${env.JOB_NAME}..."
		sh "pytest --verbose tests/test_commands.py"
    }
}

return this
