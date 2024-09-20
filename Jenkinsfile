pipeline {
    agent any
    environment {
        // Define the project type as either 'python' or 'java'
        PROJECT_TYPE = '' 
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
                        // Restart Flask app to apply changes
                        sh 'pkill -f "python3 app.py" || true'
                        sh 'nohup python3 app.py &'
                    } else if (env.PROJECT_TYPE == 'java_maven') {
                        echo "Deploying Java Maven Project"
                        sh 'java -jar target/your-java-application.jar'
                    } else if (env.PROJECT_TYPE == 'java_gradle') {
                        echo "Deploying Java Gradle Project"
                        sh 'java -jar build/libs/your-java-application.jar'
                    }
                }
            }
        }
        stage('Save Logs') {
            steps {
                script {
                    // Save the Jenkins build logs using $BUILD_NUMBER or another appropriate path
                    sh 'cp $WORKSPACE/log $WORKSPACE/build-$BUILD_NUMBER.log'
                }
            }
        }
        stage('Cleanup') {
            steps {
                script {
                    echo "Cleaning up workspace"
                    sh 'rm -rf $WORKSPACE/*'
                }
            }
        }
    }
}
