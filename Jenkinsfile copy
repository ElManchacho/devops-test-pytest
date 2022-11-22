pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        sh 'pytest'
        sh 'python3 --version'
      }
    }
    stage('hello') {
      steps {
        sh 'pytest'
      }
    }
  }
}