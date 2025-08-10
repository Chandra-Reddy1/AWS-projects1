pipeline {
    agent { label 'ubuntu' } // Or 'any' if you don't have a specific label

    environment {
        TF_TOKEN_app_terraform_io = credentials('TF_TOKEN') // Jenkins secret
        AWS_DEFAULT_REGION = 'us-east-1'
        // Uncomment if you store AWS keys in Jenkins credentials
        // AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        // AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
    }

    stages {
        stage('Checkout code') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh '''
                sudo apt-get update
                sudo apt-get install -y python3 python3-pip
                python3 --version
                '''
            }
        }

        stage('Install Terraform') {
            steps {
                sh '''
                curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
                echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
                sudo apt-get update && sudo apt-get install -y terraform=1.8.5
                terraform -version
                '''
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                pip3 install --upgrade pip
                if [ -f requirements.txt ]; then pip3 install -r requirements.txt || true; fi
                '''
            }
        }

        stage('Terraform Init') {
            steps {
                sh 'terraform init'
            }
        }

        stage('Terraform Validate') {
            steps {
                sh 'terraform validate'
            }
        }

        stage('Terraform Plan') {
            steps {
                sh 'terraform plan'
            }
        }

        stage('Terraform Apply') {
            steps {
                sh 'terraform apply -auto-approve'
            }
        }
    }
}
