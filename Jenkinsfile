
pipeline {
    agent any

    stages {
        stage('Verify Jenkins') {
            steps {
                echo 'Jenkins pipeline started'
                echo 'Checking report publishing configuration'
            }
        }
    }

    post {
        always {
            echo 'Publishing test reports'

            junit testResults: 'reports/junit.xml',
                  allowEmptyResults: true

            publishHTML(target: [
                reportName: 'Pytest HTML Report',
                reportDir: 'reports',
                reportFiles: 'report.html',
                keepAll: true,
                alwaysLinkToLastBuild: true,
                allowMissing: true
            ])
        }
    }
}
