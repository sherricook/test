def call(config) {

    stage("External Pipeline") {
        echo "External pipeline received this:"
        echo "Provision Windows? ${config.provision_win}"
        echo "Credentials: ${config.credentials}"
    }
}

return this
