pipeline {
    agent any

    triggers {
        issueCommentTrigger('.*rerun this build.*')
    }

    stages {

        stage('Detect Project Type') {
            steps {
                script {
                    if (fileExists('pom.xml')) {
                        env.PROJECT_TYPE = 'maven'
                    } else if (fileExists('requirements.txt')) {
                        env.PROJECT_TYPE = 'python'
                    } else if (fileExists('package.json')) {
                        env.PROJECT_TYPE = 'node'
                    } else {
                        error('No dependency file found')
                    }
                    echo "Project type: ${env.PROJECT_TYPE}"
                }
            }
        }

        stage('Install') {
            steps {
                echo '[GUARDIAN] Installing dependencies...'
                script {
                    if (env.PROJECT_TYPE == 'python') {
                        sh '''
                            python3 -m venv venv
                            . venv/bin/activate
                            pip install -r requirements.txt
                        '''
                    } else if (env.PROJECT_TYPE == 'maven') {
                        sh 'mvn clean install -DskipTests'
                    } else if (env.PROJECT_TYPE == 'node') {
                        sh 'npm install'
                    }
                }
            }
        }

        stage('Dependency Compatibility Tests') {
            steps {
                echo '[GUARDIAN] Running dependency compatibility tests...'
                script {
                    if (env.PROJECT_TYPE == 'python') {
                        sh '''
                            . venv/bin/activate
                            python -m pytest tests/ -v
                        '''
                    } else if (env.PROJECT_TYPE == 'maven') {
                        sh 'mvn test'
                    } else if (env.PROJECT_TYPE == 'node') {
                        sh 'npm test'
                    }
                }
            }
        }

    }

    post {
        success {
            echo '[GUARDIAN] ✅ Build PASSED — safe to merge PR'
        }
        failure {
            echo '[GUARDIAN] ❌ Build FAILED — RAG will suggest fix'
        }
    }
}
