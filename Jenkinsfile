pipeline {
    agent any
    stages {
        stage('Detect Language') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        env.PROJECT_TYPE = 'python'
                    } else if (fileExists('pom.xml')) {
                        env.PROJECT_TYPE = 'java_maven'
                    } else if (fileExists('build.gradle')) {
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
                        sh 'mvn clean install'
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
                        // Here, run your Flask app if required, or copy files to your deployment target
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
    }
}
