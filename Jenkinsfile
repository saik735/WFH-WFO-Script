pipeline {
    agent any
    environment {
        PROJECT_TYPE = 'python'  // Hardcoded to Python for this version
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/saik735/WFH-WFO-Script.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                script {
                    echo "Setting up Python environment for version 1.0"
                    // Create virtual environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Flask App') {
            steps {
                script {
                    echo "Deploying Python Flask Project version 1.0"
                    // Kill any existing Flask process and start the app
                    sh 'pkill -f "python3 app.py" || true'
                    sh 'nohup python3 app.py > $WORKSPACE/flask_output.log 2>&1 &'
                }
            }
        }

        stage('Save Logs') {
            steps {
                script {
                    // Archive the Flask app logs
                    archiveArtifacts artifacts: '*.log', allowEmptyArchive: true
                }
            }
        }

        stage('Cleanup') {
            steps {
                script {
                    echo "Cleaning up workspace but preserving log files"
                    // Clean up workspace, keeping logs intact
                    sh 'rm -rf $WORKSPACE/*.{py,xml,gradle,md}'
                }
            }
        }
    }

    post {
        always {
            echo "Job finished, cleaning up"
            cleanWs()
        }
    }
}
