  //Bet you are looking why all those javascripts are in the folder aren't you?
var app = angular.module("myApp", ['duScroll']);

app.controller("myCtrl", function($q, $scope, $http, $document) {
    $scope.firstName = "John";
    $scope.lastName = "Doe";
    $scope.questions = [];

    $http.get("/api/v1/problems/")
    .success(function(response) {
    								// $scope.questions = response; 
                    //Zelf de volgorde bepalen, laat niemand dit ooit zien

                    console.log(response[2].text);
                    $scope.questions[0] = response[1];
                    $scope.questions[1] = response[5];
                    $scope.questions[2] = response[3];
                    $scope.questions[3] = response[4];
                    $scope.questions[4] = response[2];
                    $scope.questions[5] = response[0];
                    
    								ResetGame();
    							});
    
    function ResetGame(){
      $scope.activequestion = -1;
      $scope.scoreA = 99;
      $scope.scoreB = 72;
      $scope.scoreC = 50;
      $scope.scoreD = 40;
      $scope.scoreE = 30;
      $scope.scoreF = 12;
      $scope.loadNextQuestion(false);
      $scope.choosen ="";
      checkColor();
    }

    $scope.loadNextQuestion = function(scroll){
      
      $scope.activequestion++;

      if(scroll){
          var someElement = angular.element($("#question"+$scope.activequestion));
          var mainElement = angular.element($("#slidecontainer"));
          mainElement.scrollToElement(someElement, 0, 500);
      }

    	$http.get("/api/v1/problems/"+($scope.questions[$scope.activequestion].id)+"/choices/")
    	.success(function(response) {
    		$scope.questions[$scope.activequestion].choices = response; 
        

    	});

    }
    
    $scope.chooseAnswer = function(index){

      $scope.choosen = $scope.questions[$scope.activequestion].choices[index];
      var someElement = angular.element($("#answer"+$scope.activequestion));
      var mainElement = angular.element($("#slidecontainer"));
      mainElement.scrollToElement(someElement, 0, 500);
      $scope.scoreA = Math.min(Math.max($scope.scoreA + $scope.choosen.scoreA,0),100);
      $scope.scoreB = Math.min(Math.max($scope.scoreB + $scope.choosen.scoreB,0),100);
      $scope.scoreC = Math.min(Math.max($scope.scoreC + $scope.choosen.scoreC,0),100);
      $scope.scoreD = Math.min(Math.max($scope.scoreD + $scope.choosen.scoreD,0),100);
      $scope.scoreE = Math.min(Math.max($scope.scoreE + $scope.choosen.scoreE,0),100);
      $scope.scoreF = Math.min(Math.max($scope.scoreF + $scope.choosen.scoreF,0),100);
      
      checkColor();
      //TODO: Laad de info in!!!
    }

    function checkColor(){
      $scope.scoreAColor = getColor($scope.scoreA);
      $scope.scoreBColor = getColor($scope.scoreB);
      $scope.scoreCColor = getColor($scope.scoreC);
      $scope.scoreDColor = getColor($scope.scoreD);
      $scope.scoreEColor = getColor($scope.scoreE);
      $scope.scoreFColor = getColor($scope.scoreF);
    }

    function getColor(value){
        return "color"+Math.floor(value/16);
    }

    $scope.startNewGame = function(){
      ResetGame();
      var someElement = angular.element($("#question0"));
      var mainElement = angular.element($("#slidecontainer"));
      mainElement.scrollToElement(someElement, 0, 500);
    }

});

app.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[{');
  $interpolateProvider.endSymbol('}]}');
});