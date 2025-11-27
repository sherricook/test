node('agent1') {

    def config = readYaml file: 'config/config.yaml'

    echo "Provision Windows: ${config.provision_win}"
    echo "Credentials: ${config.credentials}"

    def main = load 'test_execution/main.groovy'
    main.call(config)

}