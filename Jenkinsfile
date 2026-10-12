pipeline {
    agent any
    stages
    {
        stage('Run selenium tests with pytest'){
            steps{
                echo "Running selenium tests using pytest"

                sh "pip install -r requirements.txt"

                sh "start /B python app.py"

                sh "ping 127.0.0.1 -n 5 > nul"

                sh "pytest -v"
            }
        }
        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"
                sh "docker build -t seleniumdemoapp:v1 ."
            }
        }
        stage('Docker Login') {
            steps {
                  sh 'docker login -u indupriyasanga -p Indu@2006'
                }
            }
        stage('push Docker Image to Docker Hub') {
            steps {
                echo "push Docker Image to Docker Hub"
                sh "docker tag seleniumdemoapp:v1 indupriyasanga/flaskapp:seleniumimage1"               
                    
                sh "docker push indupriyasanga/flaskapp:seleniumimage1"
                
            }
        }
        stage('Deploy to Kubernetes') { 
            steps { 
                    // apply deployment & service 
                    sh 'kubectl apply -f deployment.yaml --validate=false' 
                    sh 'kubectl apply -f service.yaml' 
            } 
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}