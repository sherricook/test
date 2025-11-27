import groovy.json.JsonSlurper
import org.jenkinsci.plugins.workflow.steps.FlowInterruptedException
import hudson.tasks.junit.TestResultAction
import hudson.tasks.Mailer

def call(config) {

    stage("Get Config") {
		def job_config = readYaml(file: config)
        echo "External pipeline received this:"
        echo "Provision Windows? ${job_config.provision_win}"
        echo "Credentials: ${job_config.credentials}"
    }
	
	stage('Prepare Workspace') {
		// Clean workspace before build
		cleanWs()
		// Explicitly checkout source code
		checkout scm
		echo "Building ${env.JOB_NAME}..."
		WORKSPACE = "${WORKSPACE}"
		echo "WORKSPACE ${WORKSPACE}"
	}
}

return this
