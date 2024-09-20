pipeline {
    agent any
    environment {
        PROJECT_TYPE = '' // Define the project type as either 'python' or 'java'
    }
    stages {
        stage('Detect Language') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        echo "Python project detected"
                        env.PROJECT_TYPE = 'python'
                    } else if (fileExists('pom.xml')) {
                        echo "Java Maven project detected"
                        env.PROJECT_TYPE = 'java_maven'
                    } else if (fileExists('build.gradle')) {
                        echo "Java Gradle project detected"
                        env.PROJECT_TYPE = 'java_gradle'
                    } else {
                        error "Unknown project type. Could not find Python or Java build files."
                    }
                }
            }
        }
        stage('Build Project') {
            steps {
                script {
                    if (env.PROJECT_TYPE == 'python') {
                        echo "Building Python Project"
                        sh 'pip install -r requirements.txt'
                    } else if (env.PROJECT_TYPE == 'java_maven') {
                        echo "Building Java Maven Project"
                        sh 'mvn clean compile'
                    } else if (env.PROJECT_TYPE == 'java_gradle') {
                        echo "Building Java Gradle Project"
                        sh 'gradle build'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (env.PROJECT_TYPE == 'python') {
                        echo "Running Python Tests"
                        sh 'pytest'
                    } else if (env.PROJECT_TYPE == 'java_maven') {
                        echo "Running Java Maven Tests"
                        sh 'mvn test'
                    } else if (env.PROJECT_TYPE == 'java_gradle') {
                        echo "Running Java Gradle Tests"
                        sh 'gradle test'
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    if (env.PROJECT_TYPE == 'python') {
                        echo "Deploying Python Project"
                        // Restart Flask app and capture logs
                        sh 'pkill -f "python3 app.py" || true'
                        sh 'nohup python3 app.py > $WORKSPACE/flask_output.log 2>&1 &'
                    } else if (env.PROJECT_TYPE == 'java_maven') {
                        echo "Deploying Java Maven Project"
                        sh 'java -jar target/your-java-application.jar > $WORKSPACE/java_output.log 2>&1 &'
                    }
                }
            }
        }
        stage('Save Logs') {
            steps {
                script {
                    // Archive generated log files
                    archiveArtifacts artifacts: '*.log', allowEmptyArchive: true
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    echo "Cleaning up workspace but preserving log files"
                    // Only remove unnecessary files, not the logs
                    sh 'rm -rf $WORKSPACE/*.{py,java,xml,gradle,md}'
                }
            }
        }
    }
}
