node('agent1') {

    def config = readYaml file: 'config/config.yaml'

    echo "Provision Windows: ${config.provision_win}"
    echo "Credentials: ${config.credentials}"

    withEnv([
        "PROVISION_WIN=${config.provision_win}"
    ]) {

        config.credentials.each { cred ->
            withCredentials([usernamePassword(credentialsId: cred, usernameVariable: 'NAME', passwordVariable: 'VALUE')]) {
                echo "Loaded credentials: $cred $NAME $VALUE"
            }
        }
    }

    def main = load 'test_execution/main.groovy'
    main.call(config)

}