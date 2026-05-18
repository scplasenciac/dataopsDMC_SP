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
    stage('Prepare Output') {
  steps {
    sh 'mkdir -p output'
  }
}
stage('Test Host Write') {
  steps {
    sh 'echo "test" > output/test.txt'
    sh 'ls -l output'
  }
}
    stage('Run Script') {
      steps {
         sh 'docker run --rm -u $(id -u jenkins):$(id -g jenkins) -v $PWD:/workspace comisiones-app'
      }
    }
    stage('List Host Output') {
  steps {
    sh 'ls -l output'
    sh 'pwd'
  }
}
    stage('Debug Container Output') {
  steps {
    sh 'docker run --rm -v $PWD/output:/workspace/output comisiones-app ls -l /workspace/output'
  }
}
    stage('Archive Results') {
      steps {
        archiveArtifacts artifacts: 'resultado_comisiones.xlsx', fingerprint: true
      }
    }
    stage('List Workspace') {
      steps {
        sh 'ls -l'
  }
}
  }
}
