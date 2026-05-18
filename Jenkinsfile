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
      groovy
stage('Docker Info') {
  steps {
    sh 'docker info'
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
  stage('Fix Permissions') {
    steps {
      sh 'chmod -R 777 output'
    }
  }
stage('Run Script and Copy') {
  steps {
    // Ejecuta el contenedor y deja el archivo dentro
    sh 'docker run --name comisiones_tmp comisiones-app'

    // Copia el archivo desde el contenedor al host Jenkins
    sh 'docker cp comisiones_tmp:/app/output/resultado_comisiones.xlsx output/'

    // Borra el contenedor temporal
    sh 'docker rm comisiones_tmp'
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
      archiveArtifacts artifacts: 'output/resultado_comisiones.xlsx', fingerprint: true
    }
  }
      stage('List Workspace') {
        steps {
          sh 'ls -l'
    }
  }
    }
  }
