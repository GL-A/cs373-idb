// Define a new module for our app
var app = angular.module('index', []);


// The controller
app.controller('HeaderController',function HeaderController($scope, $location){
	// The data model. These items would normally be requested via AJAX,
	// but are hardcoded here for simplicity. See the next example for
	// tips on using AJAX.

  $scope.isActive = function (viewLocation) { 
        return $location.path().indexOf(viewLocation) == 0;
    };


});


