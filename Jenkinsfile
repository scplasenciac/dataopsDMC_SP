pipeline {
  agent any
  environment {
    DOCKER_HOST = "tcp://docker:2375"
  }
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/scplasenciac/dataopsDMC_SP.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t comisiones-app -f Dockerfile.app .'
      }
    }
    stage('Run Script') {
      steps {
         sh 'docker run --rm -v $PWD:/app comisiones-app python /app/script_comisiones.py'
      }
    }
    stage('Archive Results') {
      steps {
        archiveArtifacts artifacts: 'resultado_comisiones.xlsx', fingerprint: true
      }
    }
  }
}
