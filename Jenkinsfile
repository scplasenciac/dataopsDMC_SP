pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url: 'https://github.com/scplasenciac/dataopsDMC_SP.git'
      }
    }
    stage('Build Docker Image') {
      steps {
        sh 'docker build -t comisiones-app .'
      }
    }
    stage('Run Script') {
      steps {
        sh 'docker run --rm -v $PWD:/app comisiones-app python script_comisiones.py'
      }
    }
    stage('Archive Results') {
      steps {
        archiveArtifacts artifacts: 'resultado_comisiones.xlsx', fingerprint: true
      }
    }
  }
}