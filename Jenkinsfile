pipeline {
    agent any
    stages {
        stage('Run Script') {
            steps {
                // This runs the script and saves the output to output.txt
                sh 'python3 sadhanaofficeschedule.py > output.txt'
                
                // Archive the output.txt file so you can access it from Jenkins
                archiveArtifacts artifacts: 'output.txt', allowEmptyArchive: true
            }
        }
        
        stage('Test') {
            steps {
                // Placeholder for test stage - just echo for now
                echo 'Testing... (Placeholder for actual tests)'
            }
        }
        
        stage('Deploy') {
            steps {
                // Placeholder for deploy stage - just echo for now
                echo 'Deploying... (Placeholder for actual deployment)'
            }
        }
    }
}
